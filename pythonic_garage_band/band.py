from abc import abstractmethod


class Musician:
    '''
    base class (parent)
    contain __str__,__repr__ function that return a name and instrument for the Musician
    and there is a  get_instrument method that return the what every Musician play with
    And in the end we have play_solo method that a abstract method 
    
    '''
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'
    # @abstractmethod
    def get_instrument(self):
        return f'{self.type}'
        
    @abstractmethod
    def play_solo(self):
        pass


class Band(Musician):
    '''
    sub class (child)
    it inherits attributes and method from the base class (Musician)
    also it have a to_list method that a class method 
    and there is a play_solos method that contain a for loop to represent what each member plays
    
    '''
    instances=[]
    def __init__(self,name,members):
        self.members=members
        Band.instances.append(self)
        super().__init__(name)

    @classmethod
    def to_list(cls):
        return cls.instances

    def play_solos(self):
        solos=[]
        for i in self.members:
            solos.append(i.play_solo())
        return solos
    
class Guitarist(Musician):
    '''
    sub class (child)
    it inherits attributes and method from the base class (Musician)
    and there is a play_solo method that return what the Musician plays
    
    '''
    type='guitar'
    # def get_instrument(self):
    #     return f'{self.type}'
    def play_solo(self):
        return "face melting guitar solo"



class Bassist(Musician):
    '''
    sub class (child)
    it inherits attributes and method from the base class (Musician)
    and there is a play_solo method that return what the Musician plays
    
    '''
    type='bass'
    # def get_instrument(self):
    #     return f'{self.type}'
    def play_solo(self):
        return "bom bom buh bom"

    

class Drummer(Musician):
    '''
    sub class (child)
    it inherits attributes and method from the base class (Musician)
    and there is a play_solo method that return what the Musician plays
    
    '''
    type='drums'
    # def get_instrument(self):
    #     return f'{self.type}'
    def play_solo(self):
        return "rattle boom crash"


