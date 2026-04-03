from tools.password_checker import check_password
from tools.password_recovery import generate_from_pattern, akinator_mode


def main():
    while True:
        print("\n================================")
        print("   Genesis Cyber Toolkit")
        print("================================\n")

        print("1. Password Strength Checker")
        print("2. Password Pattern Generator")
        print("3. Akinator Pattern Mode")
        print("4. Exit\n")

        choice = input("Enter choice: ").strip()

        # =========================
        # CHECKER
        # =========================
        if choice == "1":
            while True:
                pw = input("\nEnter password (or 'back'): ").strip()

                if pw.lower() == "back":
                    break

                print("\nResult:", check_password(pw))

        # =========================
        # BASIC PATTERN GENERATOR
        # =========================
        elif choice == "2":
            while True:
                pattern = input("\nEnter pattern (or 'back'): ").strip()

                if pattern.lower() == "back":
                    break

                results = generate_from_pattern(pattern, 30)

                print("\n🔥 Generated Examples:\n")
                for i, r in enumerate(results, 1):
                    print(f"{i}. {r}")

        # =========================
        # AKINATOR MODE
        # =========================
        elif choice == "3":
            akinator_mode()

        # =========================
        # EXIT
        # =========================
        elif choice == "4":
            print("\nGoodbye 👋")
            break

        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()