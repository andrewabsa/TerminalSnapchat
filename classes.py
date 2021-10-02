import random


class Username():
    def __init__(self, nickname):
        self.nickname = nickname
        self.name_list = []
        
    def add_name(self):
        self.name_list.append(self.nickname)
    

class Message():
    def __init__(self):
        pass

    def send_text(self, txt):
        pass

    def send_messages(self):
        pass

class Names():
    def __init__(self, namelist):
        self.value = {
            "Tom": 0,
            "Emmanuel": 0,
            "Brad": 0,
            "Russel": 0
         }
        for name in namelist:
            self.value[name.value] += 5

    def name_choice(self):
        self.nickname = random.choice(self.value)


 

            
    


   

    
   
    
    




    

