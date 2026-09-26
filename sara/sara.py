"""
SARA AI Core
TRON P-01
"""

SARA_NAME = "SARA"
VERSION = "P-01"


def process(message: str) -> str:
    """
    Initial SARA processing layer.

    Later this layer will connect to TRON's
    own AI model and reasoning system.
    """

    message = message.strip()

    if not message:
        return "Please give me something to process."

    text = message.lower()

    if text in ["hello", "hi", "hey"]:
        return "Hello. SARA is online."

    if "who are you" in text:
        return "I am SARA, the AI system inside TRON."

    if "tron" in text:
        return "TRON core is currently running in P-01 development mode."

    return (
        "SARA received your message: "
        + message
        + "\n\n"
        "Advanced reasoning will be connected to the SARA AI engine "
        "in a later build."
    )


def status():
    return {
        "name": SARA_NAME,
        "version": VERSION,
        "status": "online",
        "mode": "development"
    }


if __name__ == "__main__":

    print("SARA AI Core")
    print("Version:", VERSION)
    print("Status: ONLINE")
    print()
    print("Type 'exit' to stop.")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("SARA: Goodbye.")
            break

        response = process(user_input)

        print("SARA:", response)
