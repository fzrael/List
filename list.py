import random
import time
import string
def g (w = 3):
    le = string.ascii_letters
    return ''.join((random.choice(le) for i in range(w)))

q= input('Enter Name File: ')
d = input('How many letters: ')
e = input('How many do you want:')

with open(f'{q}''.txt', 'w') as file:
    start = time.time()
    for x in range(int(e)):
        file.write(g(int(d)) + '\n')



    print("\nDonnnne (=\n")