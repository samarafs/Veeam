import os, shutil
import csv

    
def fixPath(srcPath, cpyPath, retType):
    fixedPath = ""
    lsChar = ""
    for char in srcPath:
        if(char == "\\" and lsChar != "\\"):
            fixedPath += "\\\\"
        elif(char != "\\"):
            fixedPath += char
        lsChar = char




    try:   
        if(fixedPath[-1] != "\\" and fixedPath[-2] != "\\"):
            fixedPath += "\\\\"
    except(IndexError):
        print("\ninvalid path")
    
    if(retType.upper() == "S"):
        return fixedPath
    elif(retType.upper() == "C"):
        folder = fixedPath.split("\\\\")[-2]
        fixedPath = fixPath(cpyPath, "", "s") + folder + "\\\\"
        return fixedPath


while True:
    sourcePath = fixPath(input("insert the full path of the source folder: "), "", "s")
    userCopyPath = input("insert the full path of the copy folder: ")
    copyPath = fixPath( sourcePath, userCopyPath, "c")
    
    print(sourcePath)
    print(copyPath)
    
    
    

    
    
    count = 0
    while True:
        count += 1

        if count % 35000000 == 0:
            
            os.chdir(sourcePath)
            try:
                shutil.copytree(sourcePath, copyPath)
            except(FileExistsError):
                shutil.rmtree(copyPath)
                shutil.copytree(sourcePath, copyPath)