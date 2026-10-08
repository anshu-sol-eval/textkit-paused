import json
import urllib.request

DEFAULT_TIMEOUT = 30


class OpenAIProvider:
    """Thin wrapper that sends a prompt to an OpenAI-compatible endpoint."""

    def __init__(self, base_url, api_key, timeout=DEFAULT_TIMEOUT):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

    def build_request(self, prompt):
        body = json.dumps({"input": prompt}).encode()
        return urllib.request.Request(
            self.base_url + "/v1/responses",
            data=body,
            headers={"Authorization": "Bearer " + self.api_key,
                     "Content-Type": "application/json"},
        )

    def complete(self, prompt, opener=urllib.request.urlopen):
        req = self.build_request(prompt)
        with opener(req, timeout=DEFAULT_TIMEOUT) as resp:
            return json.loads(resp.read())
