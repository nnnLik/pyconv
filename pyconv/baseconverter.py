from abc import ABC, abstractmethod


class BaseConverter(ABC):
    @abstractmethod
    def convert(self, input_file, output_format):
        pass
