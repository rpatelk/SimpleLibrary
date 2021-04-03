class Book:

    __name = ""
    __author = ""
    __genre = ""
    __unqiueId = ""
    __checkedIn = True

    def __init__(self, name, author, genre, unqiueId):
        self.setName(name)
        self.setAuthor(author)
        self.setGenre(genre)
        self.setId(unqiueId)

    # Getter and Setter methods for each variable.    

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getAuthor(self):
        return self.__author

    def setAuthor(self, author):
        self.__author = author
    
    def getGenre(self):
        return self.__genre

    def setGenre(self, genre):
        self.__genre = genre

    def getId(self):
        return self.__unqiueId

    def setId(self, unqiueId):
        self.__unqiueId = unqiueId
    
    def getCheckedIn(self):
        return self.__checkedIn

    def setCheckedIn(self, checkedIn):
        self.__checkedIn = checkedIn

    def toString(self):
        status = ""
        if self.__checkedIn == True:
            status = "Yes"
        else:
            status = "No"
        return "Name: " + self.__name + "\n" + "Author: " + self.__author + "\n" + "Genre: " + self.__genre + "\n" + "Id: " + self.__unqiueId + "\n" + "Checked In: " + status