#Library Managenment System

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
    "Pyhton Basics",
    "Data Structure",
    "Database Managenment",
    "Operating Systems",
    "Computer Networks"
]

#Display all books
print("\nLibrary Books:")

for book in books:
    print(book)

## -->Day 2: Functions & OOPs Classes<--

#Function to calculate fine
def calculate_fine(days_late):
    fine = days_late*10
    return fine

fine = calculate_fine(7)                     #Calling the function

print("Days Late:",5)
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