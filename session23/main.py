from service import show_menu
from bank_system import BankSystem
from data_manager import DataManager

dm = DataManager()
accounts = dm.get()
bs = BankSystem(accounts)

def main():
    while True:
        show_menu()

        request = input('Select from Menu: ')
        
        if request == '1':
            bs.show_info()
            
        elif request == '2':
            id = input('id: ')
            bs.echo_history(id)
            
        elif request == '3':
            name = input('name: ')
            amount = input('amount: ')
            result = bs.create_account(name, amount)
            print(result)
            
        elif request == '4':
            id = input('id: ')
            amount = input('amount: ')
            result= bs.deposit(id, amount)
            print(result)
            
        elif request == '5':
            id = input('id: ')
            amount = input('amount: ')
            bs.withdraw(id, amount)
            
        elif request == '6':
            id_from = input('id from: ')
            id_to = input('id to: ')
            amount = input('amount: ')
            bs.transfer(id_from, id_to, amount)
            
        elif request == '7':
            dm.set(accounts)
            break
    
    

main()




# accounts = {
#     '1': {
#         'name': 'ali', 
#         'balance': 120, 
#         'history': [
#             'created with $120.0 on 27 Oct at 12:22, balance = 120 ',
#             'deposit with $30.0  balance = 220 ',
#         ]
#     }
# }