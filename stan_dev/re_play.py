import re


name = "cyril grayson jr"

name = re.sub(" jr", "", name)

print(name)
print(len(name))