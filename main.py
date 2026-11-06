
class BankAccount:

  bank_name = "Global Tech Bank"
  total_accounts = 0
  interest_rate = 3.5 
  
  def __init__(self, account_holder, account_number, balance):
    self.account_holder = account_holder
    self.account_number = account_number
    self.balance = float(balance)

  @staticmethod
  def validate_amount(amount):
    if amount > 0:
      return True
    else:
      return False
      
  def deposit(self, amount):
    
    if BankAccount.validate_amount(self.amount):
      self.balance += self.amount
      print("Amount added successfully!")
    else:
      print("Invalid amount!")
    
      
  def 








