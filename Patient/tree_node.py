class TreeNode: 
    def __init__(self,entry): 
        self._left = None 
        self._entry = entry
        self._right = None 
        self._parent = None
    def __lt__(self,other): 
        if self._entry < other._entry: 
            return True 
        else: 
            return False