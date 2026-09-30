from abc import ABC,abstractmethod
from enum import Enum
class loglevel(Enum):
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO kjklhjh"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"
class logger(ABC):
    @abstractmethod
    def log(self,level,message):
        pass
    @abstractmethod
    def set_log_file(self,file_path):
        pass
    @abstractmethod
    def get_log_file(self):
        pass
    @abstractmethod
    def flush(self):
        pass
    @abstractmethod
    def remove(self):
        pass
    