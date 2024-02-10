from collections import UserDict

endings = ['good bye!', 'close', 'exit', '.'] 
def end():
    print('Good bye!')

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print('Nie znaleziono podanego kontaktu, wprowadź kontakt poprawnie lub dodaj nowy')
            return
        except ValueError:
            print('Telefon musi składać się z samych cyfr')
            return
        except IndexError:
            print('Nie istnieje kontakt o podanym indeksie')
            return
    return wrapper

class AddressBook(UserDict):
    @input_error
    def search(self, arg):
        print(f' Numer(y) do {arg.name.value}: {self.data[arg.name.value]}')
    @input_error
    def add_record(self, arg):
        if arg.name.value in self.data:
            self.data[arg.name.value].append(arg.phone.value)
        else:
            self.data[arg.name.value] = [arg.phone.value]
        print(self.data)
    

contacts_c = AddressBook()

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        
class Phone(Field):
    def __init__(self, value=None):
        super().__init__(value)

class Record:
    def __init__(self, name, phone=None):
        self.name = name.value
        if phone != None:
            self.phone = phone.value
        else:
            self.phone = []
    def add_phone(self, arg):
        self.phone.append(arg.value)
        print(self.phone)
    @input_error
    def change_phone(self, arg):
        self.phone = arg.phone.value
        contacts_c.data[arg.name.value] = self.phone
    @input_error
    def remove_phone(self, phone):
        contacts_c[self.name.value].remove(phone.value)
        

def main():
    start = input('Write "hello" to start the bot: ')
    if start.lower() == 'hello':
        rec = None
        print('bot started')
        while True:
            command_raw = input('How can i help you?: ')
            command_lower = command_raw.lower()
            if command_lower.startswith('dodaj'):
                rec = Record(Name(Field(command_raw.split(' ')[1])), Phone(Field(command_raw.split(' ')[2])))
                contacts_c.add_record(rec)
                pass
            elif command_lower.startswith('zmień'):
                rec = Record(Name(Field(command_raw.split(' ')[1])), Phone(Field(command_raw.split(' ')[2])))
                rec.change_phone(rec)
                pass
            elif command_lower.startswith('phone'):
                rec = Record(Name(Field(command_raw.split(' ')[1])))
                contacts_c.search(rec)
            elif command_lower.startswith('usuń kontakt'):
                rec = Record(Name(Field(command_raw.split(' ')[2])))
                contacts_c.data.pop(rec.name.value)
            elif command_lower.startswith('usuń telefon'):
                contact_name = command_raw.split(' ')[2]
                phone_number = command_raw.split(' ')[3]
                rec = Record(Name(Field(contact_name)))
                rec.remove_phone(Phone(Field(phone_number).value))
            elif command_lower == 'pokaż':
                print(contacts_c)
                pass
            elif command_lower in endings:
                print('bot stopped')
                end()
                break
            else:
                print('Nie znam takiej komendy', command_raw)
                pass


if __name__ == '__main__':
    main()