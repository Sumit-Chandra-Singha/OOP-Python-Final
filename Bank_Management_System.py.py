
class Bank:
    def __init__(self,name,balance) -> None:
        self.name = name
        self.__total_balance = balance
        self.is_loan_active = True
        self.total_loan = 0

    @property
    def get_balance(self):
        return self.__total_balance
    
    @get_balance.setter
    def get_balance(self,amount):
        if amount[0]<0:
            return 'Amount cannot be negative'
        if amount[1]=='+':
            self.__total_balance += amount[0]
        else:
            self.__total_balance -= amount[0]



class Account:
    users = []
    admins = []

    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address  = address

class User(Account):
    
    def __init__(self, name, email, address, account_type) -> None:
        super().__init__(name, email, address)
        self.account_type = account_type
        self.account_number = name+address
        self.balance = 0
        self.deposited = 0
        self.loan = 0
        self.history = []
        Account.users.append(self)

    def deposit(self, amount):
        if amount <= 0:
            print("\nAmount Must Be Positive..")
            return
        self.balance += amount
        self.deposited += amount
        bank.get_balance = (amount,'+')
        self.history.append(f"Deposited Ammount {amount}.")
        print(f'\nAmount {amount} Taka Successful Deposited !!')

    def withdraw(self, amount):
        if bank.get_balance < amount:
            print('\nThe Bank is bankrupt !!!')
            return
        if amount > self.balance:
            print('\nWithdrawal amount exceded!')
            return
        
        self.balance -= amount
        bank.get_balance = (amount,'-')
        self.history.append(f"Withdrawn Ammount {amount}.")
        print(f'\nAmount {amount} Taka Successfully Withdrawn !!')

    def check_bank_balance(self):
        print(f"\n  Your Balance Is {self.balance} Taka..")  
        print(f"-> Deposited - {self.deposited}")  
        print(f"-> Loan - {self.balance - self.deposited}")  

    def check_history(self):
        if self.history == None:
            print('\nNo History Found.')
            return
        print()
        for data in self.history:
            print('-> ',data)

    def take_loan(self, amount):
        if bank.is_loan_active==False:
            print('\n  Loan Feature is Inactive !')
            return
        if self.loan >= 2 :
            print('\n  Loan limit exceded !')
            return
        if amount > bank.get_balance:
            print('\n  Insufficient Bank Balance !')
            return
        self.balance += amount
        bank.get_balance = (amount,'-')
        bank.total_loan += amount
        self.loan += 1
        self.history.append(f"Took Loan Ammount {amount}.")
        print('\n  Congratulations ! Loan Granted...')
        
    def transaction(self, amount, user2):
        if amount <= 0:
            print('\nAmount must be positive..')
            return
        if user2 == self.name:
            print('\nReceiver cannot be the Sender..')
            return
        for user in Account.users:
            if user.name == user2:
                self.balance -= amount
                user.balance += amount
                self.history.append(f"Ammount {amount} transfered to {user.name}.")
                user.history.append(f"Ammount {amount} received from {self.name}.")
                print(f"\nAmmount {amount} transfered to {user.name}.")
                return
        print('\nAccount does not exist !')

class Admin(Account):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)
        Account.admins.append(self)

    def create_account(self):
        name=input("Name : ")
        email=input("Email : ")
        address=input("Address : ")
        account_type=input("Account Type : \n\t1.Savings\n\t2.Current\n  : ")
        if account_type==1:
            currentUser=User(name,email,address,'Savings')
        else:
            currentUser=User(name,email,address,'Current')

        print('\n\tAccount Created !!')
        
    def delete_account(self,user):
        for account in Account.users:
            if account.name == user:
                Account.users.remove(account)
                print("\n\tAccount Deleted !")
                return 
        print('\n\tNo Account Available.')
                 
    def see_accounts(self):
        # print('\n  Username   Email   Address\n')
        for account in Account.users:
            print(f"\nUsername : {account.name}, Email : {account.email}, Address : {account.address},\n Type : {account.account_type}, AccountNum : {account.account_number}.")

    def check_bank_balance(self):
        print(f"\n\t---{bank.name} Bank---\n\nBalance : {bank.get_balance} Taka")

    def check_loan(self):
        print(f"\n\t---{bank.name} Bank---\n\nTotal Loan : {bank.total_loan} Taka")

    def turn_on_loan(self):
        bank.is_loan_active = True
        print('\nLoan Feature Is Turned On')

    def turn_off_loan(self):
        bank.is_loan_active = False
        print('\nLoan Feature Is Turned Off')

