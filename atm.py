name = input('Enter your name: ')
print('Hello ',name)
message = """
How may i help you sir.

Please select any of them option,
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAW.
"""
print(message)
task = int(input('\nPlease enter your option: '))
available_amount = 5000
if task >= 1 and task <=3:
    print('\nWelcome to you in virtual bank program.')

    if task == 1:
        print('Your available amount is: ',available_amount,'INR')
    
    elif task == 2:
        deposit_amount = int(input('Please enter deposit amount: '))
        if deposit_amount > 0:
            available_amount += deposit_amount
            print('\nYou have successfully deposited your amount: ',deposit_amount)
            print('Your available amount is: ',available_amount,'INR')
        else:
            print('Please enter valid amount!')
    
    else:
        withdraw_amount = int(input('Please enter your withdraw amount: '))
        if withdraw_amount <= available_amount:
            available_amount -= withdraw_amount
            print('\nYou have successfully withdraw your amount: ',withdraw_amount)
            print('Your available amount is: ',available_amount,'INR')
        else:
            print("you don't have sufficient amount in your account!")
            print('Your available amount is: ',available_amount,'INR')
else:
    print('Please choose a correct option.')