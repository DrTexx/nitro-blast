import subprocess

FIRESTARTER_DIR = "./tools/FIRESTARTER"
FIRESTARTER_BIN = f"{FIRESTARTER_DIR}/FIRESTARTER"


def main() -> None:
    print("[NiTROBLAST] Hello from NiTROBLAST!")
    print("[NiTROBLAST] Running precursory Python subprocess test...")
    subprocess.run(["python3", "-c", 'print("Hello, world!")'])
    print("[NiTROBLAST] Running precursory Python subprocess test... - OK")
    print("[NiTROBLAST] Running FIRESTARTER for 10s...")
    subprocess.run([FIRESTARTER_BIN, "-t", "10"])
    print("[NiTROBLAST] Running FIRESTARTER for 10s... - OK")
    print("[NiTROBLAST] Done!")


if __name__ == "__main__":
    main()
