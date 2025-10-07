class LibraryBook:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    
    def is_available(self):
        return self.copies > 0
    
    def check_out(self):
        if self.is_available():
            self.copies -= 1
            print(f"Checked out '{self.title}'.")
        else:
            print(f"'{self.title}' is not available for checkout.")

    def return_book(self):
        self.copies += 1
        print(f"Returned '{self.title}'. Total copies now: {self.copies}")
    
    def __str__(self):
        status = "Available" if self.is_available() else "Not Available"
        return f"'{self.title}' by {self.author} - {status} ({self.copies} copies left)"
    
class LibraryCatalogue:
    def __init__(self):
        self.catalogue = {}

    def add_book(self, title, author, copies):
        if title in self.catalogue:
            self.catalogue[title].copies += copies
            print(f"Added {copies} more copies of '{title}'. Total copies now: {self.books[title].copies}")
        else:
            self.catalogue1
            [title] = LibraryBook(title, author, copies)
            print(f"Added new book '{title}' by {author} with {copies} copies.")

    def list_all_books(self):
        if not self.catalogue:
            print("No books in the catalogue.")
        else:
            print("\n-- Library Catalogue --")
            for book in self.catalogue.values():
                print(book)

    def check_out_book(self, title):
        if title in self.catalogue:
            self.catalogue[title].check_out()
        else:
            print(f"No book found with title '{title}'.")
    
    def return_book(self, title):
        if title in self.catalogue:
            self.catalogue[title].return_book()
        else:
            print(f"No book found with title '{title}'.")
            
def main():
    library = LibraryCatalogue()

    while True:
        print("\n--- Library Catalogue Menu ---")
        print("1. Add Book")
        print("2. List All Books")
        print("3. Check Out Book")
        print("4. Return Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(title, author, copies)
        elif choice == '2':
            library.list_all_books()
        elif choice == '3':
            title = input("Enter book title to check out: ")
            library.check_out_book(title)
        elif choice == '4':
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

