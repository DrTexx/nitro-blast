import subprocess
import sys

LOG_PREFIX = "[NiTROBLAST] "
FIRESTARTER_DIR = "./tools/FIRESTARTER"
FIRESTARTER_BIN = f"{FIRESTARTER_DIR}/FIRESTARTER"


def log(msg, message_prefix=LOG_PREFIX):
    print(message_prefix + msg)


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
        subprocess.run(firestarter_commandline)
        log("Running FIRESTARTER for 10s... - OK")

    log("Done!")
    sys.exit(0)


if __name__ == "__main__":
    main()
