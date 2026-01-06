class Patient: 
    def __init__(self,name,age,ailment,severity,arival): 
        self._name = name 
        self._age = int(age) 
        self._ailment = ailment 
        self._severity = int(severity) 
        self._arrival = int(arival) 

    def __lt__(self,other):
        if self._severity < other._severity: 
            return True 
        elif self._age < other._age: 
                return True 
        elif self._arrival < other._arrival: 
                return True 
        else: 
            return False 
    
