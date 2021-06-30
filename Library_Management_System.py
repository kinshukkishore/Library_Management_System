class Library:
    def __init__(self, bookList):
        self.bookList=bookList
        self.lendDirectory={}

    def displayBooks(self):
        print("Books present in this library: ")
        for book in self.bookList:
            print(" *", book)

    def lendBooks(self,user,book):
        if book in self.bookList:
            if book not in self.lendDirectory.keys():
                self.lendDirectory.update({book:user})
                print("Database updated! You have been issued the book. Take good care of it.")                
            else:
                print(f"Book is already been issued to {self.lendDirectory[book]}")
        else:
            print("Sorry This book is currently not availble in this Library. Please Try after some time.")

    def addBooks(self,book):
        self.bookList.append(book)
        print("Book has been added to the list.")


    def returnBooks(self,book):
        self.lendDirectory.pop(book)
        

if __name__ == "__main__":
    stardust=Library(["HTML", "Django", "css", "Python","Javascript"])
    while(True):
        welcomeMsg = '''\n ====== Welcome to Stardust Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add a book
        4. Return a book
        5. Exit the Library
        '''
        print(welcomeMsg)

        a = int(input("Enter a choice: "))
        try:
            if a == 1:
                stardust.displayBooks()
            elif a == 2:
                book=input("Enter the name of book you want to borrow: ")
                user=input("Enter your name: ")
                stardust.lendBooks(user,book)
            elif a == 3:
                book=input("Enter the name you want to add: ")
                stardust.addBooks(book)
            elif a == 4:
                book=input("Enter the name of the book you want to return: ")
                stardust.returnBooks(book)
            elif a == 5:
                print("****Thank you for choosing Stardust Library****")
                exit()
            else:
                print("Invalid Choice!")
        except:
            print("Something went wrong!!")
            exit()