from tkinter import *
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        root.title("DBU LIBRARY MANAGEMENT SYSTEM")
        root.configure(bg='#cfe2f3')  # Changed background color to light blue

        self.library = []  # List to hold existing library books
        self.added_books = []  # List to hold newly added books by the admin
        self.borrowed_books = []  # List to keep track of borrowed books

        self.create_widgets()

    def create_widgets(self):
        self.label0 = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="black", fg="white", font=("Times", 30))

        # Entry fields and labels
        self.label1 = Label(self.root, text="ENTER BOOK NAME", bg="purple", relief="ridge", fg="white", font=("Times", 12), width=25)
        self.entry1 = Entry(self.root, font=("Times", 12))

        self.label2 = Label(self.root, text="ENTER AUTHOR NAME", bd="2", relief="ridge", height="1", bg="purple", fg="white", font=("Times", 12), width=25)
        self.entry2 = Entry(self.root, font=("Times", 12))

        self.label3 = Label(self.root, text="ENTER BOOK ID", bd="2", relief="ridge", bg="purple", fg="white", font=("Times", 12), width=25)
        self.entry3 = Entry(self.root, font=("Times", 12))

        self.label4 = Label(self.root, text="ENTER SHELF NUMBER", bd="2", relief="ridge", bg="purple", fg="white", font=("Times", 12), width=25)
        self.entry4 = Entry(self.root, font=("Times", 12))

        self.label5 = Label(self.root, text="ENTER EDITION YEAR", bg="purple", relief="ridge", fg="white", font=("Times", 12), width=25)
        self.entry5 = Entry(self.root, font=("Times", 12))

        self.label6 = Label(self.root, text="ENTER SEARCH ID", bd="2", relief="ridge", bg="purple", fg="white", font=("Times", 12), width=25)
        self.entry6 = Entry(self.root, font=("Times", 12))

        # Buttons
        self.button2 = Button(self.root, text="DISPLAY BOOK", bg="light blue", fg="black", width=30, font=("Times", 12), command=self.display_books)
        self.button4 = Button(self.root, text="REMOVE BOOK(by edition year)", bg="light blue", fg="black", width=30, font=("Times", 12), command=self.remove_book)
        self.button7 = Button(self.root, text="BORROW BOOK(ID)", bg="light blue", fg="black", width=30, font=("Times", 12), command=self.borrow_book_gui)
        self.button8 = Button(self.root, text="RETURN BOOK(return to library)", bg="light blue", fg="black", width=30, font=("Times", 12), command=self.return_book_gui)

        self.button1 = Button(self.root, text="ADD BOOK", bg="light blue", fg="black", width=30, font=("Times", 12), command=self.add_book)
        self.button3 = Button(self.root, text="SEARCH BOOK(by_id)", bg="light blue", fg="black", width=30, font=("Times", 12), command=self.search_book)
        self.button5 = Button(self.root, text="ADD BOOK (admin)", bg="light blue", fg="black", width=30, font=("Times", 12), command=self.add_book_by_admin)
        self.button6 = Button(self.root, text="DISPLAY ALL BOOK(add by admin,lib exist book) ", bg="light blue", fg="black", width=30, font=("Times", 12), command=self.display_all_books)
        self.button9 = Button(self.root, text="BOOK BORROWED STATUS", bg="light blue", fg="black", width=30, font=("Times", 12), command=self.book_borrowed_status)
        self.button10 = Button(self.root, text="EXIT", bg="light blue", fg="black", width=30, font=("Times", 12), command=self.root.quit)

        # Grid placement
        self.label0.grid(columnspan=10, padx=10, pady=10)

        self.label1.grid(row=1, column=0, sticky=W, padx=10, pady=10)
        self.entry1.grid(row=1, column=1, padx=10, pady=10)
        self.button1.grid(row=1, column=2, padx=10, pady=10)

        self.label2.grid(row=2, column=0, sticky=W, padx=10, pady=10)
        self.entry2.grid(row=2, column=1, padx=10, pady=10)
        self.button2.grid(row=2, column=2, padx=10, pady=10)

        self.label3.grid(row=3, column=0, sticky=W, padx=10, pady=10)
        self.entry3.grid(row=3, column=1, padx=10, pady=10)
        self.button3.grid(row=3, column=2, padx=10, pady=10)

        self.label4.grid(row=4, column=0, sticky=W, padx=10, pady=10)
        self.entry4.grid(row=4, column=1, padx=10, pady=10)
        self.button4.grid(row=4, column=2, padx=10, pady=10)

        self.label5.grid(row=5, column=0, sticky=W, padx=10, pady=10)
        self.entry5.grid(row=5, column=1, padx=10, pady=10)
        self.button5.grid(row=5, column=2, padx=10, pady=10)

        self.label6.grid(row=6, column=0, sticky=W, padx=10, pady=10)
        self.entry6.grid(row=6, column=1, padx=10, pady=10)
        self.button6.grid(row=6, column=2, padx=10, pady=10)

        self.button7.grid(row=1, column=3, padx=10, pady=10)
        self.button8.grid(row=2, column=3, padx=10, pady=10)
        self.button9.grid(row=3, column=3, padx=10, pady=10)
        self.button10.grid(row=7, columnspan=4, padx=10, pady=10)

        # Bind the Enter key to search_book function
        self.root.bind('<Return>', lambda event: self.search_book())

    def add_book(self):
        name = self.entry1.get()
        author = self.entry2.get()
        book_id = int(self.entry3.get())
        shelf = int(self.entry4.get())
        edition_year = int(self.entry5.get())
        book = {"name": name, "author": author, "id": book_id, "shelf": shelf, "edition_year": edition_year, "borrowed": False}
        self.library.append(book)
        messagebox.showinfo("Success", "Book added to library")
        self.clear_entries()

    def display_books(self):
        if self.library:
            books = "\n".join(f"Name: {book['name']}, Author: {book['author']}, ID: {book['id']}, Shelf: {book['shelf']}, Edition Year: {book['edition_year']}, Borrowed: {book['borrowed']}" for book in self.library)
            messagebox.showinfo("Library exist  Books", books)
        else:
            messagebox.showinfo("Library exist Books", "No books exist in the library")

    def search_book(self):
        search_id = int(self.entry6.get())
        for book in self.library:
            if book["id"] == search_id:
                messagebox.showinfo("Book Found", f" Name: {book['name']}, Author: {book['author']},ID: {book['id']},shelf:{book['shelf']},Edition year:{book['edition_year']} borrowed: {book['borrowed']}")
                return
        messagebox.showinfo("Not Found", "The book is not found in the library")

    def remove_book(self):
        edition_year = int(self.entry5.get())
        removed_book = None  # Initialize variable to store removed book information
        removed = False
        for book in self.library:
            if book["edition_year"] <= edition_year:
                removed_book = book  # Store the book information before removal
                self.library.remove(book)
                removed = True
                break
        if removed:
            if removed_book:
                # Show the book information before removal
                messagebox.showinfo("Removed Book", f"The following book will be removed:\nName: {removed_book['name']}\nAuthor: {removed_book['author']}\nID: {removed_book['id']}")
            self.display_books()
            messagebox.showinfo("Success", "Book removed successfully")
        else:
            messagebox.showinfo("Not Removed", "No books were removed because they are newer")

    def add_book_by_admin(self):
        name = self.entry1.get()
        author = self.entry2.get()
        book_id = int(self.entry3.get())
        shelf = int(self.entry4.get())
        edition_year = int(self.entry5.get())
        book = {"name": name, "author": author, "id": book_id, "shelf": shelf, "edition_year": edition_year, "borrowed": False}
        self.added_books.append(book)
        self.display_all_books()
        messagebox.showinfo("Success", "Book added by admin")
        self.clear_entries()

    def display_all_books(self):
        library_books = "\n".join(f"ID: {book['id']}, Name: {book['name']}, Author: {book['author']}" for book in self.library)
        new_books = "\n".join(f"ID: {book['id']}, Name: {book['name']}, Author: {book['author']}" for book in self.added_books)
        messagebox.showinfo("Books", f"Books in the library:\n{library_books}\n\nNew Books added by admin:\n{new_books}")

    def borrow_book_gui(self):
        book_id = int(self.entry6.get())
        book = self.find_book_by_id(book_id)
        if book:
            messagebox.showinfo("Borrow Book", f"You are going to borrow the following book:\nName: {book['name']}\nAuthor: {book['author']}\nID: {book['id']}")
            self.borrow_book(book)
        else:
            messagebox.showinfo("Error", "Book not found in the library")

    def return_book_gui(self):
        book_id = int(self.entry6.get())
        book = self.find_borrowed_book_by_id(book_id)
        if book:
            messagebox.showinfo("Return Book", f"You are going to return the following book:\nName: {book['name']}\nAuthor: {book['author']}\nID: {book['id']}")
            self.return_book(book)
        else:
            messagebox.showinfo("Error", "Book not found in borrowed books")

    def borrow_book(self, book):
        if not book["borrowed"]:
            book["borrowed"] = True
            self.borrowed_books.append(book)
            messagebox.showinfo("Success", "Book borrowed successfully")
        else:
            messagebox.showinfo("Error", "Book is already borrowed")

    def return_book(self, book):
        book["borrowed"] = False
        self.borrowed_books.remove(book)
        messagebox.showinfo("Success", "Book returned successfully")

    def find_book_by_id(self, book_id):
        for book in self.library + self.added_books:
            if book["id"] == book_id:
                return book
        return None

    def find_borrowed_book_by_id(self, book_id):
        for book in self.borrowed_books:
            if book["id"] == book_id:
                return book
        return None

    def book_borrowed_status(self):
        book_id = int(self.entry6.get())
        for book in self.borrowed_books:
            if book["id"] == book_id:
                status = "borrowed"
                messagebox.showinfo("Book Status", f"The book is currently {status}")
                return
        for book in self.library:
            if book["id"] == book_id:
                status = "borrowed" if book["borrowed"] else "available"
                messagebox.showinfo("Book Status", f"The book is currently {status}")
                return
        for book in self.added_books:
            if book["id"] == book_id:
                status = "borrowed" if book["borrowed"] else "available"
                messagebox.showinfo("Book Status", f"The book is currently {status}")
                return
        messagebox.showinfo("Error", "Book not found in the library")

    def clear_entries(self):
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.entry5.delete(0, 'end')
        self.entry6.delete(0, 'end')

root = Tk()
app = LibraryManagementSystem(root)
root.mainloop()
