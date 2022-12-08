import sys


class Dir:
    sizes = []
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
        self.size = size
        return size

    def printStruct(self, indent = 0):
        print(f"{'  '*indent}- {self.name} (dir)")
        for d, obj in self.child.items():
            obj.printStruct(indent +1)
        for name, size in self.files.items():
            print(f"{'  '*(indent+1)}- {name} (file, size={size})")
    
    def lowestDirAboveThreshold(self, threshold):
        if(self.size > threshold):
            Dir.sizes.append(self.size)
        for name, obj in self.child.items():
            if(obj.size >= threshold):
                print(name, obj.size)
                obj.lowestDirAboveThreshold(threshold)

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

rootSize = root.getSize()
root.printStruct()
print(rootSize, root.size)
threshold = 30000000 - (70000000 - rootSize)
print(f"threshold={threshold}")
root.lowestDirAboveThreshold(threshold)
Dir.sizes.sort()
print(Dir.sizes)
