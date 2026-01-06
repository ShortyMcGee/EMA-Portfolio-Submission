'''
Noah Short 
3161774 
Date Created: 11/13/25 
Date Submitted: 11/20/25 
Purpose: To sort given pokedex entries into a BST that can be editted and accessed through each entries key 
'''

from pokemon import Poke_Enrty 

def add(self): 
    prompt = int(input(f'Add individual entry or file?\n1) Individual\n2) File\nSelection: '))
    if prompt == 1: 
        new_root = (input(f'Enter English Name,Number,Japanese Name\nEntry: ').strip().split(',')) 
        if self == None:
                self = Poke_Enrty(new_root[1])
                self._eng = new_root[0]
                self._jap = new_root[2]
                print(f'Created new Pokedex with entry {new_root[1]}')
                return self
        else:
                self.insert(entry)
                print(f'Successfully inserted entry {new_root[1]}')
        return self 
    elif prompt == 2: 
        file = open(input('Enter desired file name: '),'r') 
        tester = []
        for line in file: 
            list = line.strip().split() 
            tester.append(list) 
        self = Poke_Enrty(tester[0][1]) 
        for entry in tester[1:]: 
            self.insert(entry)  
        return self 
    else: 
        print('INVALID CHOICE') 
        return self
    
def searcher(self): 
    target = int(input('Enter targeted entry: ')) 
    return self.search(target) 

def printer(self): 
    choice = int(input(f'Select desired order:\n1) In Order\n2) Pre Order\n3) Post Order\nSelection: '))
    if choice == 1: 
        self.in_order() 
    elif choice == 2: 
        self.pre_order() 
    elif choice == 3: 
        self.post_order() 
    
def remover(self): 
    choice = int(input('Enter entry for removal: ')) 
    chopped = self.search(choice)
    print('ABOVE ENTRY REMOVED')
    self.remove(choice) 

def copy(self): 
    copied = self 
    return copied 

def main(): 
    poke = None
    copied = None
    option = int(input(f'------Welcome to the Poke-dex------\n1) Add \n2) Search\n3) Print\n4) Remove\n5) Copy\n6) Quit\nSelection: '))
    while option != 6: 
        if option == 1:
            if copied != None: 
                select = int(input(f'1) Original\n2) Copy\nSelection: '))
                if select == 1: 
                    poke = add(poke)
                elif select == 2: 
                    copied = add(copied) 
                else: 
                    print('INVALID SELECTION')
            else: 
                poke = add(poke) 
        elif option == 2: 
            if copied != None: 
                select = int(input(f'1) Original\n2) Copy\nSelection: '))
                if select == 1: 
                    searcher(poke)
                elif select == 2: 
                    searcher(copied) 
                else: 
                    print('INVALID SELECTION')
            else: 
                searcher(poke) 
        elif option == 3: 
            if copied != None: 
                select = int(input(f'1) Original\n2) Copy\nSelection: '))
                if select == 1: 
                    printer(poke)
                elif select == 2: 
                    printer(copied) 
                else: 
                    print('INVALID SELECTION')
            else: 
                printer(poke) 
        elif option == 4: 
            if copied != None: 
                select = int(input(f'1) Original\n2) Copy\nSelection '))
                if select == 1: 
                    remover(poke)
                elif select == 2: 
                    remover(copied) 
                else: 
                    print('INVALID SELECTION')
            else: 
                remover(poke) 
        elif option == 5: 
            if copied != None: 
                print('MAX COPIES ACHIEVED') 
            else: 
                copied = copy(poke) 
                print('List Copied') 
        option = int(input(f'------Welcome to the Poke-dex------\n1) Add \n2) Search\n3) Print\n4) Remove\n5) Copy\n6) Quit\nSelection: '))
    print('Exiting...')  

main()
