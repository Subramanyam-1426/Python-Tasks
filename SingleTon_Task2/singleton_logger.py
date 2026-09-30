from datetime import datetime
from logger import logger
class LoggerImp1(logger):
    _instance=None
    def __new__(cls):
        if (cls._instance==None):
            cls._instance=super().__new__(cls)
        return cls._instance
    def log(self,level,message):
         if self.file_path is None:
              raise Exception("File path is not created")
         timestamp=datetime.now()
         entry = (f"{timestamp} {level.value} {message}")
         with open(self.file_path,"a") as file:
              file.write(entry)
    def set_log_file(self,file_path):
        self.file_path=file_path
    def get_log_file(self):
        return self.file_path
    def flush(self):
            pass
    def remove(self):
            pass
    @classmethod
    def reset(cls):
        cls._instance=None