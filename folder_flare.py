#!/usr/bin/env python3
"""folder_flare – tiny directory watcher that sends desktop notifications.

Usage:
    python folder_flare.py /path/to/watch
"""
import sys
import os
from pathlib import Path

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    sys.exit("Missing dependency: watchdog. Install with 'pip install watchdog'.")

try:
    from plyer import notification
except ImportError:
    sys.exit("Missing dependency: plyer. Install with 'pip install plyer'.")

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_name = Path(event.src_path).name
        notification.notify(
            title="folder‑flare",
            message=f"New file added: {file_name}",
            timeout=5,
        )
        print(f"[+] {file_name} detected")

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python folder_flare.py <directory_to_watch>")
    watch_path = Path(sys.argv[1]).expanduser().resolve()
    if not watch_path.is_dir():
        sys.exit(f"Error: '{watch_path}' is not a directory.")

    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, str(watch_path), recursive=False)
    observer.start()
    print(f"[✓] Watching '{watch_path}' – press Ctrl+C to stop")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
