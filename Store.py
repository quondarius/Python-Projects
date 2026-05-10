
class Store:
    def __init__(self):
        self.data = []

    def info(self):
        pin = input("Set up 4-digit PIN: ")

        login = input("Enter PIN to login: ")

        if login != pin:
            print("Wrong PIN. Access Denied.")
            exit()
        else:
            print("Access granted.")

    def total(self):
        price = float(input("Enter Price: $"))
        discount = float(input("Enter Discount as decimal, like 0.20 for 20%: "))

        discount_amount = price * discount
        final_price = price - discount_amount
        change = final_price - price

        self.data.append(f"Original price: ${price}")
        self.data.append(f"Discount amount: ${discount_amount}")
        self.data.append(f"Final price: ${final_price}")

        print(f"Original price: ${price:.2f}")
        print(f"Discount amount: ${discount_amount:.2f}")
        print(f"Final price: ${final_price:.2f}")
        print(f'Here goes Your change: {change}')


store = Store()
store.info()
store.total()