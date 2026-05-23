# folder‑flare

**watch‑it‑notify** – a minimal Python tool that monitors a folder and pops a desktop notification for every new file.

## Features
- Zero‑configuration – just point it at a folder.
- Works on Windows, macOS and Linux (uses `plyer` for notifications).
- Uses the lightweight `watchdog` library for reliable file‑system events.
- Single‑file implementation, < 100 lines of code.

## Installation
```bash
# clone the repo (or copy the files) then install dependencies
python -m pip install -r requirements.txt
```

## Usage
```bash
python folder_flare.py /path/to/watch
```
A notification like **"New file added: example.txt"** will appear each time a file is created in the target directory.

## License
MIT – see `LICENSE`.
