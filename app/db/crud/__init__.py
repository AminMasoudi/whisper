from abc import ABC, abstractmethod

class BaseCrud(ABC):
    @abstractmethod
    def create(): ...

    @abstractmethod
    def retrieve(): ...

    @abstractmethod
    def list(): ...

    @abstractmethod
    def update(): ...

    @abstractmethod
    def delete(): ...