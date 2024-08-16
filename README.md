# IssueRelay

Folder Breakdown
/src: Contains the main application code.

/src/gui: For Tkinter UI components and layouts.
/src/gui/main_window.py: The main application window and primary Tkinter setup.
/src/gui/ticket_window.py: If you have separate windows or dialogs for ticket management.
/src/services: Handles the logic for interacting with APIs and Excel files.
/src/services/api_service.py: Functions to upload and download ticket records.
/src/services/excel_service.py: Functions to read from and write to Excel files.
/src/controllers: Contains logic to coordinate between the UI and the backend services.
/src/controllers/ticket_controller.py: Manages ticket-related operations, including invoking API and Excel services based on user actions.
/assets: Stores static files like images, icons, and other resources used in the Tkinter UI.

/assets/images: For image files (icons, logos, etc.).
/assets/styles: For any style-related files (if using custom styles or themes).
/config: Configuration files and settings.

config.json: Store settings such as file paths, default values, or API configurations.
/data: Temporary storage for data files, if needed.

/data/exports: For exported Excel files or other data dumps.
/data/imports: For files to be processed or imported.
/utils: Utility functions and helper scripts.

/utils/file_utils.py: General file handling functions.
/utils/gui_utils.py: Helper functions for managing Tkinter widgets or layouts.
/tests: Contains unit and integration tests.

/tests/unit: For unit tests of individual components or functions.
/tests/integration: For tests that involve multiple components or interactions.

# My App

## Setup

1. Install Pipenv if you haven’t already:

   ```bash
   pip install pipenv
pipenv install
pipenv run python src/gui/main_window.py
pipenv run pyinstaller --onefile src/gui/main_window.py

### Summary

- **`Pipenv` does not handle entry points directly**; you manage scripts and entry points using Python scripts and command-line tools.
- **Use `PyInstaller`** for packaging and creating executables.
- **Document your process** in `README.md` for clarity.

By setting up scripts and using `PyInstaller`, you can effectively manage and package your Tkinter application while using `Pipenv` for dependency management.
