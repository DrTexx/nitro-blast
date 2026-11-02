import subprocess

LOG_PREFIX = "[NiTROBLAST] "
FIRESTARTER_DIR = "./tools/FIRESTARTER"
FIRESTARTER_BIN = f"{FIRESTARTER_DIR}/FIRESTARTER"


def log(msg, message_prefix=LOG_PREFIX):
    print(message_prefix + msg)


def main() -> None:
    log("Hello from NiTROBLAST!")
    log("Running precursory Python subprocess test...")
    subprocess.run(["python3", "-c", 'print("Hello, world!")'])
    log("Running precursory Python subprocess test... - OK")
    log("Running FIRESTARTER for 10s...")
    subprocess.run([FIRESTARTER_BIN, "-t", "10"])
    log("Running FIRESTARTER for 10s... - OK")
    log("Done!")


if __name__ == "__main__":
    main()
