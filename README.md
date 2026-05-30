# InceptionLLM Chatbot

This project demonstrates how to interact with the InceptionLLM API (specifically the `mercury-2` model) to build a command-line chatbot.

## Features

- **Conversational Interface**: Maintains context throughout a conversation.
- **System Prompts**: Allows you to define the personality/role of the chatbot.
- **API Integration**: Uses the `requests` library to communicate with the InceptionLLM API.
- **Environment Variables**: Securely manages API keys using `.env` files.

## Getting Started

### Prerequisites

- Python 3.6+
- An API key from InceptionLabs. You can get one from the [InceptionLabs Dashboard](https://dashboard.inceptionlabs.ai/).

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd chatbot
   ```

2. Install dependencies:
   ```bash
   pip install requests python-dotenv
   ```

3. Set up the environment:
   - Create a file named `.env` in the `chatbot` directory.
   - Add your API key to it in the following format:
     ```env
     INCEPTION_API_KEY=your_api_key_here
     ```

## Usage

### Running the Chatbot

To start an interactive chat session, run:

```bash
python3 mychat.py
```

Type your messages and press Enter. The chatbot will respond based on its system prompt.

### Example: Angry Rapper

The default `mychat.py` uses a system prompt that configures the AI to act as an angry rapper.

**Sample Interaction:**
```
You: Hey, how are you?
[AI Response as an angry rapper]
```

### API Reference (Quick Look)

We use the `POST /v1/chat/completions` endpoint.

**Request:**
```json
{
    "model": "mercury-2",
    "messages": [
        {"role": "system", "content": "..."},
        {"role": "user", "content": "..."}
    ]
}
```

**Response:**
```json
{
    "choices": [
        {
            "message": {
                "content": "..."
            }
        }
    ]
}
```

## Files Explained

- `mychat.py`: The main application logic. It handles the loop for continuous conversation, manages the message history, and makes API calls.
- `chat.py`: A simple script to test a single API call without the conversational loop.
- `testchat.py`: Demonstrates a more complex interaction with a specific system persona (pirate).
