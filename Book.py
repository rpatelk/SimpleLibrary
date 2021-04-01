class Book:

    __name = ""
    __author = ""
    __genre = ""
    __checkedIn = True

    def __init__(name, author, genre):
        setName(name)
        setAuthor(author)
        setGenre(genre)

    # Getter and Setter methods for each variable.    

    def getName():
        return self.__name

    def setName(name):
        self.__name = name

    def getAuthor():
        return self.__author

    def setAuthor(author):
        self.__author = author
    
    def getGenre():
        return self.__genre

    def setGenre(genre):
        self.__genre = genre
    
    def getCheckedIn():
        return self.__checkedIn

    def setCheckedIn(checkedIn):
        self.__checkedIn = checkedIn

    def toString():
        return "Name: " + self.__name + "\n" + "Author: " + self.__author + "\n" + "Genre: " + self.__genre + "\n" + "Checked In: " + self.__checkedIn