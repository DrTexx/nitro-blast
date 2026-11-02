import subprocess
import sys
from time import sleep
from multiprocessing import Process, freeze_support

LOG_PREFIX = "[NiTROBLAST] "
FIRESTARTER_DIR = "./tools/FIRESTARTER"
FIRESTARTER_BIN = f"{FIRESTARTER_DIR}/FIRESTARTER"


def log(msg, message_prefix=LOG_PREFIX):
    print(message_prefix + msg)


def firestarter_status():
    while True:
        print("🔥", end="", flush=True)
        sleep(1)


def main() -> None:
    if "--help" in sys.argv:
        log(
            """

Options:
  --help                 display help text
  --skip-firestarter     skip running FIRESTARTER
  --unquiet-firestarter  don't use the quiet flag (-q) when running FIRESTARTER
"""
        )
        sys.exit(0)

    log("Hello from NiTROBLAST!")

    log("Running precursory Python subprocess test...")
    subprocess.run(["python3", "-c", 'print("Hello, world!")'])
    log("Running precursory Python subprocess test... - OK")

    if "--skip-firestarter" in sys.argv:
        log("Skipping FIRESTARTER (--skip-firestarter used)")
    else:
        firestarter_commandline = [FIRESTARTER_BIN, "-t", "10"]
        if not "--unquiet-firestarter" in sys.argv:
            firestarter_commandline.append("-q")

        log("Running FIRESTARTER for 10s...")

        p_firestarter_status = Process(target=firestarter_status)
        p_firestarter_status.start()
        subprocess.run(firestarter_commandline)
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
    main()
