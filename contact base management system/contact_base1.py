#contact base management system

'''1.add contact
2.update contact
3.list contacts
4.delete contact
5.exit
option-1->name->pooja,mobileno->789080....,mailid=p@gmail.com
option-3->to display contact details
option-2->old mobile->789080,new mobile->9878989
option-3->to display updated contact details
option-4->name->pooja,->it will remove entire contact information
option-5->exit'''

class Contact:
    def __init__(self):
        self.contacts = {}
class AddContact(Contact):
    def add_contact(self):
        name = input("Enter Name: ")
        mobile = input("Enter Mobile Number: ")
        mailid = input("Enter Mail ID: ")
        self.contacts[name] = {
            "Mobile": mobile,
            "Mailid": mailid
        }
        print("Contact Added Successfully")
class UpdateContact(AddContact):
    def update_contact(self):
        old_number = input("Enter Old Mobile Number: ")
        for name in self.contacts:
            if self.contacts[name]["Mobile"] == old_number:
                new_number = input("Enter New Mobile Number: ")
                self.contacts[name]["Mobile"] = new_number
                print("Contact Updated Successfully")
                return
        print("Mobile Number Not Found")
class ListContact(UpdateContact):
    def list_contact(self):
        if len(self.contacts) == 0:
            print("No Contact")
        else:
            for name, details in self.contacts.items():
                print("Name :", name)
                print("Mobile :", details["Mobile"])
                print("Mail ID :", details["Mailid"])
class DeleteContact(ListContact):
    def delete_contact(self):
        name = input("Enter Name to Delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact Deleted Successfully")
        else:
            print("Contact Not Found")
class Menu(DeleteContact):
    def menu(self):
        while True:
            option = int(input(""" 1. Add Contact
2. Update Contact
3. Contact List
4. Delete Contact
5. Exit
Enter Option:
"""))
            if option == 1:
                self.add_contact()
            elif option == 2:
                self.update_contact()
            elif option == 3:
                self.list_contact()
            elif option == 4:
                self.delete_contact()
            elif option == 5:
                print("quit")
                break
            else:
                print("Invalid Choice")
obj = Menu()
obj.menu()
