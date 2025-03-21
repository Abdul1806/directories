'''
python file for this take home project:

Create a program that takes in commands: create, list, move, delete
create(file/folder): either creates sub folders or a file within a folder
list: displays current structure of all files/folders
move(fileToMove destination): move specific file/folder to designated place
delete(pathToFileToDelete): if the exact file path exists for what we want to delete then delete it

idea: use a tree directory to keep track of each different folder structure and we'll
      use the parent child relationship to track folder/file strucutre
      I'll use a dictionary to contain each child and it's node
'''

class Node:
    def __init__(self,name,parent=None):
        self.name = name
        self.parent = parent
        self.children = {}
        

class Directory:
    def __init__(self, parent=None, children =[]):
        self.root = {}

    #Helper to go to a specific node given a path
    def _navigateToNode(self,path):
        parts = path.split("/")
        cur_node = self.root.get(parts[0])
        #print(f"cur_node name: {cur_node.name}, parent: {cur_node.parent}, children: {cur_node.children}")
        for part in parts[1:]:
            #print(f"part: {part}")
            if cur_node and part in cur_node.children:
                cur_node = cur_node.children[part]
            else:
                return None
        return cur_node

    #Helper to rearrange parent tracking this specific child node
    def _removeFromParent(self,node):
        if node.parent:
            node.parent.children.pop(node.name)
        else:
            self.root.pop(node.name)
            
    def create(self,path):
        parts = path.split("/")
        cur_level = self.root
        parent = None
        for part in parts:
            if part not in cur_level:
                cur_level[part] = Node(part,parent)
            parent = cur_level[part]
            cur_level = cur_level[part].children

    def move(self,source, destination):
        s_node = self._navigateToNode(source)
        d_node = self._navigateToNode(destination)

        if s_node is None:
            print(f" Can't move {source} it doesn't exist")
            return
        
        if d_node is None:
            #Q: Should I error handle this and say that we can't move?
            #I don't think so I think we should be able to move anywhere we want to and if it doesn't exist then create it
            #This would be production level code that the email was looking for 
            self.create(destination)
            d_node = self._navigateToNode(destination)
            
        #remove parent from tracking this child
        self._removeFromParent(s_node)
            
        #update parent child relationship for destination node
        d_node.children[s_node.name] = s_node
        s_node.parent = d_node
        
    def delete(self,path):
        delete_node = self._navigateToNode(path)
        #we couldn't navigate to the path so we can't delete
        if delete_node is None:
            print(f"Cannot delete {path} - {path.split('/')[0]} does not exist")
            return
        self._removeFromParent(delete_node)
    
    def list(self):
        def dfs(cur_dict,indent):
            for name in sorted(cur_dict.keys()):
                print(" " *indent + name)
                dfs(cur_dict[name].children,indent +1)
        dfs(self.root, 0)


def process(commands):
    tree = Directory()
    for line in commands:
        if not line.strip():
            continue
        print(line)
        parts = line.strip().split()
        cmd = parts[0]
        if cmd == 'CREATE':
            tree.create(parts[1])
        elif cmd == 'MOVE':
            tree.move(parts[1], parts[2])
        elif cmd == 'DELETE':
            tree.delete(parts[1])
        elif cmd == 'LIST':
            tree.list()
def test():
    commands = [
    "CREATE fruits",
    "CREATE vegetables",
    "CREATE grains",
    "CREATE fruits/apples",
    "CREATE fruits/apples/fuji",
    "LIST",
    "CREATE grains/squash",
    "MOVE grains/squash vegetables",
    "CREATE foods",
    "MOVE grains foods",
    "MOVE fruits foods",
    "MOVE vegetables foods",
    "LIST",
    "DELETE fruits/apples",
    "DELETE foods/fruits/apples",
    "LIST"
    ]
    commands2 = [
        "CREATE fruits",
        "LIST",
        "DELETE fruits/apple",
        "LIST",
        "DELETE fruits",
        "LIST",
        ]
    print("We are running this input: {command}")
    process(commands)
    
def main():
    tree = Directory()
    print("Enter commands CREATE, MOVE, DELETE, LIST\nTo end the program just click enter")
    print("Write a command >>> (or just write TEST if you want to run the given input)")
    while True:
        command = input().strip().split()
        if command is None:
            continue
        cmd = command[0]
        
        if cmd.upper() == 'CREATE' and len(command) == 2:
            tree.create(command[1])
        elif cmd.upper() == 'MOVE' and len(command) == 3:
            tree.move(command[1], command[2])
        elif cmd.upper() == 'DELETE' and len(command) == 2:
            tree.delete(command[1])
        elif cmd.upper() == 'LIST':
            tree.list()
        elif cmd.upper() == 'TEST':
            test()
        else:
            print("Invalid commands. Try again")

    
        
if __name__ == "__main__":
    main()
