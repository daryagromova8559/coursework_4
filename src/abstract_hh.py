from abc import ABC, abstractmethod


class AbstractHH(ABC):

    @abstractmethod
    def get_url(self):
        pass
