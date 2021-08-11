from abc import ABC, abstractmethod

class dbclass(ABC):

    @abstractmethod
    def get(self):
        pass


    @abstractmethod
    def insert(self, dataLine):
        pass


    @abstractmethod
    def updateData(self, dataLine):
        pass


    @abstractmethod
    def isRegistered(self, username, password):
        pass

    
    @abstractmethod
    def register(self,isAdmin ,username, password, role):
        pass

    @abstractmethod
    def getUserData(self, username):
        pass
