import json 
from dataclasses import dataclass,asdict

FILE="books.json" 

@dataclass
class Book:
    title:str
    author:str
    read: bool=False


def load_books() -> list[Book]:
    try:
        with open(FILE, encoding="utf-8") as f:
            return [Book(**item) for item in json.load(f)]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: books.json is empty or damaged. Starting with an empty list.")
        return []

def save_books(books: list[Book])-> None:
    with open(FILE,'w',encoding="utf-8")as f:
        json.dump([asdict(b) for b in books],f,indent=2)



def ask_number(books: list[Book], prompt: str) -> int | None:
    """Ask for a book number. Return None if it is not valid."""
    try:
        number = int(input(prompt))
    except ValueError:
        print("Please type a number.")
        return None
    if not 1 <= number <= len(books):
        print("That number is not in the list.")
        return None
    return number

def add_book(books: list[Book]) -> None:
    title=str(input("Type your title:")).strip()
    if not title:
        print("The titlr cant be empty")
        return
    author=str(input("Enter your author:"))
    books.append(Book(title,author))    
    save_books(books)
    print("---Books Added----")


def show_book(books: list[Book])->None:
    if not books:
        print("book not found")
        return
    save_books(books)
    for number, b in enumerate(books,start=1):
        mark="x" if b.read else " "
        print(f"{number}.{mark} {b.title}-{b.author}")
        
def mark_read(books: list[Book]) -> None:
    if not books:
        print("No books yet.")
        return
    show_book(books)
    number = ask_number(books, "Number of the book you finished: ")
    if number is None:
        return
    books[number - 1].read = True
    save_books(books)
    print("Marked as read.")

def delete_book(books:list[Book])->None:
    if not books:
        print("Book Not Found")
        return
    show_book(books)
    number = ask_number(books, "Number of the book to delete: ")
    if number is None:
        return
    removed=books.pop(number-1)
    save_books(books)
    print(f"Deleted{removed.title}")

def main():
    books=load_books()
    
    while True:
        print("\n 1.ADD \n 2. list \n 3.Delete \n 4.mark as read \n5.Quit")
        choice=input("Enter Your Choice:")
        if choice=="1":
            add_book(books)
        elif choice=="2":
            show_book(books)
        elif choice=="3":
            delete_book(books)
        elif choice=="4":

            mark_read(books)
        elif choice=="5":
            print("bye")
            break
        else:
            print("Invalid choice")


if __name__=="__main__":
    main()
