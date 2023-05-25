accounts = {
    "1111": 5000,
    "2222": 3000,
    "3333": 8000
}

def spend(card_num, amount):
    if card_num not in accounts:
        return "Недійсний номер карти. Спробуйте ще раз."
    
    if amount <= accounts[card_num]:
        accounts[card_num] -= amount
        return accounts[card_num]
    else:
        return "Недостатньо грошей на рахунку. Відмова."

def deposit(card_num, amount):
    if card_num not in accounts:
        return "Недійсний номер карти. Спробуйте ще раз."
    
    accounts[card_num] += amount
    return accounts[card_num]

def check_balance(card_num):
    if card_num not in accounts:
        return "Недійсний номер карти. Спробуйте ще раз."
    
    print("Ваш баланс: ", accounts[card_num])

def atm():
    print("Вітаю в Пайтон Банкоматі!")
    while True:
        card_num = input("Вставте вашу карту (введіть номер карти): ")
        if card_num in accounts:
            while True:
                print("\nОберіть функцію: ")
                print("1. Зняти гроші")
                print("2. Покласти гроші")
                print("3. Перевірити баланс")
                print("4. Вийти")

                option = input()

                if option == "1":
                    amount = float(input("Введіть суму яку ви хочете зняти: "))
                    result = spend(card_num, amount)
                    if type(result) == str:
                        print(result)
                    else:
                        print("Транзакція успішна. Ваш новий баланс: ", result)
                elif option == "2":
                    amount = float(input("Введіть суму яку ви хочете покласти: "))
                    print("Транзакція успішна. Ваш новий баланс: ", deposit(card_num, amount))
                elif option == "3":
                    check_balance(card_num)
                elif option == "4":
                    print("Дякую за використання нашого банкомату!")
                    break
                else:
                    print("Обраної функціі не існує. Спробуйте ще раз.")
        else:
            print("Недійсний номер карти. Спробуйте ще раз.")
            continue

atm()