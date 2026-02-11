import math
import string
import re

def calculate_entropy(password):
    pool = 0

    if re.search(r"[a-z]", password):
        pool += 26
    if re.search(r"[A-Z]", password):
        pool += 26
    if re.search(r"[0-9]", password):
        pool += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        pool += 32

    entropy = len(password) * math.log2(pool) if pool else 0
    return entropy

def estimate_crack_time(entropy):
    guesses_per_second = 1_000_000_000  # 1 billion guesses/sec (GPU attack)

    total_combinations = 2 ** entropy
    seconds = total_combinations / guesses_per_second

    years = seconds / (60 * 60 * 24 * 365)
    return years

def password_strength(entropy):
    if entropy < 28:
        return "Very Weak 😢"
    elif entropy < 36:
        return "Weak ⚠"
    elif entropy < 60:
        return "Moderate 🙂"
    elif entropy < 128:
        return "Strong 💪"
    else:
        return "Very Strong 🔥"

def analyze_password(password):
    entropy = calculate_entropy(password)
    years = estimate_crack_time(entropy)
    strength = password_strength(entropy)

    print("\n🔎 PASSWORD ANALYSIS REPORT")
    print("-" * 40)
    print(f"Password Length: {len(password)}")
    print(f"Entropy: {round(entropy,2)} bits")
    print(f"Strength Level: {strength}")
    print(f"Estimated brute-force time: {round(years, 2)} years")
    print("-" * 40)

if __name__ == "__main__":
    print("🔐 AI Password Strength Analyzer")
    pwd = input("Enter your password: ")
    analyze_password(pwd)
