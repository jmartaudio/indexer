#**Disk Indexer**

A simple tool for creating an sqlite database of all of the files and folders on a disk.

I have a lot of external disks all over the place. I forget what files are on them.
scan the drive with this tool and create a searchable database of all of the files on the disk
Omce you find the file you will know what disk your file is on

## Usage
python3 main.py path-to-disk
example: python3 main.py /Volumes/external_disk

### Current Features - or lack of
- to browse use and sql browser I'm using [sqlitebrowser] (https://sqlitebrowser.org/)
- files link to folders
- folders link to drives
- disk usage and size metadata
- folder show number of items
- files show name, full path, , size, date created, date modifies, parent folderID
- plan to add more metadata at some point
