
str = "3214231"
pos = "3"

def hi(str, pos):
    for i in str:
            if i is pos:
                return False
    return True

print(hi(str, pos))