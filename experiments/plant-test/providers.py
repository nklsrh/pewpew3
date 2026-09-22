"""OpenAI-compatible backends, including two that need no key and no signup.

Stdlib only - no pip install. Anonymous providers are rate-limited hard, so every
call is throttled and the runner checkpoints after each one.
"""
import json
import os
import time
import urllib.error
import urllib.request

PROVIDERS = {
    # Anonymous, no key, no signup. 2 requests/min per IP per model.
    "ovh": dict(
        url="https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/chat/completions",
        model="gpt-oss-120b", rpm=2, key_env=None,
    ),
    # Anonymous, no key. 10 RPM but only 60 requests/hour - fine for a partial run.
    "llm7": dict(
        url="https://api.llm7.io/v1/chat/completions",
        model="gpt-oss:20b", rpm=10, key_env=None,
    ),
    # Free tier, needs a free key from console.groq.com.
    "groq": dict(
        url="https://api.groq.com/openai/v1/chat/completions",
        model="openai/gpt-oss-120b", rpm=30, key_env="GROQ_API_KEY",
    ),
}

_last_call = {}


def _throttle(name: str):
    gap = 60.0 / PROVIDERS[name]["rpm"]
    prev = _last_call.get(name)
    if prev is not None:
        wait = gap - (time.time() - prev)
        if wait > 0:
            time.sleep(wait)
    _last_call[name] = time.time()


def call(name: str, system: str, prompt: str, max_tokens: int = 2000,
         temperature: float = 1.0, attempts: int = 4) -> str:
    """One completion. Raises RuntimeError if every attempt fails."""
    p = PROVIDERS[name]
    headers = {"Content-Type": "application/json"}
    if p["key_env"]:
        key = os.environ.get(p["key_env"])
        if not key:
            raise RuntimeError(f"{name} needs {p['key_env']} set")
        headers["Authorization"] = f"Bearer {key}"

    body = json.dumps({
        "model": p["model"],
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature,
    }).encode()

    last = None
    for i in range(attempts):
        _throttle(name)
        try:
            req = urllib.request.Request(p["url"], data=body, headers=headers)
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.loads(r.read())
            return data["choices"][0]["message"]["content"].strip()
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read()[:200].decode('utf8', 'replace')}"
            if e.code in (429, 500, 502, 503, 529):
                time.sleep(min(60, 5 * 2 ** i))       # backoff on transient
                continue
            if e.code in (403, 407):
                raise RuntimeError(
                    f"{name}: {last}\nBlocked by a network policy, not the provider. "
                    "Run this from a machine with open egress.") from None
            raise RuntimeError(f"{name}: {last}") from None
        except Exception as e:                         # timeouts, resets, bad JSON
            last = repr(e)
            time.sleep(min(60, 5 * 2 ** i))
    raise RuntimeError(f"{name}: gave up after {attempts} attempts. Last: {last}")


def extract_json(text: str) -> dict:
    """Free models ignore response_format, so recover the first JSON object."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    while start != -1:
        depth, in_str, esc = 0, False, False
        for i in range(start, len(text)):
            c = text[i]
            if in_str:
                if esc:
                    esc = False
                elif c == "\\":
                    esc = True
                elif c == '"':
                    in_str = False
            elif c == '"':
                in_str = True
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start:i + 1])
                    except json.JSONDecodeError:
                        break
        start = text.find("{", start + 1)
    raise ValueError(f"no JSON object found in: {text[:200]}")
