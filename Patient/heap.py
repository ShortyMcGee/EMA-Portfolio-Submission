from tree_node import TreeNode
class Heap: 
    def __init__(self): 
        self.root = None 
        self.nodes = []

    def upheap(self,entry): 
        current_node = entry
        while current_node._parent != None and current_node._parent._entry < current_node._entry and current_node != None: 
            parent_node = current_node._parent
            temp_value = current_node._entry
            current_node._entry = current_node._parent._entry
            parent_node._entry = temp_value
            current_node = parent_node

    def downheap(self,entry):  
        check = True
        current_node = entry
        while check ==True:  
            largest = current_node 
            if current_node._left != None and largest._entry < current_node._left._entry: 
                largest = current_node._left
            if  current_node._right != None and largest._entry < current_node._right._entry: 
                largest = current_node._right 
            if largest == current_node: 
                check = False
            temp_value = current_node._entry 
            current_node._entry = largest._entry
            largest._entry = temp_value 
            current_node = largest
            

    def add(self,entry): 
        if self.root == None: 
            self.root = entry 
            self.nodes.append(entry)
            return None
        node_index = len(self.nodes) 
        parent_index = (len(self.nodes)-1)//2 
        parent = self.nodes[parent_index]
        entry._parent = self.nodes[parent_index] 
        if node_index % 2 == 1: 
            parent._left = entry 
        else: 
            parent._right = entry
        self.nodes.append(entry) 
        self.upheap(entry)  

    def remove(self): 
        if not self.nodes: 
            return None 
        removed = self.root._entry 
        if len(self.nodes) == 1: 
            self.nodes = []
            self.root = None 
            return removed
        new_root = self.nodes.pop() 
        root_parent = new_root._parent 
        if root_parent: 
            if root_parent._left == new_root: 
                root_parent._left = None 
            else: 
                root_parent._right = None 
        self.root._entry = new_root._entry
        self.downheap(self.root) 
        return removed 
