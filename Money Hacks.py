import time
balance = 0
money = "$1.00 has been given to your PayPall account!"
while True:
    time.sleep(0.1)
    print(money)
    print("Your current balance is:")
    balance = balance + 1
    print("$",balance)
