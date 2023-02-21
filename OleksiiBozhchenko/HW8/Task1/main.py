# 1. Create structure:
#     main folder > main.py

#     main folder > models
#     main folder > models > __init__.py
#     main folder > models > admin.py
#     main folder > models > user.py

#     main folder > utils
#     main folder > utils > __init__.py
#     main folder > utils > formatter.py
#     main folder > utils > logger.py

# 2. Create functions "create_user", "create_admin", "log_in_file", "format_string" in corresponding modules. 
# This functions may have implementations like "pass".
# 3. Define "__all__" in all modules so that they contain only the functions from the previous step
# (you can create some additional functions to test it).
# 4. Fill "__init__.py" files in packages so that import * of these packages contain only functions from second step.
# 5. In "main.py" file write next code:
#     from utils import *
#     from models import *
#     print(list(filter(lambda str: not ("__" in str), dir())))

# You must odtain like list like this ['create_admin', 'create_user', 'format_string', 'log_in_file']

from utils import *
from models import *
    
print(list(filter(lambda str: not ("__" in str), dir())))