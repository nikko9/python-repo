import random
import string

size = int(input("write the size of password do you want:"))

chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+,.;:?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(size)))
