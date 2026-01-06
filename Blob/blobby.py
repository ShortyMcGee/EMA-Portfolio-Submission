
def map_create(self): 
    map = open(self,'r')
    mapped = []
    for line in map: 
        line = line.strip().split()
        if len(line) == 1: 
            new_line = line[0]
            mapped.append(list(new_line))
        else:
            mapped.append(line)
    mapped.pop(0)
    mapped.pop(0)
    return mapped 

def point_check(self,row,clmn,eaten): 
        if self[row][clmn] == 'P': 
            eaten+=1
        self[row][clmn] = 'B'
        rec_blob(self,row,clmn,eaten) 

def spin(self,row,clmn):
    if row == 0:
        if clmn == 0:
            if self[row][clmn+1] == 'P' or self[row][clmn+1] == 'S': 
                return 'right'
            elif self[row+1][clmn] == 'P' or self[row+1][clmn] == 'S': 
                return 'down'
        elif clmn == len(self[0])-1:
            if self[row+1][clmn] == 'P' or self[row+1][clmn] == 'S': 
                return 'down'
            elif self[row][clmn-1] == 'P' or self[row][clmn-1] == 'S': 
                return 'left'
        elif self[row][clmn+1] == 'P' or self[row][clmn+1] == 'S': 
            return 'right'
        elif self[row+1][clmn] == 'P' or self[row+1][clmn] == 'S': 
            return 'down'
        elif self[row][clmn-1] == 'P' or self[row][clmn-1] == 'S': 
            return 'left' 
    if row == len(self[0])-1: 
        if clmn == 0:
            if self[row][clmn+1] == 'P' or self[row][clmn+1] == 'S': 
                return 'right'
            elif self[row+1][clmn] == 'P' or self[row+1][clmn] == 'S': 
                return 'down'
        elif clmn == len(self[0])-1:
            if self[row+1][clmn] == 'P' or self[row+1][clmn] == 'S': 
                return 'down'
            elif self[row][clmn-1] == 'P' or self[row][clmn-1] == 'S': 
                return 'left'
        elif self[row][clmn+1] == 'P' or self[row][clmn+1] == 'S': 
            return 'right'
        elif self[row+1][clmn] == 'P' or self[row+1][clmn] == 'S': 
            return 'down'
        elif self[row][clmn-1] == 'P' or self[row][clmn-1] == 'S': 
            return 'left' 
    elif clmn == 0:
        if self[row-1][clmn] == 'P' or self[row-1][clmn] == 'S': 
            return 'up'
        elif self[row][clmn+1] == 'P' or self[row][clmn+1] == 'S': 
            return 'right'
        elif self[row+1][clmn] == 'P' or self[row+1][clmn] == 'S': 
            return 'down'
    elif clmn >= len(self)-1:
        if self[row-1][clmn] == 'P' or self[row-1][clmn] == 'S': 
            return 'up'
        elif self[row+1][clmn] == 'P' or self[row+1][clmn] == 'S': 
            return 'down'
        elif self[row][clmn-1] == 'P' or self[row][clmn-1] == 'S': 
            return 'left' 
    else:
        if self[row-1][clmn] == 'P' or self[row-1][clmn] == 'S': 
            return 'up'
        elif self[row][clmn+1] == 'P' or self[row][clmn+1] == 'S': 
            return 'right'
        elif self[row+1][clmn] == 'P' or self[row+1][clmn] == 'S': 
            return 'down'
        elif self[row][clmn-1] == 'P' or self[row][clmn-1] == 'S': 
            return 'left'
        else:
            return None

def rec_blob(self,row,clmn,eaten): 
    check = spin(self,row,clmn) 
    if check == 'up':
        return point_check(self,row-1,clmn,eaten) 
    elif check == 'right':
        return point_check(self,row,clmn+1,eaten) 
    elif check == 'down':
        return point_check(self,row+1,clmn,eaten) 
    elif check == 'left': 
        return point_check(self,row,clmn-1,eaten) 
    else: 
        return self 
    
test = 'test.txt' 

brick = rec_blob(map_create(test),0,2,0) 

for line in brick: 
    print(line)
    