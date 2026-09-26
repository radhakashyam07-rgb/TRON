"""
TRON Search Engine
TRON P-01
"""

ENGINE_NAME = "TRON Search"
VERSION = "P-01"


class SearchEngine:

    def __init__(self):
        self.index = {}

    def add_document(self, url, title, content):
        self.index[url] = {
            "title": title,
            "content": content
        }

    def search(self, query):

        query = query.lower().strip()
        results = []

        if not query:
            return results

        for url, document in self.index.items():

            text = (
                document["title"] + " " +
                document["content"]
            ).lower()

            if query in text:

                results.append({
                    "url": url,
                    "title": document["title"],
                    "content": document["content"]
                })

        return results


def create_engine():

    engine = SearchEngine()

    # Temporary development documents.
    # Later these will come from TRON's own index.

    engine.add_document(
        "tron://welcome",
        "Welcome to TRON",
        "TRON is an independent search engine and AI platform."
    )

    engine.add_document(
        "tron://sara",
        "SARA AI",
        "SARA is the AI system being developed inside TRON."
    )

    return engine


if __name__ == "__main__":

    engine = create_engine()

    print("TRON Search Engine")
    print("Version:", VERSION)
    print("Status: ONLINE")
    print()

    while True:

        query = input("Search: ")

        if query.lower() == "exit":
            break

        results = engine.search(query)

        if not results:
            print("No results found.")
            continue

        for result in results:

            print("\n" + result["title"])
            print(result["url"])
            print(result["content"])
