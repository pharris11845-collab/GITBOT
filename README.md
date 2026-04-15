# GITBOT

Forex Trading Bot

This repository includes a starter script to connect to OpenAI ChatGPT via the official Python API.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Add your OpenAI API key:

   ```bash
   cp .env.example .env
   # Then edit .env and replace your_api_key_here
   ```

   or set it directly:

   ```bash
   export OPENAI_API_KEY="your_api_key"
   ```

## Usage

Run the starter script:

```bash
python main.py
```

## Files

- `main.py`: example OpenAI ChatGPT integration script
- `requirements.txt`: Python dependency for the OpenAI client
- `.env.example`: environment variable example
