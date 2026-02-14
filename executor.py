import os
import subprocess
import webbrowser
import winreg


def get_real_desktop():
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
    )
    value, _ = winreg.QueryValueEx(key, "Desktop")
    return os.path.expandvars(value)


CURRENT_DIR = get_real_desktop()


BLOCKED_APPS = [
    "powershell",
    "cmd",
    "regedit",
    "taskmgr"
]

# -----------------------------
# Utility
# -----------------------------

def resolve_path(path):
    global CURRENT_DIR

    if not path:
        return CURRENT_DIR

    # If model returns fake Desktop path
    if "Desktop" in path:
        filename = os.path.basename(path)
        return os.path.join(CURRENT_DIR, filename)

    # Relative path
    if not os.path.isabs(path):
        return os.path.join(CURRENT_DIR, path)

    return path


# -----------------------------
# Action Functions
# -----------------------------

def open_app(action):
    app = action.get("app", "").lower()

    if app in BLOCKED_APPS:
        print("Blocked dangerous app:", app)
        return

    if app in ["file explorer", "explorer"]:
        subprocess.Popen("explorer")
        return

    if app in ["vscode", "vs code"]:
        vscode_path = r"C:\Users\junej\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        subprocess.Popen(vscode_path)
        return

    try:
        subprocess.Popen(app)
    except Exception as e:
        print("Failed to open app:", e)


def search_web(action):
    query = action.get("query", "")
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)


def open_url(action):
    url = action.get("url", "").strip()

    if not url:
        print("No URL provided")
        return

    # If missing protocol, add https
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    webbrowser.open(url)
    print("Opening:", url)



def create_file(action):
    file_name = action.get("path") or action.get("name")
    path = resolve_path(file_name)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        f.write("")

    print("Created file:", path)



def create_folder(action):
    folder_name = action.get("path") or action.get("name")
    path = resolve_path(folder_name)

    os.makedirs(path, exist_ok=True)
    print("Created folder:", path)



def delete_file(action):
    path = resolve_path(action.get("path"))

    if os.path.isfile(path):
        os.remove(path)
        print("Deleted file:", path)
    else:
        print("File not found:", path)


def move_file(action):
    source = resolve_path(action.get("source"))
    destination = resolve_path(action.get("destination"))

    os.rename(source, destination)
    print("Moved file from", source, "to", destination)


def list_files(action):
    path = resolve_path(action.get("path"))

    if os.path.isdir(path):
        files = os.listdir(path)
        print("Files in", path, ":", files)
    else:
        print("Directory not found:", path)


def change_directory(action):
    global CURRENT_DIR

    path = resolve_path(action.get("path"))

    if os.path.isdir(path):
        CURRENT_DIR = path
        print("Changed directory to:", CURRENT_DIR)
    else:
        print("Directory not found:", path)


def create_project(action):
    global CURRENT_DIR

    name = action.get("name")
    project_path = os.path.join(CURRENT_DIR, name)

    os.makedirs(project_path, exist_ok=True)
    os.makedirs(os.path.join(project_path, "src"), exist_ok=True)
    os.makedirs(os.path.join(project_path, "data"), exist_ok=True)

    main_file = os.path.join(project_path, "src", "main.py")

    with open(main_file, "w") as f:
        f.write("# Python Project Entry Point\n\nprint('Project started')\n")

    print("Created project at:", project_path)

    vscode_path = r"C:\Users\junej\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    subprocess.Popen([vscode_path, project_path])


def shutdown(action):
    os.system("shutdown /s /t 1")


# -----------------------------
# Action Registry
# -----------------------------

ACTIONS = {
    "open_app": open_app,
    "search_web": search_web,
    "open_url": open_url,
    "create_file": create_file,
    "create_folder": create_folder,
    "delete_file": delete_file,
    "move_file": move_file,
    "list_files": list_files,
    "change_directory": change_directory,
    "create_project": create_project,
    "shutdown": shutdown
}


# -----------------------------
# Dispatcher
# -----------------------------

def execute_action(action):
    action_type = action.get("action")

    if action_type in ACTIONS:
        try:
            ACTIONS[action_type](action)
        except Exception as e:
            print("Execution error:", e)
    else:
        print("Unknown action:", action_type)
