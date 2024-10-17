from abc import ABC, abstractmethod


class VisualizerBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def save(self, filename):
        pass
