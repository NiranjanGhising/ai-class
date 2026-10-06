import os

from mistralai.client import Mistral


MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

if not MISTRAL_API_KEY:
    raise RuntimeError("Set MISTRAL_API_KEY before running this script.")

client = Mistral(api_key=MISTRAL_API_KEY)

try:
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[{"role": "user", "content": "Test API key"}]
    )
    print("API Key Valid:", response.choices[0].message.content)
except Exception as e:
    print("API Key Invalid:", e)   