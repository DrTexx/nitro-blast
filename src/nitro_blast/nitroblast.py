import subprocess
import sys
from time import sleep
from multiprocessing import Process, freeze_support
import traceback
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import json
from os import path

CONFIG_FILEPATH = "./nitroblast_config.json"
LOG_PREFIX = "[NiTROBLAST] "
RESET_TOOL_PATH_FLAG = "--reset-all-tool-paths"
DEFAULT_CONFIG = {"tool_paths": {}}


class Config:
    def __init__(self):
        if not path.exists(CONFIG_FILEPATH):
            with open(CONFIG_FILEPATH, "w") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
        with open(CONFIG_FILEPATH, "r") as f:
            _config = json.load(f)
        self.tool_paths = _config["tool_paths"]

    def get_tool_path(self, tool_name):
        if tool_name in self.tool_paths:
            tool_path = self.tool_paths[tool_name]
            if not path.exists(tool_path):
                raise RuntimeError(
                    f"Failed to find tool {tool_name} at configured path ('{tool_path}')."
                    + f"\nIf any tools have been moved, try using the `{RESET_TOOL_PATH_FLAG} option"
                )
            return
        else:
            print(f"Path to tool '{tool_name}' not configured.")
            print(f"Please select the path to '{tool_name}'")
            Tk().withdraw()
            tool_path = askopenfilename()

    def update_tool_path(self, tool_name, tool_path):
        tool_path = path.relpath(tool_path)
        with open(CONFIG_FILEPATH, "r") as f:
            cfg = json.load(f)
        cfg["tool_paths"][tool_name] = tool_path
        with open(CONFIG_FILEPATH, "w") as f:
            json.dump(cfg, f)


FIRESTARTER_DIR = "./tools/FIRESTARTER"
FIRESTARTER_BIN = f"{FIRESTARTER_DIR}/FIRESTARTER"
if sys.platform == "linux":
    PYTHON_BINARY = "python3"
elif sys.platform == "win32":
    PYTHON_BINARY = "python.exe"
else:
    PYTHON_BINARY = "python"


def log(msg, message_prefix=LOG_PREFIX):
    print(message_prefix + msg)


def firestarter_status():
    try:
        while True:
            print("🔥", end="", flush=True)
            sleep(1)
    except KeyboardInterrupt:
        log("Process aborted.")
    except Exception as err:
        raise err


def main() -> None:
    if "--help" in sys.argv:
        log(
            f"""

Options:
  --help                   display help text
  {RESET_TOOL_PATH_FLAG}   clears the stored path for all tools, will re-prompt
                           user for paths again next run
Linux only:
  --skip-firestarter       skip running FIRESTARTER
  --unsilence-firestarter  don't silence FIRESTARTER
  --quiet-firestarter      use the quiet flag (-q) when running FIRESTARTER,
                           implies --unsilence-firestarter
"""
        )
        sys.exit(0)

    cfg = Config()

    # if RESET_TOOL_PATH_FLAG in sys.argv:
    #     cfg.clear_tools_paths()

    _prime95_bin = cfg.get_tool_path("prime95")
    print(f"prime95 binary path: {_prime95_bin}")

    try:
        log("Hello from NiTROBLAST!")

        log("Running precursory Python subprocess test...")
        subprocess.run([PYTHON_BINARY, "-c", 'print("Hello, world!")'])
        log("Running precursory Python subprocess test... - OK")

        if "--skip-firestarter" in sys.argv:
            log("Skipping FIRESTARTER (--skip-firestarter used)")
        elif sys.platform == "win32":
            log("Skipping FIRESTARTER (not yet supported on Windows)")
        else:
            firestarter_commandline = [FIRESTARTER_BIN, "-t", "10"]
            capture_firestarter_output = True
            if "--unsilence-firestarter" in sys.argv:
                capture_firestarter_output = False
            if "--quiet-firestarter" in sys.argv:
                capture_firestarter_output = False
                firestarter_commandline.append("-q")

            log("Running FIRESTARTER for 10s...")

            p_firestarter_status = Process(target=firestarter_status)
            p_firestarter_status.start()
            subprocess.run(
                firestarter_commandline,
                capture_output=capture_firestarter_output,
            )
            p_firestarter_status.terminate()
            print()  # newline after terminating status process

            log("Running FIRESTARTER for 10s... - OK")

        log("Done!")
        input("\nPress [ENTER] to close...")
        sys.exit(0)
    except Exception as err:
        traceback.print_exc()
        log("^ An error occurred:")
        input("\nPress [ENTER] to close...")
        sys.exit(1)


if __name__ == "__main__":
    # NOTE: required when using pyinstaller
    # ... so that multiprocessing doesn't call
    # ... itself instead of another process when
    # ... Process().start() is used.
    freeze_support()
    try:
        main()
    except KeyboardInterrupt:
        log("Script aborted.")
    except Exception as err:
        raise err
