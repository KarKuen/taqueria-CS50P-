def main():
    total = 0
    while True:
        try:
            orders = input('Item: ')
            orderlist = orders.split(' ')
            orderword = []
            for words in orderlist:
                orderword.append(words.lower().capitalize())
            orders = ' '.join(orderword)
            total = total + order(orders)
            cost = '$' + str('%.2f' % total)
            print('Total:', cost)
        except EOFError:
            print()
            break
        except TypeError:
            pass

def order(orders):
    felipes = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    if orders in felipes:
        total = felipes[orders]
        return(total)

main()