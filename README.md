# nitro-blast
Tool for unattended benchmarking

## Usage

- **Windows** - Double-click `run-on-windows.bat`
- **Linux** - Run `./NiTROBLAST`

## Building

### Prerequisites

You must have the following installed on your system to build NiTROBLAST.

- [Git](https://git-scm.com/install/)
- [UV](https://docs.astral.sh/uv/getting-started/installation/)

### Windows

Download embedded version of Python interpreter ([64-bit](https://www.python.org/ftp/python/3.14.10/python-3.14.10-embed-amd64.zip) / [32-bit](https://www.python.org/ftp/python/3.14.10/python-3.14.10-embed-win32.zip) / [ARM](https://www.python.org/ftp/python/3.14.10/python-3.14.10-embed-arm64.zip)) for platforms that you want to support and place them into `./put-python-interpreters-here`

From Git Bash, run

```bash
./build-windows.sh
```

### Linux

```bash
./build-linux.sh
```
