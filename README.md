# nitro-blast
Tool for unattended benchmarking

## Usage

- **Windows** - Double-click `run-on-windows.bat`
- **Linux** - Run `./NiTROBLAST`

**NOTE:** if you're stress-testing a new build, it's highly recommended to install drivers first, otherwise most benchmarks will fail to launch. Some benchmarks like Prime95 also have an initial configuration question or two when they're first launched; if you're setting up NiTROBLAST on an external USB drive, it's recommended to launch each benchmark you'll use and run through any first-time questions first so they don't interrupt unattended benchmarking.

## Development

### Prerequisites

You must have the following installed on your system to build NiTROBLAST.

- [Git](https://git-scm.com/install/)
- [UV](https://docs.astral.sh/uv/getting-started/installation/)

### Environment Configuration

```bash
# create and sync uv venv
uv sync

# update and install pre-commit hooks
uv run pre-commit autoupdate # updates hooks to latest version
uv run pre-commit install --hook-type pre-commit --hook-type pre-push # installs git hooks
uv run pre-commit run --all-files # runs hooks over all current local files
```

### Building

#### Windows

Download embedded version of Python interpreter ([64-bit](https://www.python.org/ftp/python/3.14.10/python-3.14.10-embed-amd64.zip) / [32-bit](https://www.python.org/ftp/python/3.14.10/python-3.14.10-embed-win32.zip) / [ARM](https://www.python.org/ftp/python/3.14.10/python-3.14.10-embed-arm64.zip)) for platforms that you want to support and place them into `./put-python-interpreters-here`

From Git Bash, run

```bash
./build-windows.sh
```

#### Linux

```bash
./build-linux.sh
```
