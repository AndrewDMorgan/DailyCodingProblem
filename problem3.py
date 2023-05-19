
# the node class
class Node:
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

# generatates a dictionary of all the nodes
def GetNodes(node, values={}, depth=0, x=0):
    # adding a dictionary to the dictionary at the depth
    if depth not in values:
        values[depth]={}
    # adding the value of the node
    values[depth][x] = node.val
    if node.left: GetNodes(node.left, values, depth+1, x)
    if node.right: GetNodes(node.right, values, depth+1, x+1)
    return values

# serializing the bianry tree
def Serialize(node):
    # the values in a dictionary
    values = GetNodes(node)
    
    # getting the max depth of the tree
    maxDepth = max([key for key in values])
    
    # the layers of the pyrimid
    layers = ""
    numWide=1  # the width of the tree (max width possible)
    # looping through the binary tree
    for depth in range(maxDepth+1):
        row = ""
        # looping through the row
        for x in range(numWide):
            # adding a node or a blank cell
            if x in values[depth]:
                row += values[depth][x]
            else:
                row += "None"
            if x<numWide-1: row += ","
        # adding up the row and doubling the max possible width
        layers += row + "\n"
        numWide*=2
    
    # returning the serialized binary tree
    return layers

# generates the nodes from the dictionary
def GenerateNode(values, x, depth, maxDepth):
    # checking if it's still in bounds
    if depth < maxDepth:
        # checking if the tree contains a value there
        if values[depth][x] == None:
            return None  # no valid node
        # returning a node composed of more nodes
        return Node(values[depth][x], GenerateNode(values, x, depth+1, maxDepth), GenerateNode(values, x+1, depth+1, maxDepth))
    return None  # no value node

# deserializing the binary tree
def Deserialize(string):
    # generating a dictionary
    values = {}
    
    # the layers of the tree
    layers = string.split("\n")[:-1]
    
    # looping through the layers
    for y, layer in enumerate(layers):
        # adding a dictionary for the row
        values[y] = {}
        # looping through the row
        for x, val in enumerate(layer.split(",")):
            if val!="None":  # checking if there is a node here
                values[y][x] = val
            else:  # there is no node here
                values[y][x] = None
    
    # generating the binary tree
    nodes = GenerateNode(values, 0, 0, len(layers))
    return nodes  # returning the generated binary tree


# testing the binary tree
tree = Node("root", Node("left", Node("left.left")), Node("right"))
serialized = Serialize(tree)
print(serialized)
print(Deserialize(serialized))
