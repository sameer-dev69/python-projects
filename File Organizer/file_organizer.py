import os
import shutil
import file_types
import logging

folder_names = file_types.FILE_TYPES # imported the dictionary present in file_types.py

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "organizer_events.log")
logging.basicConfig(filename=file_path, 
                    filemode="w", level=logging.INFO,
                    format="%(asctime)s : %(name)s : %(message)s")

def organize_files(directory):
    success = False
    files_moved = 0
    files_skipped = 0
    try:
        logging.info("Starting file organizer.")
        for e in os.scandir(directory):
            if e.is_file() and e.name != "desktop.ini":
                extension_of_file = os.path.splitext(e.name)[1].lower() 
                if folder_names.get(extension_of_file): # checks if extension has a relevant folder name
                    destination_folder = folder_names[extension_of_file]
                else:
                    destination_folder = "Others" # for files not matching any category
                try:
                    # creates the destination path and moves the file to its relevant folder according to extension
                    # example:
                    # .docx file to Documents
                    # .jpg file to Images
                    destination_path = os.path.join(directory, destination_folder)  
                    os.makedirs(destination_path, exist_ok=True)
                    shutil.move(e.path, destination_path) 
                    logging.info(f"Moved {e.name} -> {destination_folder}")
                    files_moved +=1
                except PermissionError: # incase a file was not permitted to be moved
                    logging.error("File could not be moved, either it is open, or is protected.")
                    logging.info(f"Skipped {e.name}")
                    files_skipped +=1
                except:
                    logging.error("File couldn't be moved due to unknown error.")
                    logging.info(f"Skipped {e.name}")
                    files_skipped +=1
        success = True
        logging.info(f"Program ended successfully!\nMoved {files_moved} files, skipped {files_skipped} files.")
    except FileNotFoundError:
        logging.error("Folder path could not be found!")
        success=False
    except:
        logging.error("Session ended due to unknown error, couldnt move all files successfully.")
        success=False

    if (success):
        print("Action Completed")
    else:
        print("Action terminated with error.")

if __name__ == "__main__":
    n = input("Enter the path: ")
    organize_files(n)
