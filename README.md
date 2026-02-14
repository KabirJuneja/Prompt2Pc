# Prompt2Pc

Prompt2Pc is a Telegram-controlled Windows automation tool that executes local system actions based on natural language commands.

It uses a locally running AI model (via Ollama) to convert user instructions into structured commands, which are then executed on the machine.

This project currently runs entirely offline for AI processing.

---

## Current Features

* Open installed applications:

  * Google Chrome
  * Microsoft Edge
  * Visual Studio Code
  * Notepad
* Perform web searches through the default browser
* Parse commands locally using Ollama (Phi-3 model)
* Restrict usage to an authorized Telegram user

The system does not require cloud AI services at this stage.

---

## How It Works

1. A command is sent through Telegram.
2. The AI model (Phi-3 via Ollama) converts the request into structured JSON.
3. The executor reads the JSON and performs the action locally on Windows.

Only predefined applications are allowed for execution to reduce risk.

---

## Requirements

* Windows
* Python 3.10+
* Ollama installed
* Telegram Bot Token
* Authorized Telegram User ID

---

## Ollama Setup

### 1. Install Ollama

Download and install from:

[https://ollama.com/download](https://ollama.com/download)

After installation, verify:

```
ollama --version
```

### 2. Download the Model

```
ollama pull phi3
```

Confirm:

```
ollama list
```

You should see `phi3` in the list.

---

## Project Setup

### 1. Clone the Repository

```
git clone https://github.com/KabirJuneja/Prompt2Pc.git
cd Prompt2Pc
```

### 2. Create a Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

If you have a requirements file:

```
pip install -r requirements.txt
```

Or install manually if needed.

### 4. Create a `.env` File

Create a file named `.env` in the project root:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
AUTHORIZED_USER_ID=your_telegram_user_id_here
```

Do not commit this file to GitHub.

---

## Running the Bot

```
python main.py
```

Make sure Ollama is running before starting the bot.

---

## Security Notes

This project executes commands on the local machine.
It should only be used on systems you own or control.

Administrative privileges are not enabled by default.
