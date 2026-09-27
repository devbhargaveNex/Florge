# Florge

Florge is a Python command-line file organization tool. It scans a source directory, identifies files by extension, lets the user review and remove items from the operation, supports a dry run, and can move the remaining files into categorized destination folders.

## Current status

Florge is currently under development. The current version is a working development build; V1 is being prepared.

## Current workflow

1. Scan the source directory.
2. Detect file extensions and folders.
3. Show the files found to the user.
4. Allow multiple files to be removed from the operation.
5. Preview the planned organization with dry run.
6. Move the remaining files into their corresponding destination categories.

Hidden files are ignored. Folders are kept separate from files and are moved to the `Folders` destination rather than being processed as regular files.

## Current categories

Florge currently recognizes extension groups for:

- Images
- Videos
- Audio
- Documents
- Applications
- Temporary files
- Other files
- Folders

The extension groups are defined in `app/utls.py`.

## Project structure

```text
app/
├── Main.py
├── scan.py
├── detect.py
├── operations.py
├── move.py
├── dry.py
└── utls.py
```

The modules have separate responsibilities for scanning, detection, user operations, dry-run handling, and moving files.

## Planned V1 work

- CLI source/root directory argument
- Debugging and cleanup
- Logging
- More complete testing
- Final documentation

## Development

Florge is being developed as a practical tool rather than only as a learning exercise. The project is also being used to develop experience with modular Python programs, filesystem operations, debugging, refactoring, and CLI design.
