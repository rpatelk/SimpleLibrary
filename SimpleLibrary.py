from Library import Library
from Book import Book
libraries = []

def generate():
    global libraries
    book1 = Book("Hatchet", "Gary Paulsen", "Survival, Fiction", "61743")
    book2 = Book("Outsiders", "S. E. Hinton", "Drama, Fiction", "52963")
    book3 = Book("Tangerine", "Edward Bloor", "Fiction", "10446")
    book4 = Book("1984", "George Orwell", "Fiction", "77104")
    listOfBooks1 = [book1, book2, book3, book4]
    library1 = Library("Hello Library", "123 Hello World", listOfBooks1)
    libraries = [library1]

def checkOut():
    id = input("Enter book id: ")
    for x in libraries:
        for y in x.getListOfBooks():
            check = y.getId()
            if check == id:
                if y.getCheckedIn() == True:
                    y.setCheckedIn(False)
                    print(y.getName(), "was successfully checked out!")
                    break
                else:
                    print(y.getName(), "is already checked out.")

def nameSearch():
    name = input("Enter name of book: ")
    name = name.lower()
    print()
    for x in libraries:
        for y in x.getListOfBooks():
            check = y.getName().lower()
            if check == name:
                print(y.toString())
                print("Location:", x.getLibraryName())
                print("Location address:", x.getAddress())

def authorSearch():
    author = input("Enter author of book: ")
    author = author.lower()
    print()
    for x in libraries:
        for y in x.getListOfBooks():
            check = y.getAuthor().lower()
            if check == author:
                print(y.toString())
                print("Location:", x.getLibraryName())
                print("Location address:", x.getAddress())

def genreSearch():
    genre = input("Enter genre of book: ")
    genre = genre.lower()
    print()
    for x in libraries:
        for y in x.getListOfBooks():
            check = y.getGenre().lower()
            if genre in check:
                print(y.toString())
                print("Location:", x.getLibraryName())
                print("Location address:", x.getAddress())

def main():
    global libraries
    generate()

    print("Welcome to SimpleLibrary.")

    while (True):
        print()
        print("1. Search for a book by name.")
        print("2. Search for a book by author.")
        print("3. Search for a book by genre.")
        print("4. Checkout book.")
        print("5. Quit")
        print()
        num = 0;
        while (num == 0):
            num = input("Choose an option: ")
            if num == "1" or num == "2" or num == "3" or num == "4" or num == "5":
                break
            else:
                num = 0
        
        if num == "1":
            nameSearch()
        
        elif num == "2":
            authorSearch()

        elif num == "3":
            genreSearch()

        elif num == "4":
            checkOut()

        elif num == "4":
            return

    

if __name__ == "__main__":
    main()