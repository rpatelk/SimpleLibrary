import unittest
from Book import Book

# Test class for Book class
# @author Raj Patel
class BookTest(unittest.TestCase):

    # Tests the methods associated with name.
    def test_name(self): 
        b = Book("Hatchet", "Gary Paulsen", "Survival, Fiction", "61743")

        # Passing Test
        self.assertEqual(b.getName(), "Hatchet")
        b.setName("Harry Potter")
        self.assertEqual(b.getName(), "Harry Potter")

        # Failing Test
        b.setName("Hatchet")
        self.assertNotEqual(b.getName(), "Harry Potter")
        b.setName("Harry Potter")
        self.assertNotEqual(b.getName(), "Hatchet")

    # Tests the methods associated with author.
    def test_name(self): 
        b = Book("Hatchet", "Gary Paulsen", "Survival, Fiction", "61743")

        # Passing Test
        self.assertEqual(b.getAuthor(), "Gary Paulsen")
        b.setAuthor("Tolkien")
        self.assertEqual(b.getAuthor(), "Tolkien")

        # Failing Test
        b.setAuthor("Gary Paulsen")
        self.assertNotEqual(b.getAuthor(), "Tolkien")
        b.setAuthor("Tolkien")
        self.assertNotEqual(b.getAuthor(), "Gary Paulsen")

    # Tests the methods associated with genre.
    def test_name(self): 
        b = Book("Hatchet", "Gary Paulsen", "Survival, Fiction", "61743")

        # Passing Test
        self.assertEqual(b.getGenre(), "Survival, Fiction")
        b.setGenre("Thriller")
        self.assertEqual(b.getGenre(), "Thriller")

        # Failing Test
        b.setGenre("Survival, Fiction")
        self.assertNotEqual(b.getGenre(), "Thriller")
        b.setGenre("Thriller")
        self.assertNotEqual(b.getGenre(), "Survival, Fiction")

    # Tests the methods associated with id.
    def test_name(self): 
        b = Book("Hatchet", "Gary Paulsen", "Survival, Fiction", "61743")

        # Passing Test
        self.assertEqual(b.getId(), "61743")
        b.setId("43591")
        self.assertEqual(b.getId(), "43591")

        # Failing Test
        b.setId("61743")
        self.assertNotEqual(b.getId(), "43591")
        b.setId("43591")
        self.assertNotEqual(b.getId(), "61743")

    # Tests the methods associated with checkedin status.
    def test_name(self): 
        b = Book("Hatchet", "Gary Paulsen", "Survival, Fiction", "61743")

        self.assertTrue(b.getCheckedIn())
        b.setCheckedIn(False)
        self.assertFalse(b.getCheckedIn())

    # Tests toString() method.
    def test_name(self): 
        b = Book("Hatchet", "Gary Paulsen", "Survival, Fiction", "61743")

        # Initial Test
        self.assertEqual(b.toString(), "Name: Hatchet\nAuthor: Gary Paulsen\nGenre: Survival, Fiction\nId: 61743\nChecked In: Yes")

        # Update book params
        b.setName("Lord of the Rings")
        b.setAuthor("Tolkien")
        b.setGenre("Fantasy, Fiction")
        b.setId("43591")
        b.setCheckedIn(False)

        # Test changes

        # Original Assertion Fails
        self.assertNotEqual(b.toString(), "Name: Hatchet\nAuthor: Gary Paulsen\nGenre: Survival, Fiction\nId: 61743\nChecked In: Yes")

        # New Assertion Passes
        self.assertEqual(b.toString(), "Name: Lord of the Rings\nAuthor: Tolkien\nGenre: Fantasy, Fiction\nId: 43591\nChecked In: No")


if __name__ == '__main__':
    unittest.main()