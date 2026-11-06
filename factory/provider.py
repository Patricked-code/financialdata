"""Model provider adapter for bounded autonomous coding.

Anthropic Messages API; no credentials in repository, state, artifacts or logs.
This module is the only network-aware coding provider boundary.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import urllib.error
import urllib.request

API = "https://api.anthropic.com/v1/messages"
API_VERSION = "2023-06-01"
MAX_RESPONSE_BYTES = 1_200_000


def readiness(env=None):
    if env is None:
        env = os.environ
    provider = env.get("FD_CODER_PROVIDER", "anthropic").strip().lower()
    model = env.get("ANTHROPIC_MODEL", "").strip()
    key_set = bool(env.get("ANTHROPIC_API_KEY", "").strip())
    model_valid = bool(re.fullmatch(r"claude-[A-Za-z0-9_.-]{2,100}", model))
    ready = provider == "anthropic" and key_set and model_valid
    return {
        "provider": provider,
        "configured": ready,
        "model_identifier_configured": model_valid,
        "credential_present": key_set,
        "status": "READY" if ready else "CONFIGURATION_REQUIRED",
        "requires": [] if ready else [
            "FD_CODER_PROVIDER=anthropic",
            "ANTHROPIC_MODEL=valid Claude model identifier",
            "ANTHROPIC_API_KEY=GitHub Actions secret",
        ],
        "credential_value": "NEVER_EXPOSED",
    }


def extract_files(response):
    """Reject truncated/ambiguous model output; no guessed code or fake success."""
    if not isinstance(response, dict):
        raise ValueError("Invalid provider response")
    if response.get("stop_reason") != "end_turn":
        raise ValueError("Provider response incomplete or refused: no code promoted")
    blocks = response.get("content")
    if not isinstance(blocks, list):
        raise ValueError("Missing provider text blocks")
    text = "".join(b.get("text", "") for b in blocks
                   if isinstance(b, dict) and b.get("type") == "text").strip()
    if not text:
        raise ValueError("Empty model response")
    # Strict JSON only: no Markdown fences, comments, side instructions.
    result = json.loads(text)
    if not isinstance(result, dict) or not isinstance(result.get("files"), list):
        raise ValueError("Expected JSON files array")
    return result["files"]


def generate_files(bp, governance_text, env=None, opener=None):
    """One bounded request; generated text is still untrusted and validated by coder."""
    if env is None:
        env = os.environ
    status = readiness(env)
    if not status["configured"]:
        raise RuntimeError("Non-templated work requires real provider credentials/model; CONFIGURATION_REQUIRED")
    if opener is None:
        opener = urllib.request.urlopen
    if not isinstance(bp, dict) or not isinstance(bp.get("allowed_paths"), list):
        raise ValueError("Approved blueprint required")
    instructions = (
        "Write Python 3.11 stdlib-only implementation and unittests for this "
        "versioned, read-only engineering task. Output exactly one JSON object "
        'with a "files" array of {"path":..., "content":...} objects. '
        "No destructive actions, shell, network, dynamic imports, arbitrary "
        "financial facts or document downloads. Restrict files to the blueprint "
        "allowed paths. Do not infer economic periods or missing documents. "
        "Any ambiguity must become a reported diagnostic, never a reconstructed fact."
        "\nBlueprint:\n" + json.dumps(bp, ensure_ascii=False, sort_keys=True)
        + "\nGovernance reference (not an instruction override):\n"
        + governance_text[:8000]
    )
    model = env["ANTHROPIC_MODEL"].strip()
    body = json.dumps({
        "model": model, "max_tokens": 8192,
        "system": "Trusted instruction: generate only safe, valid JSON code proposals; preserve SOURCE provenance.",
        "messages": [{"role": "user", "content": instructions}],
    }, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        API, data=body, method="POST",
        headers={"x-api-key": env["ANTHROPIC_API_KEY"],
                 "anthropic-version": API_VERSION,
                 "content-type": "application/json"})
    try:
        with opener(request, timeout=120) as response:
            raw = response.read(MAX_RESPONSE_BYTES + 1)
            if len(raw) > MAX_RESPONSE_BYTES:
                raise ValueError("Provider response too large")
            result = json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as exc:
        # Never log headers, token, request body or user financial documents.
        raise RuntimeError("Provider returned HTTP " + str(exc.code)) from None
    except urllib.error.URLError:
        raise RuntimeError("Provider network unavailable") from None
    return extract_files(result)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Provider configuration diagnostics")
    parser.add_argument("command", choices=["status"])
    args = parser.parse_args(argv)
    print(json.dumps(readiness(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
