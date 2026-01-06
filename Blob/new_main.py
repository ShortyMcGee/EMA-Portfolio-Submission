'''
Noah Short 
3161774 
EECS 268 
Date Created: 10/23/25 
Date Submitted: 11/6/25 
Purpose: To release a blob that fills a given grid on a set path through the use of recursion. It also tracks the amount of times it 'eats' a person. 
'''

#Makes the list of lists the the map is based on 
def map_create(file): 
    city = open(file,'r')
    mapped = []
    for line in city: 
        line = line.strip().split()
        if len(line) == 1: 
            new_line = line[0]
            mapped.append(list(new_line))
        else:
            mapped.append(line)
    mapped.pop(0)
    mapped.pop(0)
    return mapped  

#grabs the top lines of info for final display of information and starting point
def point_grab(file): 
    reader = open(file,'r')
    info = []
    for line in reader: 
        line = line.strip().split() 
        if len(line) == 2: 
            info.append(line) 
    return info

#Checks the whole map for sewer points and returns a list of them 
def sewer_check(city): 
    storage = []
    for num in range(len(city)): 
        for val in range(len(city[0])): 
            if city[num][val] == '@': 
                point = [num,val]
                storage.append(point) 
    return storage 

#Recursive function the compiles all processes to produce final output 
def rec_blob(city,row,clmn,eaten): 
    row_bound = len(city) 
    clmn_bound = len(city[0]) 
    #These are my base cases 
    if row < 0 or row >= row_bound or clmn < 0 or clmn >= clmn_bound: 
        return eaten 
    position = city[row][clmn] 
    if position == 'B' or position == '#': 
        return eaten 
    if position == 'P': 
        eaten+=1  
    city[row][clmn] = 'B' 
    #look up
    eaten = rec_blob(city,row-1,clmn,eaten) 
    #look right 
    eaten = rec_blob(city,row,clmn+1,eaten) 
    #look down 
    eaten = rec_blob(city,row+1,clmn,eaten) 
    #look left 
    eaten = rec_blob(city,row,clmn-1,eaten) 
    if position == '@': 
        points = sewer_check(city)
        for value in points: 
            eaten = rec_blob(city,value[0],value[1],eaten) 
        city[row][clmn] = '@'
    return eaten

def main(): 
    file = input('Enter file name: ')
    city = map_create(file)
    eaten = rec_blob(city,int(point_grab(file)[1][0]),int(point_grab(file)[1][0]),0)
    for entry in point_grab(file): 
        print(' '.join(entry)) 
    for entry in city: 
        print(''.join(entry)) 
    print(f'People eaten = {eaten}') 

main()