#Создайте телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
#Предусмотрите следующие функции для справочника:
#- новая запись;- вывод всего справочника;- поиск по имени;
#- экспорт справочника в форматы html, xml;- чтение данных из файла;- дополнительные функции по желанию
#Требуется реализовать минимум 3 инструмента для работы со справочником.
from tkinter import *

def add_contact():
	new_contact = '{name} {surname} {phone_number}'.format(name=EntryName.get(), surname=EntrySurame.get(), phone_number=EntryPhoneNumber.get())
	allContacts.insert(END, new_contact)
	write_contacts()

def delete_contact():
	select = allContacts.curselection()
	allContacts.delete(select[0])
	write_contacts()

def write_contacts():
	data = open('phonebook.txt', 'w', encoding='utf-8')
	for row in allContacts.get(0, END):
		data.writelines(row + '\n')
	data.close()

def print_contacts():
	try:
		data = open('phonebook.txt', 'r', encoding='utf-8')
		for contact in data.readlines():
			allContacts.insert(END, contact)
		data.close()
	except FileNotFoundError:
		print('Файл не найден')

root = Tk()
root.geometry('400x400')

buttonAddContact = Button(root, text = 'Добавить контакт', command = add_contact)
buttonAddContact.grid(row=3, column=0, columnspan=2)
buttonDeleteContact = Button(root, text = 'Удалить контакт', command = delete_contact)
buttonDeleteContact.grid(row=4, column=1)

labelName = Label(root, text='Введите имя')
labelName.grid(row=0, column=0)
labelSurame = Label(root, text='Введите фамилию')
labelSurame.grid(row=1, column=0)
labelPhoneNumber = Label(root, text='Введите номер')
labelPhoneNumber.grid(row=2, column=0)

EntryName = Entry(root, width=15)
EntryName.grid(row=0, column=1)
EntrySurame = Entry(root, width=15)
EntrySurame.grid(row=1, column=1)
EntryPhoneNumber = Entry(root, width=15)
EntryPhoneNumber.grid(row=2, column=1)

allContacts = Listbox(root, height=8, width=45, selectmode=EXTENDED)
allContacts.grid(row=4, column=0)
print_contacts()

root.mainloop()
