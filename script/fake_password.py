import time
import random
import string
import sys

def type_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_hack(target):
    chars = string.ascii_letters + string.digits
    result = ""

    type_effect("\n🔍 Initializing brute force attack...")
    time.sleep(1)
    type_effect("🧠 Bypassing security layers...")
    time.sleep(1)
    type_effect("💻 Accessing encrypted data...\n")
    time.sleep(1)

    for letter in target:
        for char in chars:
            sys.stdout.write("\r🔑 Trying: " + result + char)
            sys.stdout.flush()
            time.sleep(0.02)
            if char == letter:
                result += char
                break

    print("\n\n✅ Password Cracked Successfully!")
    type_effect(f"🎉 Password is: {result}", 0.05)


# ========== RUN ==========
print("==== 🔐 SECRET PASSWORD SYSTEM ====")
user_password = input("Enter your secret password: ")

fake_hack(user_password)
