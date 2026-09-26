"""
TRON Core
P-01
Connects Search + SARA
"""

from search.search_engine import create_engine
from sara.sara import process as sara_process


class TronCore:

    def __init__(self):
        self.search_engine = create_engine()

    def search(self, query):
        return self.search_engine.search(query)

    def ask_sara(self, message):
        return sara_process(message)

    def status(self):
        return {
            "tron": "online",
            "search": "online",
            "sara": "online",
            "version": "P-01"
        }


if __name__ == "__main__":

    tron = TronCore()

    print("================================")
    print("          TRON P-01")
    print("================================")
    print("TRON:", tron.status()["tron"])
    print("Search:", tron.status()["search"])
    print("SARA:", tron.status()["sara"])
    print("================================")

    while True:

        command = input("\nTRON > ").strip()

        if command.lower() == "exit":
            print("TRON shutting down...")
            break

        if command.lower().startswith("search "):

            query = command[7:]
            results = tron.search(query)

            if not results:
                print("No results found.")
                continue

            for result in results:
                print("\n" + result["title"])
                print(result["url"])
                print(result["content"])

        elif command.lower().startswith("sara "):

            message = command[5:]
            answer = tron.ask_sara(message)

            print("\nSARA:", answer)

        elif command.lower() == "status":

            print(tron.status())

        else:

            print(
                "Commands:\n"
                "  search <query>\n"
                "  sara <message>\n"
                "  status\n"
                "  exit"
          )
