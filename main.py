from abc import ABC, abstractmethod
from datetime import datetime
class Book(ABC):
    def __init__(self,ISBN,Title,Year,Price):
        self.ISBN=ISBN
        self.Title=Title
        self.Year=Year
        self.Price=Price
    @abstractmethod
    def delv(self,mail,add):
        pass
    @abstractmethod
    def Availabilty(self,qty):
        pass
    @abstractmethod
    def red_Stock(self,qty):
        pass
class Paperbook(Book):
    def __init__(self,ISBN,Title,Year,Price,Stock):
        super().__init__(ISBN,Title,Year,Price)
        self.Stock=Stock

    def delv(self, mail, add):
        print(f"Shipping Book {self.Title} to {add}")
    def Availabilty(self,qty):
        if(self.Stock>=qty):
            return True
        else:
            return False

    def red_Stock(self, qty):
        if(self.Availabilty(qty)):
            self.Stock-=qty
        else:
            print("Value Error: Stock is not enough to be available")


class E_book(Book):
    def __init__(self, ISBN, Title, Year, Price, filetype):
        super().__init__(ISBN, Title, Year, Price)
        self.filetype = filetype

    def delv(self, mail, add):
        print(f"Shipping Book {self.Title} ({self.filetype}) to {mail}")

    def Availabilty(self, qty):
        return (qty==1)

    def red_Stock(self, qty):
        if (qty!=1):
            print(" One book only can be bought at one time")

class Demo_Book(Book):
    def __init__(self, ISBN, Title, Year, Price):
        super().__init__(ISBN, Title, Year, Price=0)

    def delv(self, mail, add):
        print("Demo Book can not be delivered of bought")

    def Availabilty(self, qty):
        return False

    def red_Stock(self, qty):
        if (qty!=1):
            print(" Demo Books Are not For Sale")

class Invent:
    def __init__(self):
        self.books={}
    def add_book(self,Book):
        self.books[Book.ISBN]=Book
        print("Book " + Book.Title + " added to the Inventory")
    def Del_Outdated_book(self, current_year,Max):
        Deleted=[]
        Del=[ISBN for ISBN, Book in self.books.items() if current_year-Book.Year>Max]
        for i in Del:
            Deleted.append(self.books.pop(i))
            print("Outdated Book with ISBN "+ i +" has deleted")
        return Deleted
    def get_Book(self,ISBN):
        return self.books.get(ISBN)

class BookStore:
    def __init__(self):
        self.inventory=Invent()
    def add_Book(self,book):
        self.inventory.add_book(book)
    def del_outdated(self,Max):
        this_year=datetime.now().year
        return self.inventory.Del_Outdated_book(this_year,Max)
    def Buy_Book(self,isbn,qty,E_Mail,Add):
        book=self.inventory.get_Book(isbn)
        if not book:
            print("Book with given ISBN not found")
            return
        elif not book.Availabilty(qty):
            print("the requested quantity is not available for this book")
            return
        book.red_Stock(qty)
        total_cost=book.Price * qty
        print(f'Book {book.Title} purchased, and the Total price is: {total_cost}')
        book.delv(E_Mail,Add)
        return total_cost

# Test Class
class Test:
    @staticmethod
    def run():
        store=BookStore()
        paper=Paperbook("ISBN 1","DSP",2019,50,12)
        ebook=E_book("ISBN 2","NETWORK",2016,63,113)
        Dbook=Demo_Book("ISBN 3","C++",2023,87)
        store.add_Book(paper)
        store.add_Book(ebook)
        store.add_Book(Dbook)
        store.del_outdated(Max=10)
        store.Buy_Book("ISBN 1",10,"A7MED@gmail.com","Giza")
        store.Buy_Book("ISBN 2",120,"User@gmail.com","Cairo")
        store.Buy_Book("ISBN 3",120,"mo@gmail.com","N/A")

if __name__ == "__main__":
    Test.run()

