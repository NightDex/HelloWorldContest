import string, random

# alphabet
lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabet = list(string.ascii_uppercase)
new_punctionation = list(string.punctuation)

# shuffled alphabet
random.shuffle(lowercase_alphabet)
random.shuffle(uppercase_alphabet)
# shuffle punctionation
random.shuffle(new_punctionation)

# functions that finds letters in lists
def find_H():
    for position, h in enumerate(uppercase_alphabet):
        if h == "H":
            return position
        continue

def find_e():
    for position, e in enumerate(lowercase_alphabet):
        if e == "e":
            return position
        continue

def find_l():
    for position, l in enumerate(lowercase_alphabet):
        if l == "l":
            return position
        continue

def find_o():
    for position, o in enumerate(lowercase_alphabet):
        if o == "o":
            return position
        continue

def find_W():
    for position, w in enumerate(uppercase_alphabet):
        if w == "W":
            return position
        continue

def find_r():
    for position, r in enumerate(lowercase_alphabet):
        if r == "r":
            return position
        continue

def find_d():
    for position, d in enumerate(lowercase_alphabet):
        if d == "d":
            return position
        continue

def find_exclamation_point():
    for position, t in enumerate(new_punctionation):
        if t == "!":
            return position
        continue

string_code = [find_H(), find_e(), find_l(), find_l(), find_o(), find_W(), find_o(), find_r(), find_l(), find_d(), find_exclamation_point()]


# In original alphabet list H position is 7
if string_code[0] > 7:
    while string_code[0]>7:
        string_code[0] -= 1
elif string_code[0] < 7:
    while string_code[0] < 7:
        string_code[0] += 1
else:
    pass

# In original alphabet list e position is 4
if string_code[1] > 4:
    while string_code[1]>4:
        string_code[1] -= 1
elif string_code[1] < 4:
    while string_code[1] < 4:
        string_code[1] += 1
else:
    pass

# In original alphabet list l position is 11 
if string_code[2] > 11:
    while string_code[2]>11:
        string_code[2] -= 1
elif string_code[2] < 11:
    while string_code[2] < 11:
        string_code[2] += 1
else:
    pass

# In original alphabet list l position is 11  (here we find 2nd l position)
if string_code[3] > 11:
    while string_code[3]>11:
        string_code[3] -= 1
elif string_code[3] < 11:
    while string_code[3] < 11:
        string_code[3] += 1
else:
    pass

# In original alphabet list o position is 14 
if string_code[4] > 14:
    while string_code[4]>14:
        string_code[4] -= 1
elif string_code[4] < 14:
    while string_code[4] < 14:
        string_code[4] += 1
else:
    pass

# In original alphabet list w position is 22 
if string_code[5] > 22:
    while string_code[5]>22:
        string_code[5] -= 1
elif string_code[5] < 22:
    while string_code[5] < 22:
        string_code[5] += 1
else:
    pass

# In original alphabet list o position is 14 (here we find 2nd o position)
if string_code[6] > 14:
    while string_code[6]>14:
        string_code[6] -= 1
elif string_code[6] < 14:
    while string_code[6] < 14:
        string_code[6] += 1
else:
    pass

# In original alphabet list r position is 17
if string_code[7] > 17:
    while string_code[7]>17:
        string_code[7] -= 1
elif string_code[7] < 17:
    while string_code[7] < 17:
        string_code[7] += 1
else:
    pass

# In original alphabet list l position is 11  (here we find 3rd l position)
if string_code[8] > 11:
    while string_code[8]>11:
        string_code[8] -= 1
elif string_code[8] < 11:
    while string_code[8] < 11:
        string_code[8] += 1
else:
    pass

# In original alphabet list d position is 3
if string_code[9] > 3:
    while string_code[9]>3:
        string_code[9] -= 1
elif string_code[9] < 3:
    while string_code[9] < 3:
        string_code[9] += 1
else:
    pass

# In original punctionation list ! position is 0
if string_code[10] > 0:
    while string_code[10]>0:
        string_code[10] -= 1
elif string_code[10] < 0:
    while string_code[10] < 0:
        string_code[10] += 1
else:
    pass

ewewew = string.ascii_lowercase[string_code[7]]
e1 = string.ascii_uppercase[string_code[0]]
nvnfjvfjf = string.ascii_lowercase[string_code[4]]
jhdhd5 = string.ascii_lowercase[string_code[2]]
rhgj7 = string.ascii_lowercase[string_code[3]]
oopoo = string.ascii_uppercase[string_code[5]]
bcdcs = string.ascii_lowercase[string_code[6]]
o67 = string.ascii_lowercase[string_code[1]]
oisdrj = string.punctuation[string_code[10]]
lolol = string.ascii_lowercase[string_code[8]]
djdjdjd = string.ascii_lowercase[string_code[9]]

print(f"{e1}{o67}{jhdhd5}{rhgj7}{nvnfjvfjf} {oopoo}{bcdcs}{ewewew}{lolol}{djdjdjd}{oisdrj}")
