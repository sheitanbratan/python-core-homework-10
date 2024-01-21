from collections import UserDict


class NumberNotFound(Exception):
    def __init__(self, message='Number not found'):
        self.message = message
        super().__init__(self.message)


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def name_enter(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        super().__init__(self.phone_validation(phone))

    def phone_validation(self, phone):
        if len(phone) == 10 and phone.isnumeric():
            return phone
        else:
            raise ValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            new_phone = Phone(phone)
            self.phones.append(new_phone)
            print(f"Phone {new_phone} added successfully to {self.name} record.")
        except ValueError as err:
            print(f'Error: {err}')

    def remove_phone(self, phone):
        try:
            for p in self.phones:
                if p.value == phone:
                    self.phones.remove(p)
            else:
                raise NumberNotFound
        except NumberNotFound as nnf:
            print(nnf.message)

    def find_phone(self, phone):
        try:
            for p in self.phones:
                if p.value == phone:
                    return p
            else:
                raise NumberNotFound
        except NumberNotFound as nnf:
            print(nnf.message)

    def edit_phone(self, phone, new_phone):
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone
                return p
        else:
            raise ValueError

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record
        else:
            raise ValueError

    def find(self, name):
        if name in self.data:
            return self.data.get(name)
        else:
            print('Name not found')

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print('Name not found')