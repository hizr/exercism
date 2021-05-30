import random
import string

class Robot:
    __blacklist = []
    
    def __init__(self): 
        self.name = self.__generate_name()

    def reset(self):
        self.name = self.__generate_name()

    def __generate_name(self):
        name = self.__random_name()
        if name in self.__blacklist:
            self.__generate_name()
        else:
            self.__blacklist.append(name)
            return name

    def __random_name(self):
        random.seed()
        prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
        suffix = random.randint(100, 999)
        return f"{prefix}{suffix}"
