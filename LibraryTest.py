import unittest
from Book import Book
from Library import Library

# Test class for Library class
# @author Raj Patel
class BookTest(unittest.TestCase):

    # Tests the methods associated with library name.
    def test_name(self): 
        b = Book("Hatchet", "Gary Paulsen", "Survival, Fiction", "61743")
        b2 = Book("Outsiders", "S. E. Hinton", "Drama, Fiction", "52963")
        books = [b, b2]
        l = Library("Hello Library", "123 Hello World", books)

        # Passing Test
        self.assertEqual(l.getLibraryName(), "Hello Library")
        l.setLibraryName("Simple Library")
        self.assertEqual(l.getLibraryName(), "Simple Library")

        # Failing Test
        l.setLibraryName("Hello Library")
        self.assertNotEqual(l.getLibraryName(), "Simple Library")
        l.setLibraryName("Simple Library")
        self.assertNotEqual(l.getLibraryName(), "Hello Library")

    # Tests the methods associated with address.
    def test_name(self): 
        b = Book("Hatchet", "Gary Paulsen", "Survival, Fiction", "61743")
        b2 = Book("Outsiders", "S. E. Hinton", "Drama, Fiction", "52963")
        books = [b, b2]
        l = Library("Hello Library", "123 Hello World", books)

        # Passing Test
        self.assertEqual(l.getAddress(), "123 Hello World")
        l.setAddress("456 Simple Library St.")
        self.assertEqual(l.getAddress(), "456 Simple Library St.")

        # Failing Test
        l.setAddress("123 Hello World")
        self.assertNotEqual(l.getAddress(), "456 Simple Library St.")
        l.setAddress("456 Simple Library St.")
        self.assertNotEqual(l.getAddress(), "123 Hello World")

    # Tests the methods associated with list of books.
    def test_name(self): 
        b = Book("Hatchet", "Gary Paulsen", "Survival, Fiction", "61743")
        b2 = Book("Outsiders", "S. E. Hinton", "Drama, Fiction", "52963")
        books = [b, b2]
        l = Library("Hello Library", "123 Hello World", books)

        # Test Size of Book list.
        self.assertEqual(len(l.getListOfBooks()), 2)

        # Add new book and test size.
        b3 = Book("Tangerine", "Edward Bloor", "Fiction", "10446") 
        l.getListOfBooks().append(b3)
        # Fail
        self.assertNotEqual(len(l.getListOfBooks()), 2)
        # Pass
        self.assertEqual(len(l.getListOfBooks()), 3)

        #Test correct books
        list = l.getListOfBooks()
        self.assertEqual(list[0].toString(), "Name: Hatchet\nAuthor: Gary Paulsen\nGenre: Survival, Fiction\nId: 61743\nChecked In: Yes")
        self.assertEqual(list[1].toString(), "Name: Outsiders\nAuthor: S. E. Hinton\nGenre: Drama, Fiction\nId: 52963\nChecked In: Yes")
        self.assertEqual(list[2].toString(), "Name: Tangerine\nAuthor: Edward Bloor\nGenre: Fiction\nId: 10446\nChecked In: Yes")

if __name__ == '__main__':
    unittest.main()