#contact base management system

class contact():
    def __init__(self):
        self.contacts={}
class AddContact(contact):
    def add_contact(self):
        name=input("enter name: ")
        mobile=input("enter mobile number: ")
        mailid=input("enter maild: ")
        self.contacts[name]={
            "Mobile": mobile,
            "Mailid": mailid
            }
        print("contact added successfully")
class UpdateContact(AddContact):
    def update_contact(self):
        old_number=input("enter old mobile number: ")
        for name in self.contacts:
            if self.contacts[name]["Mobile"]==old_number:
                new_number=input("enter new mobile number: ")
                self.contacts[name]["Mobile"]=new_number
                print("contact updated successfully")
                return
            print("Mobile number not found")
class ListContact(UpdateContact):
    def list_contact(self):
        if len(self.contacts)==0:
            print("No contact")
        else:
            for name ,details in self.contacts.items():
                print("Name:",name)
                print("Mobile:",details["Mobile"])
                print("Mail Id:",details["Mailid"])
class DeleteContact(ListContact):
    def delete_contact(self):
        name=input("Enter the name to delete:")
        if name in self.contacts:
            del self.contacts[name]
            print("contact deleted successfully")
        else:
            print("Contact Not found")
class Menu(DeleteContact):
    def menu(self):
        while True:
            option=int(input("""1.Add contact
2.Update COntact
3.Contact list
4.Delete Contact
5.Exit
Enter option:
"""))
            if option==1:
                self.add_contact()
            elif option==2:
                self.update_contact()
            elif option==3:
                self.list_contact()
            elif option==4:
                self.delete_contact()
            elif option==5:
                print("quit")
                break
            else:
                print("invalid option")
obj=Menu()
obj.menu()
