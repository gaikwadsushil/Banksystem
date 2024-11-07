import uuid
from banksystem import Account, Customer, Loan, Payment  

class BankSystem:
    def __init__(self):
        self.accounts = []
        self.customers = []
        self.loans = []
        self.payments = []
        self.transactions = []

    def add_account(self):
        account_no = uuid.uuid4()
        balance = float(input('Enter balance: '))
        acc_type = input('Enter account type: ')
        bank_id = input('Enter bank ID: ')
        account = Account(account_no, balance, acc_type, bank_id)
        self.accounts.append(account)
        print("Account created successfully!")

    def add_customer(self):
        custid = uuid.uuid4()
        name = input('Enter name: ')
        address = input('Enter address: ')
        phone = input('Enter phone: ')
        customer = Customer(custid, name, address, phone)
        self.customers.append(customer)
        print("Thank you for being our customer!")

    def add_loan(self):
        loan_id = uuid.uuid4()
        amount = float(input('Enter loan amount: '))
        interest_rate = float(input('Enter interest rate: '))
        loan_type = input('Enter loan type: ')
        loan = Loan(loan_id, amount, interest_rate, loan_type)
        loan.remaining_balance = amount  # Track remaining balance
        self.loans.append(loan)
        print("Loan processed successfully!")

    def add_payment(self):
        payment_id = uuid.uuid4()
        loan_id = input('Enter loan ID: ')
        payment_amount = float(input('Enter payment amount: '))
        payment_date = input('Enter payment date (YYYY-MM-DD): ')

        
        loan = next((loan for loan in self.loans if str(loan.loan_id) == loan_id), None)
        if loan:
            if payment_amount > loan.remaining_balance:
                print("Payment exceeds loan balance. Please enter a valid amount.")
                return

            loan.remaining_balance -= payment_amount  
            payment = Payment(payment_id, loan.loan_id, payment_amount, payment_date)
            self.payments.append(payment)
            print("Payment made successfully!")

            
            if loan.remaining_balance == 0:
                self.loans.remove(loan)
                print("Loan fully paid and removed from records.")
        else:
            print("Loan ID not found.")

    def print_all_accounts(self):
        for account in self.accounts:
            print(account)

    def print_all_customers(self):
        for customer in self.customers:
            print(customer)

    def print_all_loans(self):
        for loan in self.loans:
            print(f"Loan ID: {loan.loan_id}, Amount: {loan.amount}, Interest Rate: {loan.interest_rate}, Type: {loan.loan_type}, Remaining Balance: {loan.remaining_balance}")

    def print_all_payments(self):
        for payment in self.payments:
            print(payment)

    def start(self):
        stop = False
        while not stop:
            data = int(input('''
                If you want to add an account, press 1...
                If you want to add a customer, press 2...
                If you want to take a loan, press 3...
                If you want to make a payment, press 4...
                If you want to print all accounts, press 5...
                If you want to print all customers, press 6...
                If you want to print all loans, press 7...
                If you want to print all payments, press 8...
                If you want to exit, press 9...
            '''))

            if data == 1:
                self.add_account()
            elif data == 2:
                self.add_customer()
            elif data == 3:
                self.add_loan()
            elif data == 4:
                self.add_payment()
            elif data == 5:
                self.print_all_accounts()
            elif data == 6:
                self.print_all_customers()
            elif data == 7:
                self.print_all_loans()
            elif data == 8:
                self.print_all_payments()
            elif data == 9:
                stop = True
            else:
                print("Invalid input, please try again!")


system = BankSystem()
system.start()
