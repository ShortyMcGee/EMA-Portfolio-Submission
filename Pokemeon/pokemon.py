class Poke_Enrty: 
    def __init__(self,poke_num): 
        self._root = int(poke_num)
        self._eng = None 
        self._jap = None
        self._left = None 
        self._right = None 

    def __eq__(self,other): 
        if self._root == other: 
            return True 
        else: 
            return False 
        
    def __lt__(self,other): 
        if self._root < other: 
            return True 
        else: 
            return False 
        
    def __gt__(self,other): 
        if self._root > other: 
            return True 
        else: 
            return False  
        
    def insert(self,entry): 
        if self._root == int(entry[1]): 
            raise ValueError('MATCHING ENTRY FOUND') 
        elif self._root > int(entry[1]): 
            if self._left == None: 
                self._left = Poke_Enrty(int(entry[1]))
                self._left._eng = entry[0] 
                self._left._jap = entry[2]
            else:
                self._left.insert(entry)  
        elif self._root < int(entry[1]):
            if self._right == None: 
                self._right = Poke_Enrty(int(entry[1])) 
                self._right._eng = entry[0] 
                self._right._jap = entry[2]
            else:
                self._right.insert(entry)

    def in_order(self): 
        if self._left:
            self._left.in_order()
        print(f'{self._eng}  {self._root}  {self._jap}')
        if self._right: 
            self._right.in_order() 

    def pre_order(self): 
        print(f'{self._eng}  {self._root}  {self._jap}')
        if self._left:
            self._left.pre_order()
        if self._right: 
            self._right.pre_order()

    def post_order(self): 
        if self._left:
            self._left.post_order()
        if self._right: 
            self._right.post_order() 
        print(f'{self._eng}  {self._root}  {self._jap}')

    def search(self,target): 
        if target == self._root: 
            print(f'---Entry Found!---\n{self._eng}  {self._root}  {self._jap}')  
        elif self._root < target: 
            self._right.search(target) 
        elif self._root > target: 
            self._left.search(target)  
        else: 
            print('ENTRY NOT FOUND') 

    def remove(self, target): 
        if target < self._root: 
            if self._left != None: 
                self._left = self._left.remove(target)
            return self 
        elif target > self._root: 
            if self._right != None: 
                self._right = self._right.remove(target)
            return self 
        else: 
            if self._left == None and self._right == None: 
                return None 
            if self._left == None:
                return self._right 
            if self._right == None: 
                return self._left 
            replace = self._left 
            while replace._right != None: 
                replace = replace._right 
            self._root = replace._root 
            self._eng = replace._eng 
            self._jap = replace._jap 
            self._left = self._left.remove(replace._root) 
            return self 