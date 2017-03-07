import os
import sys

os.chdir(sys.argv[1])
parentPath = sys.argv[1]

for file in os.listdir("."):
    if os.path.isdir(file):
        print(file)
        os.chdir(file)
        for innerFile in os.listdir("."):
            if innerFile.endswith(".ptx") and innerFile != file + ".ptx":
                print(innerFile)
                os.rename(innerFile, file + ".ptx")
            os.chdir(parentPath)
