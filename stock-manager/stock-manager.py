


stock = {'Chalk': '5 boxes', 'History Books': '3 units', 'Pens': '7 boxes', 'Rulers': '9 units'}
values = []
for value in stock.values():
    values = values + [value]

amounts = input()


def item_add():
    added_item = input('Write the name of the item that you wish to add:  ').capitalize()
    added_amount = input('Write amount of the item:  ').capitalize()
    stock[added_item] = added_amount
    print(f'"{added_item}" was added to your stock' )
    print(f'Here is your updated stock: {stock}')
    answer_add_more()
    
def answer_add_more():
    add_more = input('\nRemove an item: R \nAdd a new item: A \nQuit: Q ')
    if add_more in ['Q', 'q']:
        exit()
    elif add_more in ['R', 'r']:
        item_remove()
    elif add_more in ['R', 'r']:
        item_add()
    else:
        print('Please, check your spelling.') 
        item_add()
            
def item_remove():
    print(f'This is your current stock: {stock} \n')
    answer = (input('Which item do you want to remove? ')).capitalize()
    if answer in stock:
        del stock[answer]
        print(f'"{answer}" was removed from your stock.')
        print(f'Current stock: {stock}')
        answer_remove_more()
    else:
        print('Please, check your spelling')
             
def answer_remove_more():
    remove_more = input('\nRemove another item: R \nAdd a new item: A \nQuit: Q  ')
    if remove_more in ['Q', 'q']:
        exit()
    elif remove_more in ['R', 'r']:
        item_remove()
    elif remove_more in ['R', 'r']:
        item_add()
    else:
        print('Please, check your spelling.') 
        answer_remove_more()     
               
        
def main():
    print('* * ' * 36)       
    print(f'Here is the current stock: {stock}')
    print('Do you what to add anything to the stock? \n')
    question_add = input('"YES" or "NO":  ' )
    if question_add in ['NO', 'no', 'No']:
        print('Do you wish to remove an item from the stock?')
        question_remove = input('"YES" or "NO": ')
        if question_remove in ['NO', 'no', 'No']:
            print('Thank you. Until next time.')
            exit()
        elif question_remove in ['yes', 'Yes', 'YES']:
            item_remove()
        else:
            print('Please, check your spelling.')
                
    elif question_add in ['yes', 'Yes', 'YES']:
        item_add()
    else:
        print('Please, check your spelling.') 
    
main()
        


