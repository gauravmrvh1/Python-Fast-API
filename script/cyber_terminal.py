import random
import time
import sys
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def typing(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def loading(text, duration=3):
    typing(text)
    for _ in range(duration):
        for symbol in "|/-\\":
            sys.stdout.write("\r" + symbol)
            sys.stdout.flush()
            time.sleep(0.1)
    print("\r✔ Done!")

def matrix_effect():
    chars = "01"
    for _ in range(10):
        line = "".join(random.choice(chars) for _ in range(60))
        print(line)
        time.sleep(0.05)

def start_game():
    clear()
    typing("🔐 INITIALIZING CYBER ACCESS SYSTEM...\n", 0.04)
    loading("Connecting to secure server...")
    loading("Bypassing firewall...")
    loading("Decrypting data blocks...")

    matrix_effect()

    secret_code = str(random.randint(1000, 9999))
    attempts = 5

    typing("\n⚠ SECURITY LEVEL: HIGH")
    typing("You must guess the 4-digit access code.")
    typing(f"You have {attempts} attempts.\n")

    while attempts > 0:
        guess = input("Enter access code: ")

        if guess == secret_code:
            typing("\n✅ ACCESS GRANTED")
            typing("Welcome, Elite Hacker 😎")
            return
        else:
            attempts -= 1
            typing(f"❌ ACCESS DENIED | Attempts left: {attempts}")

    typing("\n💀 SYSTEM LOCKED")
    typing(f"Correct Code was: {secret_code}")

if __name__ == "__main__":
    start_game()
