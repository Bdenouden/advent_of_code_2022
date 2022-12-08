import sys


class Dir:
    sumsize = 0
    # directories = {}
    def __init__(self, name, parent = None) -> None:
        self.name = name # dir name
        self.parent = parent # parent of the new dir
        self.child = {} # name:obj format
        self.files = {} # dict containing filenames with size

    def getSize(self):
        size = 0
        for d, obj in self.child.items():
            size += obj.getSize()
        for s in self.files.values():
            size += s
        if size <= 100000:
            Dir.sumsize += size
        return size

    def printStruct(self, indent = 0):
        print(f"{'  '*indent}- {self.name} (dir)")
        for d, obj in self.child.items():
            obj.printStruct(indent +1)
        for name, size in self.files.items():
            print(f"{'  '*(indent+1)}- {name} (file, size={size})")

root = Dir("/")
currentDir = root

with open(sys.path[0] + '/input.txt') as f:
    for lineNum, line in enumerate(f):
        line = line.strip()
        if line[:4] == "$ cd":  # cd operation
            newDir = line.split(" ")[2]
            if newDir == "..":
                currentDir = currentDir.parent
            elif newDir == "/":
                currentDir = root
            else: 
                currentDir = currentDir.child[newDir]
        elif line[:4] == "$ ls":  # list operation, no action
            pass
        elif line[:4] == "dir ":  # directory found
            newDir = line.split(" ")[1]
            currentDir.child[newDir] = Dir(newDir, currentDir)
        
        else:  # file
            temp = line.split(" ")
            currentDir.files[temp[1]] = int(temp[0])

root.printStruct()
root.getSize()
print(Dir.sumsize)
# print(root.getSize())
# for key, obj in Dir.directories.items():
#     print(f" - {key}: {obj.getSize()}")