bank = Bank('Gorib',100000)

admin = Admin('admin','admin.mail','@admin')
user = User('user','user.mail','@user','Savings')
user2 = User('user2','user2.mail','@user2','Current')
currentUser = None

while True:

    if currentUser == None:
        print('\n 1. Login\n 2. Register\n 3. Exit.')
        opt=int(input("\nEnter Option : "))

        if opt == 1:
            user =input("User Name : ")

            for account in Account.users:
                if account.name==user:
                    currentUser=account
                    break
            for account in Account.admins:
                if account.name==user:
                    currentUser=account
                    break
            if currentUser == None:
                print('\n\tNo User Available.')
            else:
                print(f"\n\tWelcome {currentUser.name} !!")

        elif opt ==2 :
            while(True):
                print('\n  1. Admin\n  2. User\n  3. Exit.\n')
                type =int(input("Choose Type: "))
                if type == 1:
                    name=input("\nName : ")
                    email=input("Email : ")
                    address=input("Address : ")
                    currentUser=Admin(name,email,address)
                    break

                elif type == 2:
                    name=input("\nName : ")
                    email=input("Email : ")
                    address=input("Address : ")
                    account_type=input("Account Type : \n\t1.Savings\n\t2.Current\n  : ")
                    if account_type==1:
                        currentUser=User(name,email,address,'Savings')
                    else:
                        currentUser=User(name,email,address,'Current')
                    print(f"\nWelcome {currentUser.name} !!")
                    break

                elif type == 3:
                    break
                else:
                    print('\nInvalid Option.\nChoose Again.')

        elif opt == 3:
            break    

        else:
            print('\nInvalid Option.\nChoose Again.')


    if currentUser in Account.admins:
        print('\n1. CREATE ACCOUNT.')
        print('2. DELETE ACCOUNT.')
        print('3. SEE ALL ACCOUNTS.')
        print('4. CHECK BANK BALANCE.')
        print('5. CHECK LOAN AMOUNT.')
        print('6. TURN OFF LOAN.')
        print('7. TURN ON LOAN.')
        print('8. LOGOUT.')
        option = int(input('\nENTER OPTION: '))

        if option == 1:
            currentUser.create_account()   
        elif option == 2:
            user = input("ENTER USERNAME: ")
            currentUser.delete_account(user)
        elif option == 3:
            currentUser.see_accounts()
        elif option == 4:
            currentUser.check_bank_balance()
        elif option == 5:
            currentUser.check_loan()
        elif option == 6:
            if bank.is_loan_active:
                currentUser.turn_off_loan()
            else:
                print('\nLoan Feature Is Already Inactive..')
        elif option == 7:
            if bank.is_loan_active==False:
                currentUser.turn_on_loan()
            else:
                print('\nLoan Feature Is Already Active..')
        elif option == 8:
            currentUser = None
        else:
            print('\nInvalid Option.\nChoose Again.')



    elif currentUser in Account.users:
        print('\n1. DEPOSIT.')
        print('2. WITHDRAW.')
        print('3. CHECK BALANCE.')
        print('4. CHECK HISTORY.')
        print('5. TAKE LOAN.')
        print('6. TRANSFER MONEY.')
        print('7. LOGOUT.')
        option = int(input('\nENTER OPTION : '))

        if option == 1:
            amount = int(input("\nENTER AMOUNT : "))
            currentUser.deposit(amount)
        elif option == 2:
            amount = int(input("\nENTER AMOUNT : "))
            currentUser.withdraw(amount)
        elif option == 3:
            currentUser.check_bank_balance()
        elif option == 4:
            currentUser.check_history()

        elif option == 5:
            amount = int(input("\nENTER LOAN AMOUNT : "))
            currentUser.take_loan(amount)
            
        elif option == 6:
            amount = int(input("\nENTER AMOUNT : "))
            user2 = input("\nENTER RECEIVER NAME : ")
            currentUser.transaction(amount,user2)
        elif option == 7:
            currentUser = None
        
        else:
            print('\nInvalid Option.\nChoose Again.')

