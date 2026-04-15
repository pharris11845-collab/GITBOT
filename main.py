import os

from openai import OpenAI


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing OPENAI_API_KEY environment variable. "
            "Set it before running this script."
        )

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Hello, ChatGPT! Please introduce yourself."
    )

    # The response shape may include multiple output segments.
    output = response.output
    if output and len(output) > 0:
        text = output[0].content[0].text
        print("ChatGPT response:\n", text)
    else:
        print("No response content returned.")


if __name__ == "__main__":
    main()
