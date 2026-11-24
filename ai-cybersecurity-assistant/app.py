"""Cybersecurity Study Assistant.
Requires an OpenAI API key in the OPENAI_API_KEY environment variable.
"""
import json
import os
import urllib.request
import urllib.error

API_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-4o-mini"

def ask_assistant(question):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Set the OPENAI_API_KEY environment variable before running.")

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a cybersecurity study assistant for a college student. "
                    "Explain concepts clearly, define technical terms, and give safe, "
                    "authorized lab examples. Do not provide instructions for attacking "
                    "real systems or bypassing authorization."
                )
            },
            {"role": "user", "content": question}
        ],
        "temperature": 0.4
    }
    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            result = json.loads(response.read().decode("utf-8"))
        return result["choices"][0]["message"]["content"].strip()
    except urllib.error.HTTPError as error:
        details = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"API request failed ({error.code}): {details}") from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"Could not connect to the AI service: {error.reason}") from error

def main():
    print("Cybersecurity Study Assistant")
    print("Ask a cybersecurity question, or type 'exit' to quit.\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in {"exit", "quit"}:
            print("Good luck with your studies!")
            break
        if not question:
            continue
        try:
            print("\nAssistant:", ask_assistant(question), "\n")
        except RuntimeError as error:
            print(f"\nError: {error}\n")

if __name__ == "__main__":
    main()
