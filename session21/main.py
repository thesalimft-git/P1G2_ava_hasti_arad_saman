from bank_system import BankSystem
accounts = dict()

def main():
    bs = BankSystem(accounts)
    bs.create_account('ali', 100)
    bs.deposit('1', 100)

    print(accounts)
    
    

    

main()




# accounts = {
#     '1': {
#         'name': 'ali', 
#         'balance': 120, 
#         'history': [
#             'created with $120.0 on 27 Oct at 12:22, balance = 120 ',
#             'deposit with $100.0 on 27 Oct at 13:22, balance = 220 ',
#         ]
#     }
# }