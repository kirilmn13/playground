import os
import shutil
import sys
import hashlib


def crearcarpeta(directorio, tipoarchivos):
    for tipoarchivo in tipoarchivos.keys():
        directory = directorio + "\\" + tipoarchivo
        if not os.path.exists(directory):
            os.mkdir(directory)

def mover(moveFile, directorio, fileTypes):
    #The file format is what is after the period in the file name
    if "." in moveFile:
        temp = moveFile.split(".")
        fileFormat = temp[-1] 
    else:
        return

    for fileType in fileTypes.keys():
        if fileFormat in fileTypes[fileType]:
            srcPath = directorio + "\\" + moveFile
            dstPath = directorio + "\\" + fileType + "\\" + moveFile

            #If the file doesn't have a duplicate in the new folder, move it
            if not os.path.isfile(dstPath):
                os.rename(srcPath, dstPath)
            #If the file already exists with that name and has the same md5 sum
            elif os.path.isfile(dstPath) and \
                 checkSum(srcPath) == checkSum(dstPath):
                os.remove(srcPath)
                print ("removed " + srcPath)
    return

def checkSum(fileDir, chunkSize = 8192):
        md5 = hashlib.md5()
        f = open(fileDir)
        while True:
            chunk = f.read(chunkSize)
            #If the chunk is empty, reached end of file so stop
            if not chunk:
                break
            md5.update(chunk)
        f.close()
        return md5.hexdigest()



def main():

    #Dictionary contains file types as keys and lists of their corresponding file formats
    fileTypes = {}
    fileTypes["Images"] = ["jpg", "gif", "png", "jpeg", "bmp"]
    fileTypes["Audio"] = ["mp3", "wav", "aiff", "flac", "aac"]
    fileTypes["Video"] = ["m4v", "flv", "mpeg", "mov", "mpg", "mpe", "wmv", \
                          "MOV", "mp4"]
    fileTypes["Documents"] = ["doc", "docx", "txt", "ppt", "pptx", "pdf", "rtf"]
    fileTypes["Exe"] = ["exe"]
    fileTypes["Compressed"] = ["zip", "tar", "7", "rar"]
    fileTypes["Virtual_Machine_and_iso"] = ["vmdk", "ova", "iso"]
    fileTypes["Datasets"]=["csv"]
    
    #The second command line argument is the download directory
    downloadDirectory = sys.argv[1]
    downloadFiles = os.listdir(downloadDirectory)
    crearcarpeta(downloadDirectory, fileTypes)

    for filename in downloadFiles:
        mover(filename, downloadDirectory, fileTypes)

main()