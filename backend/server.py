"""
TRON Backend Server
P-01
Connects TRON UI + Search + SARA
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from tron_core import TronCore


HOST = "127.0.0.1"
PORT = 8080

tron = TronCore()


class TronHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):

        response = json.dumps(data).encode("utf-8")

        self.send_response(status)

        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )

        self.send_header(
            "Content-Length",
            str(len(response))
        )

        self.send_header(
            "Access-Control-Allow-Origin",
            "*"
        )

        self.end_headers()

        self.wfile.write(response)


    def read_json(self):

        length = int(
            self.headers.get("Content-Length", 0)
        )

        body = self.rfile.read(length)

        if not body:
            return {}

        return json.loads(
            body.decode("utf-8")
        )


    def do_GET(self):

        if self.path == "/":

            self.send_json({
                "system": "TRON",
                "version": "P-01",
                "status": "online"
            })

            return


        if self.path == "/api/status":

            self.send_json(
                tron.status()
            )

            return


        self.send_json({
            "error": "Not found"
        }, 404)


    def do_POST(self):

        try:

            data = self.read_json()

        except Exception:

            self.send_json({
                "error": "Invalid JSON"
            }, 400)

            return


        # -------------------------
        # TRON SEARCH
        # -------------------------

        if self.path == "/api/search":

            query = data.get(
                "query",
                ""
            ).strip()

            if not query:

                self.send_json({
                    "error": "Search query is empty"
                }, 400)

                return

            results = tron.search(query)

            self.send_json({
                "query": query,
                "results": results
            })

            return


        # -------------------------
        # SARA AI
        # -------------------------

        if self.path == "/api/sara":

            message = data.get(
                "message",
                ""
            ).strip()

            if not message:

                self.send_json({
                    "error": "Message is empty"
                }, 400)

                return

            answer = tron.ask_sara(
                message
            )

            self.send_json({
                "message": message,
                "answer": answer
            })

            return


        self.send_json({
            "error": "Not found"
        }, 404)


def start_tron():

    server = HTTPServer(
        (HOST, PORT),
        TronHandler
    )

    print("")
    print("================================")
    print("          TRON P-01")
    print("================================")
    print("TRON Core : ONLINE")
    print("Search    : ONLINE")
    print("SARA      : ONLINE")
    print("Server    : http://127.0.0.1:8080")
    print("================================")
    print("")

    server.serve_forever()


if __name__ == "__main__":

    start_tron()
