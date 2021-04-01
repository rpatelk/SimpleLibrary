import Book
class Library:

    __libraryName = ""
    __address = ""
    __listOfBooks = []

    def __init__(libraryName, address, listOfBooks):
        setLibraryName(libraryName)
        setAddress(address)
        setListOfBooks(listOfBooks)

    # Getter and Setter methods for each variable.

    def getLibraryName():
        return self.__libraryName

    def setLibraryName(libraryName):
        self.__libraryName = libraryName

    def getAddress():
        return self.__address

    def setAddress(address):
        self.__address = address

    def getListOfBooks():
        return self.listOfBooks

    def setListOfBooks(listOfBooks):
        self.__listOfBooks = listOfBooks

