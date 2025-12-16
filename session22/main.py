from service import show_menu
from bank_system import BankSystem

accounts = dict()
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
            bs.create_account(name, amount)
            
    
    

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