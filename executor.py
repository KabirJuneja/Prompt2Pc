import os
import subprocess
import webbrowser

# Whitelisted applications
ALLOWED_APPS = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
    "vscode": "C:\\Users\\junej\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "notepad": "C:\\Windows\\System32\\notepad.exe"
}

# Base safe directory (your user folder)
SAFE_BASE = os.path.expanduser("~")


def is_safe_path(path):
    return os.path.abspath(path).startswith(SAFE_BASE)


def execute_action(action):
    action_type = action.get("action")

    try:

        # -----------------------------
        # Open App
        # -----------------------------
        if action_type == "open_app":
            app = action.get("app")

            if app in ALLOWED_APPS:
                subprocess.Popen(ALLOWED_APPS[app])
            else:
                print("App not allowed:", app)

        # -----------------------------
        # Search Web
        # -----------------------------
        elif action_type == "search_web":
            query = action.get("query")
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)

        # -----------------------------
        # Open Specific URL
        # -----------------------------
        elif action_type == "open_url":
            url = action.get("url")
            webbrowser.open(url)

        # -----------------------------
        # Create File on Desktop
        # -----------------------------
        elif action_type == "create_file":
            filename = action.get("filename")

            desktop = os.path.join(SAFE_BASE, "Desktop")
            file_path = os.path.join(desktop, filename)

            if is_safe_path(file_path):
                with open(file_path, "w") as f:
                    f.write("")
            else:
                print("Unsafe file path blocked.")

        # -----------------------------
        # Move File (within safe base only)
        # -----------------------------
        elif action_type == "move_file":
            source = action.get("source")
            destination = action.get("destination")

            if is_safe_path(source) and is_safe_path(destination):
                os.rename(source, destination)
            else:
                print("Unsafe move blocked.")

        # -----------------------------
        # Shutdown (no admin required)
        # -----------------------------
        elif action_type == "shutdown":
            os.system("shutdown /s /t 1")

        else:
            print("Unknown action:", action_type)

    except Exception as e:
        print("Execution error:", e)
