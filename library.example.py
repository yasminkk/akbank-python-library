class bookk:
    def __init__(self, title, author, num_pages,release_year):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.release_year = release_year

    def __str__(self):
        return f"{self.title},{self.author},{self.num_pages} page,{self.release_year}"

class library:
  with open("books.txt", "a+") as dosya: 
  
    def __init__(self):
        self.books = []
               

    def add_book(self,book):
            self.books.append(book)
            print(f"\n\nBook '{title}' added successfully.\n")
  
    def list_book(self):
        if  self.books:
            print("Books in the library\n")

            for i, book in enumerate(self.books, start=1):
               print(f"{i}. {book}")
        else:
           print('\nthere is no book in the library\n') 
    
    def remove_book(self,name):
                   
        if book.title.lower()==book_name.lower():
               self.books.remove(book)
               print(f"{name} is deleted in the library\n")
        else:
               print(f"{name} not found in the library\n")

    


lib=library()
while True:
        print('***MENU***')
        print("\n1. List book\n2.Add book\n3.Remove book<\n4.Exist")
        choose = input("Select the action you want to take:")

        if choose == "1":
            lib.list_book()
        elif choose == "2":
           
            title = input("book name: ")
            author = input("author: ")
        
            while True:
                try:
                        num_pages = int(input("number of page:"))
                        break 
                except ValueError:
                        print("\nIncorrect entry. Please enter number of pages:")

            while True:
                try:
                        release_year = int(input("year:"))
                        break  
                except ValueError:
                        print("\nIncorrect entry. Please enter a year:")

            book = bookk(title, author, num_pages, release_year)
            lib.add_book(book)
        
           
       
        elif choose == "3":
             book_name = input("Enter the name of the book you want to delete: ")
             lib.remove_book(book_name)
        
        elif choose == "4":
             print("Exiting the program...")
             break
        else:
             print("You made an invalid choice. Please try again.")
             