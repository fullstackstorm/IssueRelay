import os
import glob
import sys

class ExcelFileFinder:
    @staticmethod
    def find_excel_file(directory):
        """Search for Excel files with .xlsm extension in the given directory.
        Prioritizes files starting with '1'."""
        # Search for Excel files starting with '1'
        priority_files = glob.glob(os.path.join(directory, '1*.xls*'))
        if priority_files:
            # Return the first priority file found
            return priority_files[0]

        # If no priority files, return the first general Excel file found
        all_files = glob.glob(os.path.join(directory, '*.xls*'))
        return all_files[0] if all_files else None

    @staticmethod
    def get_base_directory():
        """Determine the base directory two levels up from the script or executable."""
        if getattr(sys, 'frozen', False):
            # If running as a frozen executable (e.g., via PyInstaller)
            return os.path.abspath(os.path.join(os.path.dirname(sys.executable), '../../'))
        else:
            # If running as a script
            return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))