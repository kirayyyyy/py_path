books = []
def add_books():
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year: "))
    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True,
    }

    books.append(book)
    print("Book added!")
def show_books():
    x = 1
    if books:
        for book in books:
            print ("Book",x)
            print ("Title:",book["title"])
            print ("Author:",book["author"])
            print ("Year:",book["year"])
            print ("Available:",book["available"])
            print ()
            x+=1
    else:
        print("No books in library.")
def search_book():
    search = input("Enter Book:")
    found = False
    for book in books:
        if search == book["title"]:
            print("Book found!")
            found = True
            break
    if not found:
            print("Book not found!")
def remove_book():
    remove = input("Enter Book: ")
    found = False
    for book in books:
        if remove == book["title"]:
            books.remove(book)
            print("Book removed!")
            found = True
            break
    if not found:
            print("Book not found!")
choose = 0
def borrow_book():
    borrow = input("Enter Book:")
    found = False
    for book in books:
        if borrow == book["title"] and book["available"] == True:
            book["available"] = False
            print("Book borrowed!")
            found = True
            break
        elif borrow == book["title"] and book["available"] == False:
            found = True
            print("Book is already borrowed!")
    if not found:
        print("Book not found!")
def return_book():
    returnb = input("Enter Book:")
    found = False
    for book in books:
        if returnb == book["title"] and book["available"] == False:
            book["available"] = True
            print("Book returned!")
            found = True
            break
        elif returnb == book["title"] and book["available"] == True:
            print ("Book is already in the library.")
            found = True
    if not found:
        print ("Book not found")

while choose != 7:
    choose = int(input("========== Library ==========\n\n1. Add Book\n2. Show Books\n3. Search Book\n""4. Remove Book\n5. Borrow Book\n6. Return Book\n7. Exit\n\nChoose:"))
    if choose == 1:
        add_books()
    if choose == 2:
        show_books()
    if choose == 3:
        search_book()
    if choose == 4:
        remove_book()
    if choose == 5:
        borrow_book()
    if choose == 6:
        return_book()
print ("Goodbye!")