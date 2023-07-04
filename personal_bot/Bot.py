from AddressBook import AddressBook
from info import Name, Phone, Birthday, Email, Status, Note, Record
import pickle
import datetime
from abc import ABC, abstractmethod


class DefaultBot(ABC):

    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_commands(self):
        pass


class Bot(DefaultBot):
    def __init__(self):
        self.book = AddressBook()

    def display_contacts(self, contacts):
        print(contacts)
    
    
    def display_commands(self):
        print('Commands:')
        print('- add')
        print('- search')
        print('- edit')
        print('- remove')
        print('- save')
        print('- load')
        print('- congratulate')
        print('- view')
        print('- help')
        print('- exit')

    def handle(self, action):
        if action == 'add':
            name = Name(input("Name: ")).value.strip()
            phones = Phone().value
            birth = Birthday().value
            email = Email().value.strip()
            status = Status().value.strip()
            note = Note(input("Note: ")).value
            record = Record(name, phones, birth, email, status, note)
            return self.book.add(record)
        elif action == 'search':
            print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
            category = input('Search category: ')
            pattern = input('Search pattern: ')
            result = (self.book.search(pattern, category))
            for account in result:
                if account['birthday']:
                    birth = account['birthday'].strftime("%d/%m/%Y")
                    result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                    print(result)
        elif action == 'edit':
            contact_name = input('Contact name: ')
            parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
            new_value = input("New Value: ")
            return self.book.edit(contact_name, parameter, new_value)
        elif action == 'remove':
            pattern = input("Remove (contact name or phone): ")
            return self.book.remove(pattern)
        elif action == 'save':
            file_name = input("File name: ")
            return self.book.save(file_name)
        elif action == 'load':
            file_name = input("File name: ")
            return self.book.load(file_name)
        elif action == 'congratulate':
            print(self.book.congratulate())
        elif action == 'view':
            self.display_contacts(self.book)
        elif action == 'help':
            self.display_commands()
        elif action == 'exit':
            print('Good bye!')
            return 'exit'
        else:
            print("There is no such command!")


if __name__ == '__main__':
    bot = Bot()
    print('Use command [help] for more information about commands.')

    while True:
        user = bot.handle(input('Enter command: ').lower())

        if user == 'exit':
            break
