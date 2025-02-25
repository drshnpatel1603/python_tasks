# Library Inventory Management System
from logging import exception
from datetime import date, timedelta

class Library():
    def addbook(self,store_book):
        """ Add book in store  """
        try:
            title = input("enter book title : ")
            author = input("enter book author : ")
            quantity = int(input("enter book quantity : "))
            if not title in self.store_book:
                self.store_book.update({title : [author,quantity]})
                print("added successfull!")
                print(self.store_book)
            else :
                print("This Book already in store")
        except exception as e:
            print(e)

    def removebook(self,store_book):
        """ Remove book in store """
        try:
            title = input("enter title of book you want to remove : ")
            if title in self.store_book:
                del self.store_book[title]
                print("remove book succesfully! ")
            else:
                print("Book are not available ")
        except exception as e:
            print(e)

    def updatebook(self,store_book):
        """ Update the Book Information """
        try:
            title = input("which book changes information : ")
            if title in self.store_book:
                print("if not change data than press -1")
                author = input("enter author name : ")
                quantity = int(input("enter quantity : "))
                olddata = self.store_book.get(title)
                """ Admin Can Change Specific field """
                if author != '-1':
                    self.store_book[title] = [author,olddata[1]]
                if quantity != -1:
                    self.store_book[title] = [olddata[0],quantity]
                print("Update successfully")
                print(self.store_book)
            else:
                print("book not found!")
        except exception as e:
            print(e)

    def searchbook(self,store_book):
        """ Seching book in store """
        try:
            search_book = input("find book : ")
            if self.store_book.get(search_book):
                print(f"{search_book} : {self.store_book.get(search_book)}")
            else:
                print("book not found!")
        except ValueError:
            print("enter a valid value")


class User(Library):
    def borrowbook(self,store_book,userdata):
        """ user can borrow book """
        try:
            book_name = input("which are book borrow : ")
            if book_name in store_book and store_book.get(book_name)[1] >= 1:
                user_name = input("enter User Name : ")
                # """ if user borrow first time """
                if userdata.get(user_name, "not found") == "not found":
                    due_date = date.today() + timedelta(days=14)
                    due_date = due_date.strftime('%Y-%m-%d')
                    userdata.update({user_name: [[book_name, date.today().strftime('%Y-%m-%d'), due_date]]})
                    olddata = store_book.get(book_name)
                    store_book[book_name] = [olddata[0],olddata[1]-1]
                    print(f"{book_name} book successfully borrow by {user_name}")
                # """ if user borrow second time """
                elif len(userdata.get(user_name)) == 1:
                    due_date = date.today() + timedelta(days=14)
                    due_date = due_date.strftime('%Y-%m-%d')
                    userdata[user_name].append([book_name, date.today().strftime('%Y-%m-%d'), due_date])
                    olddata = store_book.get(book_name)
                    store_book[book_name] = [olddata[0],olddata[1]-1]
                    print(f"{book_name} book successfully borrow by {user_name}")
                # """ if user borrow third time """
                else:
                    print("You have already borrow 2 books.")
            else:
                print("book not available!")
        except exception as e:
            print(e)

    def returnbook(self,store_book, userdata):
        try:
            username = input("enter user name : ")
            if username in self.userdata:
                bookname = input("enter book name : ")
                for index,val in enumerate(self.userdata.get(username)):
                    if val[0] == bookname:
                        del userdata.get(username)[index]
                        self.store_book.get(bookname)
                        olddata = self.store_book.get(bookname)
                        self.store_book[bookname] = [olddata[0], olddata[1] + 1]
                        print("Successfull return book!")
                        if len(self.userdata.get(username)) == 0:
                            del self.userdata[username]
            else:
                print(f"{username} not borrow any book")
        except exception as e:
            print(e)

    def userDetail(self,userdata):
        try:
            name = input("enter user name : ")
            if name in self.userdata:
                data = self.userdata.get(name)
                print(name, end=" ")
                for user_info in data:
                    print(f"book : {user_info[0]}, isu date : {user_info[1]}, due date : {user_info[2]}")
            else:
                print(f"{name} not borrow any books.")
        except exception as e:
            print(e)

#  Start the Program
store_book = {'python': ['drshn', 30], 'java': ['dhruv', 20]}
userdata = {"dishant" : [['python', '2025-02-25', '2025-03-11'], ['java', '2025-02-25', '2025-03-11']]}
l1 = Library()
u1 = User()
while(True):
    try:
        print(" \n Library Management System.")
        print(" 1. Add books to the library.")
        print(" 2. Remove books from the library.")
        print(" 3. Update book information.")
        print(" 4. Display available books.")
        print(" 5. Search for books by title.")
        print(" 6. borrow books.")
        print(" 7. user can return book.")
        print(" 8. show specific user detail.")
        print(" 9. exit")
        user_input = int(input("Press Number want you perform operations : "))

        match(user_input):
            case 1:
                l1.addbook(store_book)
            case 2:
                l1.removebook(store_book)
            case 3:
                l1.updatebook(store_book)
            case 4:
                print(store_book)
            case 5:
                l1.searchbook(store_book)
            case 6:
                u1.borrowbook(store_book,userdata)
            case 7:
                u1.returnbook(store_book, userdata)
            case 8:
                u1.userDetail(userdata)
            case _:
                print("exit")
                break
    except ValueError:
        print(" enter number!")
