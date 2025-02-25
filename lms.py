# Library Inventory Management System
from datetime import date, timedelta

class Library():
    store_book = {'python': ['drshn', 30], 'java': ['dhruv', 20]}

    def addbook(self):
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
        except Exception as e:
            print(e)

    def removebook(self):
        """ Remove book in store """
        try:
            title = input("enter title of book you want to remove : ")
            if title in self.store_book:
                del self.store_book[title]
                print("remove book succesfully! ")
            else:
                print("Book are not available ")
        except Exception as e:
            print(e)

    def updatebook(self):
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
        except Exception as e:
            print(e)

    def searchbook(self):
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
    # userdata = {"dishant": [['python', '2025-02-25', '2025-03-11'], ['java', '2025-02-25', '2025-03-11']]}
    userdata = {}
    borrowing_history = {}
    hold_user_book = {}

    def borrowbook(self):
        """ user can borrow book """
        try:
            book_name = input("which are book borrow : ")
            if book_name in super().store_book and super().store_book.get(book_name)[1] >= 1:
                user_name = input("enter User Name : ")
                # """ if user borrow first time """
                if self.userdata.get(user_name, "not found") == "not found":
                    due_date = date.today() + timedelta(days=14)
                    due_date = due_date.strftime('%Y-%m-%d')
                    self.userdata.update({user_name: [[book_name, date.today().strftime('%Y-%m-%d'), due_date]]})
                    # update old Data
                    olddata = super().store_book.get(book_name)
                    super().store_book[book_name] = [olddata[0],olddata[1]-1]
                    # book borrow history
                    if not self.borrowing_history:
                        self.borrowing_history.update({user_name : [[book_name, date.today().strftime('%Y-%m-%d'), due_date]]})
                    else:
                        self.borrowing_history[user_name].append([book_name, date.today().strftime('%Y-%m-%d'), due_date])
                    print(f"{book_name} book successfully borrow by {user_name}")
                # """ if user borrow second time """
                elif len(self.userdata.get(user_name)) == 1:
                    due_date = date.today() + timedelta(days=14)
                    due_date = due_date.strftime('%Y-%m-%d')
                    self.userdata[user_name].append([book_name, date.today().strftime('%Y-%m-%d'), due_date])
                    # update old Data
                    olddata = self.store_book.get(book_name)
                    super().store_book[book_name] = [olddata[0],olddata[1]-1]
                    # book borrow history
                    self.borrowing_history[user_name].append([book_name, date.today().strftime('%Y-%m-%d'), due_date])
                    print(f"{book_name} book successfully borrow by {user_name}")
                # """ if user borrow third time """
                else:
                    print("You have already borrow 2 books.")
            else:
                print("book not available right now!" )
                username = input("enter your name for holding dict :")
                if book_name in self.hold_user_book:
                    self.hold_user_book.get(book_name).append([username])
                else:
                    self.hold_user_book.update({book_name : [[username]]})

        except Exception as e:
            print(e)

    def returnbook(self):
        """ use can return book """
        try:
            username = input("enter user name : ")
            if username in self.userdata:
                bookname = input("enter book name : ")
                for index,val in enumerate(self.userdata.get(username)):
                    if val[0] == bookname:
                        if val[2] > date.today().strftime('%Y-%m-%d'):
                            del self.userdata.get(username)[index]
                            super().store_book.get(bookname)
                            olddata = super().store_book.get(bookname)
                            super().store_book[bookname] = [olddata[0], olddata[1] + 1]
                            print("Successfull return book!")
                            if len(self.userdata.get(username)) == 0:
                                del self.userdata[username]
                        else:
                            print("you pay panalty is 10rs")
                            del self.userdata.get(username)[index]
                            super().store_book.get(bookname)
                            olddata = super().store_book.get(bookname)
                            super().store_book[bookname] = [olddata[0], olddata[1] + 1]
                            print("Successfull return book!")
                            if len(self.userdata.get(username)) == 0:
                                del self.userdata[username]
            else:
                print(f"{username} not borrow any book")
        except Exception as e:
            print(e)

    def userDetail(self):
        try:
            name = input("enter user name : ")
            if name in self.userdata:
                data = self.userdata.get(name)
                print(name, end=" ")
                for user_info in data:
                    print(f"book : {user_info[0]}, isu date : {user_info[1]}, due date : {user_info[2]}")
            else:
                print(f"{name} not borrow any books.")
        except Exception as e:
            print(e)

    def display_overdue_book(self):
        try:
            for name,data in self.userdata.items():
                for value in data:
                    if date.today().strftime('%Y-%m-%d') > value[2]:
                        print(name,value)
        except Exception as e:
            print(e)

    def display_borrow_history(self):
        try:
            username = input("enter user name : ")
            for name,value in self.borrowing_history.items():
                if name == username:
                    print(name, value)
        except Exception as e:
            print(e)

    def display_holding_list(self):
        try:
            for name,value in self.hold_user_book.items():
                    print(name, value)
        except Exception as e:
            print(e)

#  Start the Program
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
        print(" 9. Display overdue books.")
        print("10. user show borrow history.")
        print("11. book holding user list.")
        print("12. exit")
        user_input = int(input("Press Number want you perform operations : "))

        match(user_input):
            case 1:
                u1.addbook()
            case 2:
                u1.removebook()
            case 3:
                u1.updatebook()
            case 4:
                print(u1.store_book)
            case 5:
                u1.searchbook()
            case 6:
                u1.borrowbook()
            case 7:
                u1.returnbook()
            case 8:
                u1.userDetail()
            case 9:
                u1.display_overdue_book()
            case 10:
                u1.display_holding_list()
            case 11:
                u1.display_borrow_history()
            case _:
                print("exit")
                break
    except ValueError:
        print(" enter number!")