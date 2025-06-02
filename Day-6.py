import random
import string

all_characters = string.ascii_letters + string.digits + string.punctuation
# string.ascii_letters gives all letters (a-z and A-Z).
# string.digits gives numbers (0-9).
# string.punctuation gives special characters like !@#$%^&*().
# We add (+) them together to make one big set of characters.

password = ''.join(random.choices(all_characters, k=8))
# random.choices(characters, k=8) picks 8 random characters from the list.
# ''.join(...) joins those characters into one string to make the password.

print("Random 8 character Password is:", password)



