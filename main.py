#Library Management System

#Book information
book_title="Python Basics"
price=500
available=True
category="Programming"

#Display book information
print("Book Title:",book_title)
print("Price:",price)
print("Available:",available)
print("Category:",category)

#Check book availablity
if available :
    print("Book is available.")
else:
    print("Book is Not available.")

#List of 5 books
books = [
    "Python Basics",
    "Data Structure",
    "Database Management",
    "Operating Systems",
    "Computer Networks"
]

#Display all books
print("Library Books:")

for book in books:
    print(book)

## -->Day 2: Functions & OOPs Classes<--

#Function to calculate fine
def calculate_fine(days_late):
    fine = days_late*10
    return fine

fine = calculate_fine(7)                     #Calling the function

print("\nDays Late:",5)
print("Fine:",fine)

#Recursive function
def  gcd(a, b):

    if b==0:                                   #base condition
        return a

    return gcd(b, a % b)                       #recursive call

result = gcd(48, 18)                           #calling the recursive function
print("GCD of 48 and 18:",result)

#Classes & Objects
class Book:         #book class
    def __init__(self, title,author):
        self.title = title
        self.price = author
        self.available = True

    def issue(self):                            #method to issue the book
        self.available = False

b1 = Book("Python Basics", "Guido van Rossum")          #creating a book object

print("Book Title:", b1.title)
print("Author:", b1.price)
print("Available:", b1.available)

b1.issue()                                      #issue the book

print("After issuing:", b1.available)

#Constructor and Destructor
class Member:                                   #member class

    def __init__(self, name,email):             #constructor
        self.name = name
        self.email = email
        print("Member created:",self.name)

    def __del__(self):                          #destructor
        print("Member deleted:",self.name)

member1 = Member("Shadab", "shadab@example.com")

print("Member name:",member1.name)
print("Member email:",member1.email)


## -->Day 3: Inheritance, Encapsulation & Polymorphism<--

#Encapsulation
class accountholder:                            #acountholder class

    def __init__(self, name, password):         #constructor
        self.name = name
        self.__password = password

    def change_password(self, new_password):        #method to change password
        self.__password = new_password
        print("Password changed successfully")

account=accountholder("shadab","old123")            #creating an accountholder object
print("\nAccount Holder:",account.name)


account.change_password("new123")                   #changing password  

#Inheritance
class LibraryBook:

    def __init__(self,title,author):                #parent class
        self.title=title
        self.author=author

    def show_book(self):
        print("Book Title:",self.title)
        print("Book Author:",self.author)

class Ebook(LibraryBook):                               #child class
    pass

ebook=Ebook("Python Basics","Guido van Rossum")         #creating an Ebook object

ebook.show_book()                                       #using method inherited from LibraryBook

#Polymorphism
class BookType:                                     #parent class
    def issue(self):
        print("E-book issued")


class EBookType(BookType):                               #child class

    def issue(self):                                    #same method diffrent behavior
        print("E-book access provided")

book=BookType()                             #creating objects
ebook=EBookType()

book.issue()                              #calling the same method
ebook.issue()

#Abstraction
from abc import ABC, abstractmethod

class LibraryItem(ABC):                            #abstract class
    
    @abstractmethod
    def display_info(self):                         
        pass

class LibraryBookItem(LibraryItem):                     #child class

    def display_info(self):                             
        print("This is a library book.")


item=LibraryBookItem()                            #creating object of child class
item.display_info()


## -->Day 4: Exception Handling & File Handling<--

