# Organizer

A simple desktop app for sorting image and document files in the folder containing `Organizer.py`.

## What it does

Click **Organize Desk** to create `Images` and `Documents` folders next to the script and move supported files into them. Files with other extensions are left where they are. If a file with the same name already exists in the destination folder, the file is skipped to avoid overwriting it. The app only checks files directly in the script's folder; it does not scan subfolders.

> **Important:** This app moves files. Back up your files or try it on a copy of the folder first.

## Requirements

- Python 3.10 or newer
- Flet 1.0.4

## Installation and usage

Install the dependency from the project folder:

```powershell
python -m pip install -r requirements.txt
```

Copy `Organizer.py` into the folder you want to organize, then run it from that folder:

```powershell
python Organizer.py
```

Do not run the script from the project folder unless you intend to sort that folder: it moves supported files, including documents such as this README.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
