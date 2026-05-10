class BankAccount:
    
    def __init__(self, name, pin, balance=0):
        

        self.name = name
    
        self.pin =pin 
        
        self.balance = balance
        
        self.history = [ ]
        
    def deposite(self, amount):
        
        self.balance += amount
        
        self. history.append(f"Deposited ${amount}")
        
        print(f'${amount} deposited! New balance: ${self.balance}') 
              
    def withdraw(self, amount):
    
        if amount <= self.balance:
        
            self.balance -= amount
            
            self.history.append(f'Withdrew ${amount}')
            
            print(f'${amount} withdraw! New balance: ${self.balance}')
            
        else:
            
            
            print('insufficient  balance!')
            
    def show_balance(self):
        print(f'Account Holder:  {self.name}, Balance: ${self.balance}') 
        
        
    def show_history(self):
        
        print('\n---Transaction History ---')
        
        for t in self.history:
            
            print(t) if  self.history else print ('No transactions yet!')
            
name = input('Enter your name: ')

pin = input('Set up 4-digit PIN: ')
        
account = BankAccount(name, pin)

if  input("Enter PIN to login: ") != account.pin:
    
    print('Wrong PIN! Access Denied.')
    
    exit()
        
while True: 
    print('\n1.Deposit 2.Withdraw 3.Show Balance 4.History 5.Exit')

    choice = input('choice:  ')
      
    if choice == '1':
        
        account.deposite(int(input('Enter amount: ')))
                 
    elif choice == '2':
        
        account.withdraw(int(input('Enter amount: ')))    
    
    elif choice == '3':
        
        account.show_balance()
        
    elif choice == '4':
        
        account.show_history()
        
    elif choice =='5':
        print('Goodbye!')
        
        break

    else:
        
        print('Invalid choice!')
        
        