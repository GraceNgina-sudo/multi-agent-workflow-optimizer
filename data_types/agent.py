from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractmethod
    def run(self, input_data):
        pass
    def describe(self):
        return f"{self.role.capitalize()} Agent: {self.name}"
    
    

