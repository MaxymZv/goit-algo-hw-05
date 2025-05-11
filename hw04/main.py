from functools import wraps

#Функція обробки помилок
def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs) 
        except IndexError:                             #В разі не правельного індексу
            return 'Please give me name and phone number!'
        except KeyError:                               #В разі не існуючого ключу словника
            return 'Ther is no such person in contacts!'
        except ValueError:                             #В разі не правильного значення
            return 'Give me name and phone number please'
    return inner




# Функція для парсингу введеного рядка
def parse_input(user_input):                           
    cmd, *args = user_input.split()                      #Розділяє введений користувачем рядок на команду та розпаковані аргументи
    cmd = cmd.lower().strip()                            #Перетворює команду на нижній регістр та видаляє пробіли
    return cmd, *args                                    #Повертає команду та аргументи


@input_error
# Функція додавання контактів
def add_contacts(args, contacts):
    name, phone = args                                   #Приймає як аргументи ім'я контакту та його номер
    contacts[name] = phone                               #Додає контакт до словника
    return 'Contact added!'                              #Повертає повідомлення про додавання контакту

@input_error
# Функція для зміни номера контакту
def change_contacts(args, contacts): 
    name, new_phone = args 
    if name not in contacts:                              #Перевіряє чи є в списку контактів ім'я
        raise KeyError                                    #Викликає KeyError
    contacts[name] = new_phone
    return f'Contact {name} changed to {new_phone}!'      #Повертає змінений контакт
 

@input_error
# Функція для відображення номеру контакту    
def show_phone(args, contacts): 
    name = args[0]                                       #Приймає як аргумент ім'я контакту
    return f'{name}: {contacts[name]}'                   #Повертає номер контакту
                  
    
# Функція для відображення всіх контактів
def show_all_contacts(contacts): 
    result = []                                          #Створює пустий список для зберігання контактів
    for name, phone in contacts.items() :
        result.append(f'{name}: {phone}')                #Додає контакти до списку
    return result                                        #Повертає список контактів


# Основна функція програми де реалізується логіка вище вказаних функції
def main():
    contacts = {}                                        #Створює пустий словник для зберігання контактів
    print('Welcome to assistant bot!')                   #Виводить привітальне повідомлення
    while True:                                          #Нескінченний цикл для очікування команди
        user_input = input('Enter command: ')
        command, *args = parse_input(user_input)

        if command in ['exit', 'close']:
            print('Goodbye!')
            break                                        #В разі команди exit або close виходить з нескінченного циклу та завершує роботу програми
        elif command == 'hello':
            print('How can i help you?')
        elif command == 'add':          
            print(add_contacts(args, contacts))
        elif command == 'all':
            print(f'All contacts: {show_all_contacts(contacts)}')
        elif command == 'change':
            print(change_contacts(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        else:                                             #В разі введення невірної команди виводить повідомлення про помилку
            print('Invalid command!') 

if __name__ == '__main__':                                
    main()

