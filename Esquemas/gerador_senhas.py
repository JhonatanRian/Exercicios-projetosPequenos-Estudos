import random, string

size: int = 16

char: string = string.ascii_letters + string.digits + "+@!#-$*&?@!*&"

rnd: random = random.SystemRandom()

password = [(rnd.choice(char)) for i in range(size)]

print("".join(password))