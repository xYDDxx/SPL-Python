class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} € wurden eingezahlt.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} € wurden abgehoben.")
        else:
            print("Nicht genügend Guthaben.")

    def check_balance(self):
        print(f"Ihr Kontostand beträgt: {self.balance} €")


def main():
    account = BankAccount()

    while True:
        print("\nBankautomat")
        print("1. Einzahlen")
        print("2. Abheben")
        print("3. Kontostand")
        print("4. Beenden")

        choice = input("Bitte wählen Sie eine Option: ")

        if choice == '1':
            amount = float(input("Geben Sie den Einzahlungsbetrag ein: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Geben Sie den Abhebungsbetrag ein: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Vielen Dank, dass Sie unseren Bankautomaten benutzt haben.")
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine der aufgeführten Optionen.")


if __name__ == "__main__":
    main()
