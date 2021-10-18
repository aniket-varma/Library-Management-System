class library:
    def __init__(self,books):
        self.books=books
    def display(self):
        print("Available Books:-")
        for book in self.books:
            print(book)

    def borrow(self,books):
        for book in books:
            if book in self.books:
                print(f"{book} is issued to you")
                self.books.remove(book)
            else:
                print(f"{book} is currently not availaible")
    def return_book(self,books):
        for book in books:
            self.books.append(book)
        print("Thanks for returning/donating the book")

class student:
    def request_book(self):
        books=[]
        n=int(input("How many books you want to borrow(max limit:3): "))
        for i in range(n):
            book=input("Enter a book name: ")
            books.append(book)
        return books

    def return_book(self):
        books=[]
        n=int(input("How many books you want to return: "))
        for i in range(n):
            book=input("Enter a book name: ")
            books.append(book)
        return books
    
if __name__ == '__main__':
    National_Library=library(["R D Sharma","Morris Mano","Bjarne Stroustop","Let us C","Algorithms"])
    student1=student()
    print("***Welcome to National Library***")
    while(True):
        print('''
1.Display Book List
2.Borrow Books
3.Return/Donate Books
4.Exit
        ''')
        choice=int(input("Enter your choice: "))
        if(choice==1):
            National_Library.display()
        elif(choice==2):
            National_Library.borrow(student1.request_book())
        elif(choice==3):
            National_Library.return_book(student1.return_book())
        elif(choice==4):
            print("Thanks for using this online system")
            exit()
        else:
            print("Invalid choice")