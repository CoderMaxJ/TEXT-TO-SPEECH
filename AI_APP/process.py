import random 
import string

length=6

characters = string.ascii_letters + string.digits

random_code=''.join(random.choice(characters) for i in range(length))

print(random_code)


