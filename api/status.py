import json
import os
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        region = os.environ.get("AWS_REGION") or os.environ.get(
            "AWS_DEFAULT_REGION"
        )
        payload = {
            "ok": True,
            "service": "aws-cli-vercel-connector",
            "aws": {
                "regionConfigured": bool(region),
                "accessKeyConfigured": bool(os.environ.get("AWS_ACCESS_KEY_ID")),
                "secretKeyConfigured": bool(
                    os.environ.get("AWS_SECRET_ACCESS_KEY")
                ),
                "sessionTokenConfigured": bool(
                    os.environ.get("AWS_SESSION_TOKEN")
                ),
            },
        }
        body = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
