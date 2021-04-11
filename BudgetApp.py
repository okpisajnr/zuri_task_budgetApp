print("ABout My Budget App\n Please kindly create an instance of the Budget class to explore the App")
class Budget:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_details(self):
        print("Budget App")
        print("Name :", self.name)
        AcctNo = id(self.name)
        print("Acct No :", AcctNo)
        print("Available Balance : #" ,self.balance)
        print("\n")

    def deposit(self, amt):
        self.amt = amt
        self.balance = self.balance + amt
        print("#",self.amt , "has been deposited")
        print("New Account Balance has been Updated #", self.balance)
    
    def withdrawl(self, amt):
        self.amt = amt
        if(self.amt > self.balance):
            print("Insufficent Balance #", self.balance)
        else:
            self.balance = self.balance - self.amt
            print("Withdrawl successful")
            print("Account Balance has been Updated #", self.balance)

    def view_balance(self):
        self.show_details()
 
    def transfer(self, amt, category):
        self.amt = amt
        self.category = category
        print(f"{self.amt}  Transfered successfully to {self.category} {self.name} \'s Account")
        self.balance = self.balance - self.amt
        print("Account Balance After The Transfer is #", self.balance)


 
