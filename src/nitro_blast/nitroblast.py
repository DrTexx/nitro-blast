import subprocess
import sys
from time import sleep
from multiprocessing import Process, freeze_support

LOG_PREFIX = "[NiTROBLAST] "
FIRESTARTER_DIR = "./tools/FIRESTARTER"
FIRESTARTER_BIN = f"{FIRESTARTER_DIR}/FIRESTARTER"
if sys.platform == "linux":
    PYTHON_BINARY = "python3"
elif sys.platform == "win32":
    PYTHON_BINARY = ".\\_internal\\python-interpreters\\python314_64bit\\python.exe"
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
            """

Options:
  --help                   display help text
  
Linux only:
  --skip-firestarter       skip running FIRESTARTER
  --unsilence-firestarter  don't silence FIRESTARTER
  --quiet-firestarter      use the quiet flag (-q) when running FIRESTARTER,
                           implies --unsilence-firestarter
"""
        )
        sys.exit(0)

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
    sys.exit(0)


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
