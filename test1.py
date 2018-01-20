import re

a = re.search(r'\d+', 'aaa35213').group()
print(a)