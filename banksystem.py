# Class for acc_type table
class AccType:
    def __init__(self, type_id, type_name):
        """Initialize acc type with type_id and type_name."""
        self.type_id = type_id
        self.type_name = type_name

    def __str__(self) -> str:
        return f"AccType(type_id={self.type_id}, type_name='{self.type_name}')"

# Class for account table
class Account:
    def __init__(self, account_no, balance,  acc_type, bank_id,):
        """Initialize account with id, account_no, balance , acc_type , and bank_id."""
        self.account_no = account_no
        self.balance = balance
        self.acc_type = acc_type
        self.bank_id = bank_id

    def __str__(self) -> str:
        return f"Account(account_no={self.account_no}, balance='{self.balance}', acc_type={self.acc_type}, bank_id={self.bank_id})"

# Class for account_customer table
class AccountCustomer:
    def __init__(self,  account_no, custid):
        """Initialize account customer with account_no, and custid."""
    
        self.account_no = account_no
        self.custid = custid

    def __str__(self) -> str:
        return f"AccountCustomer( account_no={self.account_no}, custid={self.custid})"

# Class for avail table
class Avail:
    def __init__(self, avail_id, loan_id, custid):
        """Initialize avail with avail_id , loan_id , and custid."""
        self.avail_id= avail_id
        self.loan_id = loan_id
        self.custid = custid

    def __str__(self) -> str:
        return f"Avail(avail_id={self.avail_id}, loan_id='{self.loan_id}', custid={self.custid})"

# Class for bank table
class Bank:
    def __init__(self, bank_id, name, code, address):
        """Initialize bank with bank_id , name , code, and address."""
        self.bank_id = bank_id
        self.name = name
        self.code = code
        self.address = address

    def __str__(self)-> str:
        return f"Bank(bank_id={self.bank_id}, name='{self.name}', code={self.code}, address={self.address})"

# Class for customer table
class Customer:
    def __init__(self, custid, name, address, phone):
        """Initialize customer with custid, name, address, and phone."""
        self.custid = custid
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self)-> str:
        return f"Customer(custid={self.custid}, name='{self.name}', address='{self.address}', phone={self.phone})"

# Class for loan table
class Loan:
    def __init__(self, loan_id, amount, interest_rate, loan_type):
        """Initialize loan with loan_id, amount, interest_rate, and loan_type."""
        self.loan_id = loan_id
        self.amount = amount
        self.interest_rate = interest_rate
        self.loan_type = loan_type

    def __str__(self)-> str:
        return f"Loan(loan_id={self.loan_id}, amount={self.amount}, interest_rate='{self.interest_rate}', loan_type={self.loan_type})"

# Class for loan_interest table
class LoanInterest:
    def __init__(self, loan_type_name, interest_rate):
        """Initialize loan interest with loan_type_name  and interest_rate."""
        self.loan_type_name = loan_type_name
        self.interest_rate = interest_rate

    def __str__(self)-> str:
        return f"LoanInterest( loan_type_name={self.loan_type_name}, interest_rate={self.interest_rate})"

# Class for offer table
class Offer:
    def __init__(self, offer_id, loan_id, offer_percentage, offer_description, bank_id):
        """Initialize offer with offer_id, loan_id, offer_percentage, offer_description, and bank_id."""
        self.offer_id = offer_id
        self.loan_id = loan_id
        self.offer_percentage = offer_percentage
        self.offer_description = offer_description
        self.bank_id = bank_id


    def __str__(self)-> str:
        return f"Offer(offer_id={self.offer_id}, loan_id='{self.loan_id}', offer_percentage={self.offer_percentage}, offer_description={self.offer_description}, bank_id={self.bank_id})"

# Class for payment table
class Payment:
    def __init__(self, payment_id, loan_id, payment_amount, payment_date):
        """Initialize payment with payment_id, loan_id, paymnet_amount, and payment_date."""
        self.payment_id = payment_id
        self.loan_id = loan_id
        self.payment_amount = payment_amount
        self.payment_date = payment_date

    def __str__(self)-> str:
        return f"Payment(payment_id={self.payment_id},loan_id={self.loan_id}, payment_amount={self.payment_amount},payment_date={self.payment_date})"

# Class for repayment table
class Repayment:
    def __init__(self, repayment_id, customer_id, loan_id, repayment_amount, repayment_date):
        """Initialize repayment with repayment_id, customer_id, loan_id, repayment_amount, and repaymnet_date."""
        self.repayment_id = repayment_id
        self.customer_id = customer_id
        self.loan_id = loan_id
        self.repayment_amount = repayment_amount
        self.repayment_date = repayment_date

    def __str__(self)-> str:
        return f"Repayment(repayment_id={self.repayment_id}, customer_id={self.customer_id}, loan_id={self.loan_id}, repayment_amount={self.repayment_amount}, repayment_date={self.repayment_date})"

# Class for transaction table
class Transaction:
    def __init__(self, transaction_id, customer_id, account_id, amount, transaction_date, transaction_type):
        """Initialize transaction with id, transaction_date, and transaction_amount."""
        self.transaction_id = transaction_id
        self.customer_id = customer_id
        self.account_id = account_id
        self.amount = amount
        self.transaction_date = transaction_date
        self.transaction_type = transaction_type

    def __str__(self)-> str:
        return f"Transaction(transaction_id={self.transaction_id}, customer_id={self.customer_id}, account_id={self.account_id}, amount={self.amount}, transaction_date={self.transaction_date}, transaction_type={self.transaction_type})"
