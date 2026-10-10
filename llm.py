
import os
from google import genai


def generate_response(prompt, temperature=0.3, max_tokens=500):
    api_key = os.environ.get("API_Key")

    if not api_key:
        raise RuntimeError(
            "Gemini API key is missing. "
            "Set $env:API_Key in the VS Code terminal."
        )

    try:
        client = genai.Client(api_key=api_key)

        response = client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt,
        )

        if response.output_text:
            return response.output_text

        return "The model returned an empty response."

    except Exception as e:
        return f"Gemini API error: {e}"
