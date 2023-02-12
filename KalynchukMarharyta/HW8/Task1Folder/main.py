from models import *
from utils import *

#Виходить вивести лише ['admin', 'format', 'logger', 'user'], не ['create_admin', ...] 
print(list(filter(lambda str: ('__' not in str), dir())))

#Але доступ до методів модулів є 
logger.log_in_file()

