import os
cwd = os.getcwd()

message = input('Write something:\n')
initial_file_name = open('unamed.txt', 'w')
initial_file_name.write(message)


#lets the user name the
def save():    
    current_file_name = (input('Name your file:\n') + '.txt')
    if os.path.exists(current_file_name) == False:
        os.rename('unamed.txt', current_file_name)
    else:
        print(f'A file named "{current_file_name}" already exists in the current directory. \nPlease, try again.\n')
        save()


#prompts the user about leaving the program
def exit_program():
    exit_prompt = input('Your message has been written onto a file. \nPress "X" to quit or "S" to save \n')
    
    if exit_prompt in ["x", "X"]:
        confirmation_message = input('Are you sure that you want to exit without saving your changes? \nThis action is irreversible. \nType "X" to quit or any other key to save \n')
        if confirmation_message in ["x", "X", "s", "S"]:
            print('Goodbye.')
            exit()
        else:
            save()
            
    elif exit_prompt in ["s", "S"]:
        save()
    else:
        print('WRONG key. \nPlease, try again.\n')
        exit_program()



def main():
    exit_program()   
    
       
main()