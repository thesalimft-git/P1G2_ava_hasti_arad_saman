import random
win_card = { 'r': 'p', 'p': 's', 's': 'r' }
while True:
    pc_choice = random.choice([ item for item in win_card ])
    h_choice = input('select r/p/s: ')

    if h_choice == 'end':
        break
    elif h_choice not in win_card:
        print('not valid')
        continue
    elif h_choice == pc_choice:
        print('same, try again')
        continue
    elif h_choice == win_card.get(pc_choice):
        print('win')
    else:
        print('loss')