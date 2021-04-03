from Book import Book

# Class that contaians the Object for Library
# @author Raj Patel
class Library:

    # Important library infromation including book list.
    __libraryName = ""
    __address = ""
    __listOfBooks = []

    # Library class constructor
    def __init__(self, libraryName, address, listOfBooks):
        self.setLibraryName(libraryName)
        self.setAddress(address)
        self.setListOfBooks(listOfBooks)

    # Getter and Setter methods for each variable.

    def getLibraryName(self):
        return self.__libraryName

    def setLibraryName(self, libraryName):
        self.__libraryName = libraryName

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def getListOfBooks(self):
        return self.__listOfBooks

    def setListOfBooks(self, listOfBooks):
        self.__listOfBooks = listOfBooks

