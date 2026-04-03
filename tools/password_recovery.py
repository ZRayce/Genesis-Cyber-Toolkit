import itertools

CHAR_MAP = {
    "letter": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digit": "0123456789",
    "special": "!@#$%^&*"
}


def generate_from_pattern(pattern, limit=30):
    pools = []

    for p in pattern:
        if p in CHAR_MAP:
            pools.append(CHAR_MAP[p])
        else:
            pools.append(p)

    results = []

    for combo in itertools.product(*pools):
        results.append(''.join(combo))

        if len(results) >= limit:
            break

    return results


# =========================
# AKINATOR FLOW (SAFE GAME MODE)
# =========================
def akinator_mode():
    print("\n🧠 Password Pattern Intelligence (Akinator Mode)\n")

    # Step 1: Base
    base = input("1️⃣ Does it start with a word? (type it or leave blank): ").strip()

    # Step 2: Numbers
    try:
        has_numbers = input("2️⃣ Does it include numbers? (y/n): ").strip().lower()
        digit_count = int(input("How many digits? (0-4): ") or 0) if has_numbers == "y" else 0
    except:
        digit_count = 0

    # Step 3: Letters
    try:
        extra_letters = int(input("3️⃣ Extra unknown letters? (0-3): ") or 0)
    except:
        extra_letters = 0

    # Step 4: Special chars
    try:
        special = input("4️⃣ Any special characters? (y/n): ").strip().lower()
        special_count = int(input("How many? (0-2): ") or 0) if special == "y" else 0
    except:
        special_count = 0

    # Build pattern
    pattern = []

    if base:
        pattern.extend(list(base))

    pattern += ["digit"] * digit_count
    pattern += ["letter"] * extra_letters
    pattern += ["special"] * special_count

    print("\n🔍 Interpreted Pattern:", pattern)

    results = generate_from_pattern(pattern)

    print("\n🔥 Generated Possibilities (Simulation Only):\n")

    for i, r in enumerate(results, 1):
        print(f"{i}. {r}")

    print("\n✔ This is a pattern simulation, not password recovery\n")