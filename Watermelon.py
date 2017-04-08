# WaterMelon


def buy(cash, item_name, item_num):
    if cash >= item_num * 1:  # everything costs 1 dollar
        cash -= item_num * 1
    else:
        print("Hey, you don't have enough money to buy %s" % item_name)
    return cash


amy_cash = float(input('How much cash do you have: '))  # your money at the beginning
see_item = input('What do you see: ')
if see_item == 'Tomato' or see_item == 'tomato':
    amy_cash = buy(amy_cash, 'Watermelon', 2)
else:
    amy_cash = buy(amy_cash, 'Watermelon', 1)

print('You have $' + str(amy_cash) + ' left :)\nBye!')