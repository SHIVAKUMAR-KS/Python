import random

def generate_password(nl, ns, nn):
    letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password = []

    password += [random.choice(letters) for _ in range(nl)]
    password += [random.choice(symbols) for _ in range(ns)]
    password += [random.choice(numbers) for _ in range(nn)]

    return "".join(password)

print("Welcome to the Password Generator!")
nl = int(input("How many letters would you like in your password?\n"))
ns = int(input("How many symbols would you like?\n"))
nn = int(input("How many numbers would you like?\n"))

generated_password = generate_password(nl, ns, nn)
print("Your generated password is:", generated_password)
