# src/__main__.py
import os
import sys
import time
from utils.excel_file_finder import ExcelFileFinder

# Checks if the script is being run directly or if it is being imported.
if __name__ == "__main__":
    start_time = time.time()
    # Executes the UI
    #main()

    # Retrieve the excel file in the folder.
    base_dir = ExcelFileFinder.get_base_directory()
    excel_file = ExcelFileFinder.find_excel_file(base_dir)
    print(excel_file)

    oven = sim_oven(excel_file)
    work_book = xlwings.Book(excel_file)
    work_book.macro('Clear_Sims')()
    for process in oven.process_folder_dictionary.keys():
        oven.cook(process)
        with xlwings.App(visible = False):   
            work_sheet = work_book.sheets(process)
            work_sheet.range('A2').options(header = False, index = False).value = oven.cooked_sim_list
    # oven.cook('FIF')
    # with xlwings.App(visible=False):
    #     work_sheet = work_book.sheets('FIF')
    #     work_sheet.range('A2').options(header = False, index = False).value = oven.cooked_sim_list
    # oven.labels.save()
    work_book.macro('Generate_Email_Report')()
    work_book.save()
    #work_book.close()

    process_time = time.time() - start_time
    process_minutes = process_time // 60
    process_seconds = process_time - process_minutes * 60
    print(f'Process Time: {process_minutes} minutes, {process_seconds} seconds.')
