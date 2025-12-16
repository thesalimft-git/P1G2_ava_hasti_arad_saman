from datetime import datetime

class BankSystem:
    def __init__(self, accounts):
        self.accounts = accounts
    
    def create_account(self, name:str, amount:str):
        if not amount.isdigit():
            return False
        else:
            amount = float(amount)
            
        id = len(self.accounts) + 1
        action_time = datetime.now().strftime('%d %b at %H:%M')
        self.accounts[str(id)] = {
                                'name': name, 
                                'balance': amount, 
                                'history': [
                                    f'Created with ${amount} on {action_time}, balance = ${amount}',
                                ]
                            }
    
    def deposit(self, id:str, amount:float):
        if id not in self.accounts:
            return False
        
        self.accounts[id]['balance'] += amount
        action_time = datetime.now().strftime('%d %b at %H:%M')
        self.accounts[id]['history'].append(f'deposit with ${amount} on {action_time}, balance = ${self.accounts[id]['balance']}')
        return True 
        
    def withdraw(self, id:str, amount:float):
        if id not in self.accounts:
            return False
        
        if amount > self.accounts[id]['balance']:
            return False
        
        self.accounts[id]['balance'] -= amount
        action_time = datetime.now().strftime('%d %b at %H:%M')
        self.accounts[id]['history'].append(f'withdraw with ${amount} on {action_time}, balance = ${self.accounts[id]['balance']}')
        return True
    
    def transaction(self, id:str, amount:float):
        if id not in self.accounts:
            return False
            
        self.accounts[id]['balance'] += amount
        action_time = datetime.now().strftime('%d %b at %H:%M')
        self.accounts[id]['history'].append(f'{'Deposit' if amount > 0 else 'Withdraw'} with ${amount if amount > 0 else -amount} on {action_time}, balance = ${self.accounts[id]['balance']}')
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