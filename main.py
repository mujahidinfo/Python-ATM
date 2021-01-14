import time

print("Please insert your CARD number")

time.sleep(5)

password = 1234

balance = 5000

pin = int(input("Enter your PIN: "))
if pin == password:
    while True:
        print("""
                1 == balance
                2 == Withdraw Balance
                3 == Diposit Amount
                4 == Exit
                """)
        try:
            option = int(input("Please Enter Your Option: "))
        except:
            print("Please Enter Valid Option")

        if option == 1:
            print(f"Your Current Balance is: {balance}")
        if option == 2:
            withdraw_amount = int(input("Please Enter Your Withdraw Amount: "))
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is dabited from your balance Successfully")
            print(f"Your Current Balance is {balance}")
        if option == 3:
            diposit_amount = int(input("Please Enter Your Deposit Amount: "))
            balance = diposit_amount + balance
            print(f"{diposit_amount} is Deposit your account Successfully")
            print(f"Your Current Balance is {balance}")
        if option == 4:
            print("Thank you for your transection. Wish you have a good day")
            break
else:
    print("Pin did not match. Please try again")
