from shutil import copyfile
from pathlib import Path
from typing import List

NewFileNameList: List[str] = [ 
    'C:\\Lorem\\ipsum\\dolor\\sit\\consectetur.jpg',
    'C:\\Lorem\\ipsum\\dolor\\sit\\adipiscing.jpg',
    'C:\\Lorem\\ipsum\\dolor\\amet\\elit.jpg',
    'C:\\Lorem\\ipsum\\dolor\\amet\\Duis.jpg'
    # ... so many files
    ]

sampleImage: str = "C:\\Image\\Sample.JPG"

newFile: str
for newFile in NewFileNameList:
    
    # get folder structure from file list
    newdirectory: Path = Path(newFile[:newFile.rfind('\\')])

    # make folder if not exist
    isDirectoryExist: bool = newdirectory.exists()
    if isDirectoryExist == False:
        newdirectory.mkdir(parents=True, exist_ok=True)

    # make file if not exist
    if  Path(newFile).is_file():
        print(f"already exsts: {newFile}")
    else:
        copyfile(sampleImage, newFile)
        print(f"file created: {newFile}")

    print("")