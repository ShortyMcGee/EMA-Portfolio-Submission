from patient import Patient 
from heap import Heap 
from tree_node import TreeNode
def file_reader(): 
    file = open(input('Enter Target File: '),'r')
    instructions = []
    patients = Heap()
    arrived = 0
    for line in file: 
        listed = line.strip().split() 
        if listed[0] == 'ARRIVE':
            arrived+=1
            admit = Patient(f'{listed[2]},{listed[1]}',listed[3],listed[4],listed[-1],arrived)
            patients.add(TreeNode(admit))  
        else: 
            instructions.append(line.strip()) 
    for item in instructions:
        if item == 'COUNT': 
            print(f'There are {arrived} patients left in line\n') 
        elif item == 'NEXT': 
            print(f'Next Patient:\n\n    Name: {patients.root._entry._name}\n    Age: {patients.root._entry._age}\n    Suffers From: {patients.root._entry._ailment}\n    Severity: {patients.root._entry._severity}\n    Arrival Order: {patients.root._entry._arrival}\n')
        elif item == 'TREAT': 
            patients.remove() 
            arrived-=1 