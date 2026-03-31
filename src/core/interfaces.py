from abc import ABC, abstractmethod

class AgentInterface(ABC):
    @abstractmethod
    def act(self):
        pass

class EnvironmentInterface(ABC):
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def step(self, action):
        pass
    
    @abstractmethod
    def render(self):
        pass
