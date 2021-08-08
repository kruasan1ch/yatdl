from abc import ABC, abstractmethod

class dbclass(ABC):

    @abstractmethod
    def get(self):
        pass


    @abstractmethod
    def insert(self, dataLine):
        pass


    @abstractmethod
    def update(self, dataLine):
        pass


    @abstractmethod
    def isRegistered(self, name, password):
        pass

    
    @abstractmethod
    def register(self,isAdmin ,name, password, role):
        pass
