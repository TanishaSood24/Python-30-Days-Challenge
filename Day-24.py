from dataclasses import dataclass

@dataclass
class LibraryBook:
    title: str
    author: str
    isbn: str
    publication_year: int

    def display_details(self):
        print("📖 Book Details")
        print("-" * 30)
        print(f"📚 Title           : {self.title}")
        print(f"✍️ Author          : {self.author}")
        print(f"🔖 ISBN            : {self.isbn}")
        print(f"📅 Publication Year: {self.publication_year}")
        print("-" * 30)

    def is_classic(self):
        """Returns True if the book was published over 30 years ago."""
        from datetime import datetime
        current_year = datetime.now().year
        return (current_year - self.publication_year) >= 30

book = LibraryBook(
    title="To Kill a Mockingbird",
    author="Harper Lee",
    isbn="978-0-06-112008-4",
    publication_year=1960
)

book.display_details()

# Check if the book is a classic
if book.is_classic():
    print("🌟 This is a classic book!")
else:
    print("📗 This is a modern book.")