# Prompt2Pc

Prompt2Pc is a Telegram-controlled Windows automation tool that executes local system actions based on natural language commands.

It uses a locally running AI model (via Ollama) to convert user instructions into structured JSON, which is then executed safely on the machine.

The system runs locally and does not require cloud AI services.

---

## Current Capabilities

### Application Control

* Open Chrome, Edge, VS Code, Notepad
* Open any app available in system PATH (except blocked system tools)

### Browser Automation

* Open any URL
* Automatically adds `https://` if missing
* Supports natural inputs like `Open youtube`

### File & Folder Management

* Create folders
* Create files
* Delete files
* Move files
* List directory contents

### Working Directory Memory

* Maintains a current working directory
* Defaults to the real Windows Desktop
* Supports relative paths (no need to always type full path)
* Allows changing directory during session

### Desktop Auto-Detection

* Detects the actual Windows Desktop location dynamically
* Handles OneDrive Desktop redirection correctly
* Does not rely on hardcoded paths

### Project Scaffolding

* Create basic Python project structure
* Auto-generates `src/` and `data/` folders
* Opens project in VS Code automatically

### Security Controls

* Blocks dangerous applications (PowerShell, CMD, Registry Editor, etc.)
* Restricts execution to authorized Telegram user
* Sanitizes AI-generated paths before execution

---

## How It Works

1. A command is sent via Telegram.
2. Ollama (Phi-3 model) converts the command into strict JSON.
3. The JSON is parsed into a Python dictionary.
4. The executor maps the action to a safe function.
5. Windows performs the requested action.

No JSON files are created on disk unless explicitly instructed.
All command parsing happens in memory.

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

Download from:

[https://ollama.com/download](https://ollama.com/download)

Verify installation:

```
ollama --version
```

### 2. Pull the Model

```
ollama pull phi3
```

Confirm:

```
ollama list
```

---

## Full Setup Guide

### 1. Install Ollama

Download and install from:

[https://ollama.com/download](https://ollama.com/download)

Verify installation:

```
ollama --version
```

Pull the required model:

```
ollama pull phi3
```

Confirm:

```
ollama list
```

---

### 2. Create a Telegram Bot

1. Open Telegram
2. Search for **@BotFather**
3. Run `/start`
4. Run `/newbot`
5. Follow the instructions
6. Copy the generated Bot Token

It will look like:

```
1234567890:AAExampleTokenHere
```

---

### 3. Get Your Telegram User ID

1. Search for **@userinfobot**
2. Run `/start`
3. Copy your numeric user ID

Example:

```
123456789
```

---

### 4. Clone the Repository

```
git clone https://github.com/KabirJuneja/Prompt2Pc.git
cd Prompt2Pc
```

---

### 5. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 6. Install Dependencies

If a requirements file exists:

```
pip install -r requirements.txt
```

Or install manually:

```
pip install python-telegram-bot ollama python-dotenv
```

---

### 7. Create `.env` File

Create a file named `.env` in the project root:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
AUTHORIZED_USER_ID=your_user_id_here
```

Do not commit this file to GitHub.

---

### 8. Run the Bot

Ensure Ollama is running, then:

```
python main.py
```

You should see:

```
Bot is running...
```

Now send commands to your Telegram bot.

---

## Example Commands

```
Create folder AI
Change directory to AI
Create file main.py
Open youtube
List files
```

---

## Current Limitations

* Working directory resets when bot restarts
* No persistent state storage yet
* No confirmation system for destructive actions (planned)
* No admin-level control

---

## Security Notice

This project executes commands on your local machine.
Use only on systems you control.
Do not expose the bot publicly without additional safeguards.

---

Project Status: Active Development
