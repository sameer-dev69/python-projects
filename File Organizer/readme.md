# File Organizer

This app organizes files in a given folder according to their filetypes.
Recognizes extension of the files and sends them to relevant folders

# Files:
file_organizer.py: main file with program logic written.
file_types: utility file that has a dictionary pointing filetypes to their relevant folder names
organizer_events.log: saves a log of the actions performed by file organizer everytime it runs

# Features
* Asks the user to enter folder path.
* Makes a list of files inside the path, and checks their extension
* Matches their extension to the respective folder name as given in file_types.py
* moves the file to the respective folder

## Sample Output
(gets saved in logs)
2026-03-15 11:02:19,951 : root : Starting file organizer.
2026-03-15 11:02:19,954 : root : Moved sample1.docx -> Documents
2026-03-15 11:02:19,960 : root : Moved sample2.PNG -> Images
Moved 2 files, skipped 0 files.