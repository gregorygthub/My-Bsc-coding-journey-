import random, string

def gen_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength(pwd):
    score = sum([
        len(pwd) >= 12,
        any(c.isupper() for c in pwd),
        any(c.islower() for c in pwd),
        any(c.isdigit() for c in pwd),
        any(c in "!@#$%^&*" for c in pwd)
    ])
    return ["Trash", "Weak", "Mid", "Strong", "G-Wagon Level"][score]

if __name__ == "__main__":
    pwd = gen_password(16)
    print(f"Generated: {pwd}")
    print(f"Strength: {check_strength(pwd)}")

