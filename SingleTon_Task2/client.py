from singleton_logger import LoggerImp1
from logger import loglevel
log1=LoggerImp1()
log2=LoggerImp1()
log1.set_log_file("application.log")
log1.log(loglevel.INFO,"Use logged in")