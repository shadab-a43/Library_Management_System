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

