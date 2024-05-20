class Item:
    """
    The base class for all library items.
    """

    def __init__(self, title, author_director, publication_release_year):
        self.title = title
        self.author_director = author_director
        self.publication_release_year = publication_release_year
        self._is_available = True  # Private attribute to track availability

    def is_available(self):
        """
        Returns True if the item is available, False otherwise.
        """
        return self._is_available

    def borrow(self):
        """
        Marks the item as borrowed if available.
        """
        if self._is_available:
            self._is_available = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"Sorry, {self.title} is not available for borrowing.")

    def return_(self):
        """
        Marks the item as returned.
        """
        self._is_available = True
        print(f"{self.title} has been returned.")


class Book(Item):
    """
    A subclass of Item for books.
    """

    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre

    def display_info(self):
        """
        Displays information about the book.
        """
        print(
            f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_release_year}, Genre: {self.genre}"
        )


class Audiobook(Book):
    """
    A subclass of Book for audiobooks, inheriting all attributes and methods from Book.
    """

    pass


class Movie(Item):
    """
    A subclass of Item for movies.
    """

    def __init__(self, title, director, release_year, runtime):
        super().__init__(title, director, release_year)
        self.runtime = runtime

    def display_info(self):
        """
        Displays information about the movie.
        """
        print(
            f"Title: {self.title}, Director: {self.author_director}, Release Year: {self.publication_release_year}, Runtime: {self.runtime} minutes"
        )


def main():
    """
    The main function to run the library management system.
    """

    # Create some library items
    book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954, "Fantasy")
    audiobook1 = Audiobook(
        "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, "Science Fiction"
    )
    movie1 = Movie("The Shawshank Redemption", "Frank Darabont", 1994, 142)

    # Borrow and return items
    book1.borrow()
    movie1.borrow()
    audiobook1.return_()

    # Display information about the items
    book1.display_info()
    print(f"Available: {book1.is_available()}")
    movie1.display_info()
    print(f"Available: {movie1.is_available()}")
    audiobook1.display_info()
    print(f"Available: {audiobook1.is_available()}")


if __name__ == "__main__":
    main()
