choose = 1
contacts = []
while choose != 5:
    choose = int(input("1. Add contact\n2. Show contact\n3. Search contact\n4. Delete contact\n5. Exit\nchoose: "))
    if choose == 1:
        contact = input("Enter contact: ")
        contacts.append(contact)
    elif choose == 2:
        print ("Contacts:")
        for contact in contacts:
            print (contact)
    elif choose == 3:
        search = input("Search: ")
        if search in contacts:
            print ("Found!")
        else:
            print ("Not found!")
    elif choose == 4:
        for contact in contacts:
            print(contact)
            todelete = input("Choose to delete:")
            if todelete in contacts:
                contacts.remove(todelete)
                print("Deleted!")
            else:
                print ("Contact not found!")
print ("Goodbye!")