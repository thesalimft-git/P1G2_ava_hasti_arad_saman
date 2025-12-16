from datetime import datetime

class BankSystem:
    def __init__(self, accounts):
        self.accounts = accounts
    
    def is_number(self, x:str | float) -> bool:
        if type(x) == float or type(x) == int:
            return True
        if type(x) == str:
            try:
                x = float(x)
                return True
            except:
                return False
        return False
        
    def create_account(self, name:str, amount:str|float|int): 
        if self.is_number(amount):
            amount = float(amount)
        else:
            return 'error: amount must be a number'
        
        if not name.isalpha():
            return 'error: name must be at least 3 character'
        
        id = len(self.accounts) + 1
        action_time = datetime.now().strftime('%d %b at %H:%M')
        self.accounts[str(id)] = {
                                'name': name, 
                                'balance': amount, 
                                'history': [
                                    f'Created with ${amount} on {action_time}, balance = ${amount}',
                                ]
                            }
        return 'account created successfully'
    
    def deposit(self, id:str, amount:str|float|int):
        if self.is_number(amount):
            amount = float(amount)
        else:
            return 'error: amount must be a number'
        
        if id not in self.accounts:
            return 'error: id does not exist'
        
        self.accounts[id]['balance'] += amount
        action_time = datetime.now().strftime('%d %b at %H:%M')
        self.accounts[id]['history'].append(f'deposit with ${amount} on {action_time}, balance = ${self.accounts[id]['balance']}')
        return 'deposit successfully' 
        
    def withdraw(self, id:str, amount:float):
        if id not in self.accounts:
            return False
        
        if amount > self.accounts[id]['balance']:
            return 'error: balance is not enough'
        
        self.accounts[id]['balance'] -= amount
        action_time = datetime.now().strftime('%d %b at %H:%M')
        self.accounts[id]['history'].append(f'withdraw with ${amount} on {action_time}, balance = ${self.accounts[id]['balance']}')
        return True
    
 
    def transfer(self, id_from:str, id_to:str, amount:float):
        self.deposit(id_to, amount)
        self.withdraw(id_from, amount)
    
    def show_info(self):
        for id in self.accounts:
            print(f"{id}- {self.accounts[id]['name']} ({self.accounts[id]['balance']})")
    
    def echo_history(self, id: str):
        if id not in self.accounts:
            return False
        
        print(f"{id}- {self.accounts[id]['name']} ({self.accounts[id]['balance']})")
        for item in self.accounts[id]['history']:
            print(f"\t- {item}")
        
        return True