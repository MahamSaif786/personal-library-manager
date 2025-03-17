import json

class LibraryManager:
    def __init__(self):
        self.library = []
        self.filename = "library.json"
        self.load_library()

    def load_library(self):
        try:
            with open(self.filename, "r") as file:
                self.library = json.load(file)
                for book in self.library:
                    if "read" not in book:
                        book["read"] = False
        except (FileNotFoundError, json.JSONDecodeError):
            self.library = []

    def save_library(self):
        with open(self.filename, "w") as file:
            json.dump(self.library, file, indent=4)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author: ")
        year = input("Enter publication year: ")
        genre = input("Enter genre: ")
        read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        
        self.library.append({
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read_status
        })
        self.save_library()
        print("Book added successfully!\n")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        
        for book in self.library:
            if book["title"].lower() == title.lower():
                self.library.remove(book)
                self.save_library()
                print("Book removed successfully!\n")
                return
        print("Book not found!\n")

    def search_book(self):
        query = input("Enter title or author to search: ").lower()
        matches = [book for book in self.library if query in book["title"].lower() or query in book["author"].lower()]
        
        if matches:
            print("Matching Books:")
            for i, book in enumerate(matches, 1):
                status = "Read" if book["read"] else "Unread"
                print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            print("No matching books found.\n")

    def edit_book(self):
        title = input("Enter the title of the book you want to edit: ")
        for book in self.library:
            if book["title"].lower() == title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = input(f"New author ({book['author']}): ") or book["author"]
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["genre"] = input(f"New genre ({book['genre']}): ") or book["genre"]
                book["read"] = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
                self.save_library()
                print("Book updated successfully!\n")
                return
        print("Book not found!\n")

    def display_books(self):
        if not self.library:
            print("No books in library.\n")
            return
        
        print("Your Library:")
        for i, book in enumerate(self.library, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        print()

    def display_statistics(self):
        total = len(self.library)
        read_books = sum(1 for book in self.library if book["read"])
        percent_read = (read_books / total * 100) if total > 0 else 0
        print(f"Total books: {total}\nPercentage read: {percent_read:.2f}%\n")

    def menu(self):
        while True:
            print("Welcome to your Personal Library Manager!")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Edit a book")
            print("5. Display all books")
            print("6. Display statistics")
            print("7. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.edit_book()
            elif choice == "5":
                self.display_books()
            elif choice == "6":
                self.display_statistics()
            elif choice == "7":
                self.save_library()
                print("Library saved to file. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    LibraryManager().menu()