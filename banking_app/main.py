import bankcore
import accounts

print("Welcome to ABC Bank")
while True:
    
     print("1. Create an account")
     print("2. Login to the account")
     print("3. Exit")

     choice = int(input("Enter choice:"))

     if choice == 1:
         
         name = input("Enter your name: ")
         password = input("Create password: ")
         bankcore.create_account(name, password)

     elif choice == 2:
         cid = input("Enter Customer ID: ")
         password = input("Enter Password: ")

         result= bankcore.login(cid, password)
        
       
           
         while True:
             
            print("\nBanking Menu")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Logout")

            option = int(input("Enter option: "))

            if option == 1:
                customer_id = input("Enter your id")
                accounts.check_balance(customer_id)
                
              
            elif option == 2:
                customer_id = input("Enter your id")
                amount = float(input("Enter amount to deposit: "))
                accounts.deposit(customer_id, amount)

            elif option == 3:
                customer_id = input("Enter your id")
                amount = float(input("Enter amount to withdraw: "))
                accounts.withdraw(customer_id, amount)

            elif option == 4:
                print("Logged out successfully")
                accounts.logout()
                break
     elif choice == 3:
        print("Exit")
        break


