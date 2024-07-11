class BankAccount:
  def __init__ (self, account_balance = 0) :
    self.account_balance = account_balance
  
  def deposit (self, amount) :
    self.amount = amount
    self.account_balance += self.amount


  
  def withdraw (self, amount) :
    self.amount = amount
    if self.amount > self.account_balance:
      return False
    else:
      self.account_balance -= self.amount
      return True
      
  
  def display_balance (self) :
    print(f"Current Balance: ${self.account_balance}")


