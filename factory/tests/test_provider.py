"""Isolated provider tests: no external calls, no real credentials used."""
import io
import json
import unittest
from unittest.mock import patch
from factory import provider


class FakeResponse:
    def __init__(self, data):
        self.data = json.dumps(data).encode()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return False
    def read(self, n):
        return self.data[:n]


class ProviderTests(unittest.TestCase):
    def test_status_never_exposes_key(self):
        key = "test-secret-not-for-logs"
        ready = provider.readiness({
            "ANTHROPIC_API_KEY": key,
            "ANTHROPIC_MODEL": "claude-sonnet-4-5-20250929",
            "FD_CODER_PROVIDER": "anthropic"})
        self.assertEqual(ready["status"], "READY")
        self.assertNotIn(key, json.dumps(ready))
        self.assertEqual(provider.readiness({})["status"], "CONFIGURATION_REQUIRED")

    def test_valid_mock_response(self):
        bp = {
            "id": "FD-AUTO-P1-TEMPORAL-DIAGNOSTIC", "version": 1,
            "requirements": "Read-only report",
            "allowed_paths": ["src/financialdata/", "tests/"]}
        env = {"ANTHROPIC_API_KEY": "dummy-test-key",
               "ANTHROPIC_MODEL": "claude-sonnet-4-5-20250929"}
        response = {
            "stop_reason": "end_turn",
            "content": [{"type": "text", "text": json.dumps({
                "files": [{"path": "tests/test_generated.py", "content": "import unittest\n"}]})}],
        }
        calls = []
        def fake_open(request, timeout=120):
            calls.append({"url": request.full_url, "timeout": timeout,
                          "version": request.headers.get("Anthropic-version")})
            return FakeResponse(response)
        files = provider.generate_files(bp, "Governance test", env=env, opener=fake_open)
        self.assertEqual(files[0]["path"], "tests/test_generated.py")
        self.assertEqual(calls[0]["url"], provider.API)
        self.assertEqual(calls[0]["version"], provider.API_VERSION)

    def test_truncation_refusal_and_json_invalid_fail_closed(self):
        for result in (
            {"stop_reason": "max_tokens", "content": [{"type": "text", "text": '{"files":[]}'}]},
            {"stop_reason": "refusal", "content": [{"type": "text", "text": '{"files":[]}'}]},
            {"stop_reason": "end_turn", "content": [{"type": "text", "text": "not JSON"}]},
            {"stop_reason": "end_turn", "content": [{"type": "text", "text": '{"title":"wrong"}'}]},
        ):
            with self.subTest(result=result["stop_reason"]):
                with self.assertRaises(ValueError):
                    provider.extract_files(result)

    def test_missing_credentials_prevents_network(self):
        with self.assertRaisesRegex(RuntimeError, "CONFIGURATION_REQUIRED"):
            provider.generate_files({"allowed_paths": ["tests/"]}, "Governance",
                                    env={}, opener=lambda *args, **kw: self.fail("Network must not be called"))


if __name__ == "__main__":
    unittest.main()
