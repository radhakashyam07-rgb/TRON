from http.server import BaseHTTPRequestHandler, HTTPServer
import json


HOST = "127.0.0.1"
PORT = 8080


class TronHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):

        response = json.dumps(data).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()

        self.wfile.write(response)

    def do_GET(self):

        if self.path == "/":

            self.send_json({
                "system": "TRON",
                "version": "P-01",
                "status": "online"
            })

            return

        if self.path == "/api/status":

            self.send_json({
                "tron": "online",
                "sara": "initializing",
                "search": "initializing",
                "storage": "remote-core"
            })

            return

        self.send_json({
            "error": "TRON route not found"
        }, 404)

    def do_POST(self):

        if self.path != "/api/search":

            self.send_json({
                "error": "TRON route not found"
            }, 404)

            return

        length = int(
            self.headers.get("Content-Length", 0)
        )

        body = self.rfile.read(length)

        try:
            data = json.loads(body.decode("utf-8"))

            query = data.get("query", "").strip()

            if not query:
                self.send_json({
                    "error": "Search query is empty"
                }, 400)
                return

            self.send_json({
                "engine": "TRON",
                "query": query,
                "status": "received",
                "message": "TRON search engine is ready for its index."
            })

        except Exception:
            self.send_json({
                "error": "Invalid request"
            }, 400)


def start_tron():

    server = HTTPServer(
        (HOST, PORT),
        TronHandler
    )

    print("TRON P-01 Core")
    print(f"Server: http://{HOST}:{PORT}")
    print("Status: ONLINE")

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        print("\nTRON shutting down...")

    finally:
        server.server_close()


if __name__ == "__main__":
    start_tron()
