account_balance = 5000

def spend(num):
    if num <= account_balance:
        return account_balance - num
    else:
        return "Недостатньо грошей на рахунку. Відмова."

def deposit(num):
    return account_balance + num

def check_balance():
    print("Ваш баланс: ", account_balance)

print("Вітаю в Пайтон Банкоматі!")
while True:
    print("\nОберіть функцію:")
    print("1. Зняти гроші")
    print("2. Покласти гроші")
    print("3. Перевірити баланс")
    print("4. Вийти")

    option = input()

    if option == "1":
        amount = float(input("Введіть суму яку ви хочете зняти: "))
        result = spend(amount)
        if type(result) == str:
            print(result)
        else:
            account_balance = result
            print("Транзакція успішна. Ваш новий баланс: ", result)
    elif option == "2":
        amount = float(input("Введіть суму яку ви хочете покласти:"))
        account_balance = deposit(amount)
        print("Транзакція успішна. Ваш новий баланс:", account_balance)
    elif option == "3":
        check_balance()
    elif option == "4":
        print("Дякую за використання нашого банкомату! До побачення")
        break
    else:
        print("Такої функції не існує. Спробуйте ще раз.")
