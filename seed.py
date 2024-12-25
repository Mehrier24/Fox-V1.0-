
from models import User, Book
from extensions import db

# Initialize database
db.create_all()

# Add sample books
book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald")
book2 = Book(title="1984", author="George Orwell")
book3 = Book(title="To Kill a Mockingbird", author="Harper Lee")

db.session.add_all([book1, book2, book3])
db.session.commit()

print("Database seeded!")
