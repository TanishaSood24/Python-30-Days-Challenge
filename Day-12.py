import re

def is_valid_gmail(email):
    # Regex Pattern for valid Gmail addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'

    # re.match() to check if the pattern matches the input email
    if re.match(pattern, email):
        return True
    else:
        return False

emails = [
    "john.doe@gmail.com",
    "123_abc@gmail.com",
    "test@outlook.com",
    "hello.world@GMAIL.COM",
    "invalid@gmail"
]

check = '\u2705 Valid'    # ✅
cross = '\u274C Invalid'  # ❌

for email in emails:
    print(f"{email} → {check if is_valid_gmail(email) else cross}")





