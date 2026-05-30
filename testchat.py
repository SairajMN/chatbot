import requests

response = requests.post(
  "https://api.inceptionlabs.ai/v1/chat/completions",
  headers={
    "Authorization": "Bearer your_api_key",
    "Content-Type": "application/json"
  },
  json={
    "model": "mercury-2",
    "messages": [
      {"role": "system", "content": "You are a pirate."},
      {"role": "user", "content": "Tell me a joke"}
    ]
  }
)

print(response.json()["choices"][0]["message"]["content"],end="")
