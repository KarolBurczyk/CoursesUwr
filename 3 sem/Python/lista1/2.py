import math
znaki = (" ", ",", "'", "-", "...", ".", "!", "?", ":", ";", "/")

def is_palindrom(text):
    s = text.lower()
    newstr = ""
    for elem in s:
        if elem not in znaki:
            newstr += elem
    for i in range(math.ceil(len(newstr) / 2)):
        if newstr[i] != newstr[len(newstr) - 1 - i]:
            return False
    return True

print(is_palindrom("Eine güldne, gute Tugend: Lüge nie!"))
print(is_palindrom("Míč omočím."))
print(is_palindrom("Kobyła ma mały bok."))
print(is_palindrom("rotor"))
