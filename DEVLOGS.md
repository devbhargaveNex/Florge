Based on what you've completed (setup + first three milestones) and your usual devlog style:

---

# DevLog 1

**Date:** 17/7/26
**Work Time:** ~30 min

## Goals

* Create project repository.
* Set up virtual environment.
* Create initial project structure.

## Completed

* Initialized Git repository.
* Created and activated virtual environment.
* Created main project files and folders.
* Made initial Git commit.

## What I Learned

* Project setup is much faster after completing my first project.
* Having a standard folder structure saves time before coding begins.

## Problems

* None.

## Next Session

* Plan the file organizer architecture.
* Start scanning directories and listing files.

---

# DevLog 2

**Date:** 18/7/26
**Work Time:** ~30 min

## Goals

* Design the program flow.
* Begin implementing directory scanning.

## Completed

* Planned the overall workflow of the application.
* Implemented basic directory scanning.
* Successfully listed files from a user-specified directory.
* Verified that paths are being read correctly.

## What I Learned

* Became more comfortable using `pathlib`.
* Better understanding of how files and directories are represented as `Path` objects.

## Problems

* Needed to decide how hidden files and folders should be handled.
* Started thinking about how to categorize files efficiently.

## Next Session

* Detect file extensions.
* Create mapping between extensions and destination folders.
* Begin organizing files by type.

---

# DevLog 3

**Date:** 18/7/26
**Current Status:** Session complete

## Progress Summary

Current progress:

* ✅ Project setup completed.
* ✅ Repository initialized.
* ✅ Virtual environment configured.
* ✅ Basic project structure created.
* ✅ Directory scanning working.
* ✅ File listing implemented.
* ⏳ Next milestone: Categorize and move files safely.

## Time Spent

* Session 1: ~30 min
* Session 2: ~30 min

**Total Focused Development Time:** ~1 hour

## Notes

Compared to the Expense Tracker, I spent less time figuring out project setup and more time planning the architecture before writing code. The experience from the previous project made the initial development smoother and more structured.

---

# DevLog 4

**Date:** 27/9/26
**Work Time:** Short session

## Goals

* Continue the refactor to support the new dictionary-of-lists design.
* Update `operations.py` to work with multiple files per extension.

## Completed

* Refactored `operations.py` for the new dictionary design.
* Updated the file count so it counts the actual files stored inside the lists rather than the number of dictionary keys.
* Added an exit option to the operations menu.
* Added `.gitignore` entries for temporary files and Python cache files.
* Tested the refactor and merged the PR into `main`.

## What I Learned

* A dictionary can map one key to a list when one category can contain multiple values.
* Changing a data structure means each part of the workflow that consumes it needs to be reconsidered.
* Refactoring file-by-file makes it easier to follow how a data-model change propagates through the program.

## Problems

* The previous dictionary design represented one file per extension, so the file count was based on dictionary keys rather than the actual number of files.
* `operations.py` needed to be adapted to the new dictionary-of-lists structure.

## Next Session

* Continue the refactor through the next file in the workflow.
* Test each component against the new dictionary design as it is reached.
