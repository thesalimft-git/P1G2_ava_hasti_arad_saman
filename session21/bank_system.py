from datetime import datetime

class BankSystem:
    def __init__(self, accounts):
        self.accounts = accounts
    
    def create_account(self, name:str, amount:float):
        id = len(self.accounts) + 1
        action_time = datetime.now().strftime('%d %b at %H:%M')
        self.accounts[str(id)] = {
                                'name': name, 
                                'balance': amount, 
                                'history': [
                                    f'created with ${amount} on {action_time}, balance = ${amount}',
                                ]
                            }
    
    def deposit(self, id:str, amount:float):
        if id not in self.accounts:
            return False
        
        self.accounts[id]['balance'] += amount
        return True
        

      