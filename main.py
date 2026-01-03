from library_system import LibrarySystem

def populate_library(lib):
    """Helper function to load 50+ books and 20 members."""
    
    # --- 1. Data: List of 52 Books (ISBN, Title, Author, Year, Category, Copies) ---
    books_data = [
        # Programming Classics
        ("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programming", 3),
        ("9780132350884", "Clean Code", "Robert Martin", 2008, "Programming", 5),
        ("9780132350885", "Clean Architecture", "Robert Martin", 2017, "Programming", 4),
        ("9780201633610", "Design Patterns", "Erich Gamma", 1994, "Programming", 2),
        ("9780134494166", "Clean Agile", "Robert Martin", 2019, "Programming", 3),
        ("9780321125217", "Domain-Driven Design", "Eric Evans", 2003, "Software Eng", 2),
        ("9780201485677", "Refactoring", "Martin Fowler", 1999, "Programming", 3),
        ("9780135957059", "The Pragmatic Programmer", "Andrew Hunt", 1999, "Programming", 4),
        ("9780321356680", "Effective Java", "Joshua Bloch", 2008, "Programming", 5),
        ("9781491901427", "Flask Web Development", "Miguel Grinberg", 2018, "Web Dev", 3),
        
        # Algorithms & Math
        ("9780262033848", "Introduction to Algorithms", "Thomas Cormen", 2009, "Algorithms", 10),
        ("9780321573513", "Algorithms", "Robert Sedgewick", 2011, "Algorithms", 6),
        ("9780486411471", "Calculus Vol 1", "Tom Apostol", 1967, "Mathematics", 4),
        ("9780486411472", "Calculus Vol 2", "Tom Apostol", 1969, "Mathematics", 4),
        ("9781118230718", "Elementary Linear Algebra", "Howard Anton", 2013, "Mathematics", 7),
        
        # AI & Data Science
        ("9781449369415", "Introduction to Machine Learning", "Andreas Muller", 2016, "AI", 4),
        ("9781098108550", "Data Science on AWS", "Chris Fregly", 2021, "Data Science", 3),
        ("9781492032649", "Hands-On Machine Learning", "Aurelien Geron", 2019, "AI", 8),
        ("9781617294631", "Deep Learning with Python", "Francois Chollet", 2017, "AI", 5),
        ("9780262035613", "Deep Learning", "Ian Goodfellow", 2016, "AI", 3),
        
        # Electrical Engineering
        ("9780190698614", "Microelectronic Circuits", "Adel Sedra", 2020, "Electronics", 10),
        ("9780073380575", "Electric Machinery Fundamentals", "Stephen Chapman", 2011, "Power", 5),
        ("9781118152591", "Fundamentals of Electric Circuits", "Charles Alexander", 2016, "Electronics", 8),
        ("9780134608341", "Signals and Systems", "Alan Oppenheim", 1996, "Signal Proc", 6),
        ("9780073529585", "Digital Logic Design", "Morris Mano", 2013, "Digital", 7),
        
        # Physics
        ("9780321973610", "University Physics", "Hugh Young", 2015, "Physics", 10),
        ("9781108422413", "Quantum Mechanics", "David Griffiths", 2018, "Physics", 4),
        ("9780131495081", "Introduction to Electrodynamics", "David Griffiths", 2013, "Physics", 5),
        ("9780071106090", "Concepts of Modern Physics", "Arthur Beiser", 2002, "Physics", 6),
        ("9781400847228", "The Feynman Lectures", "Richard Feynman", 2011, "Physics", 5),

        # Filling the rest with generated entries to ensure we hit 50+
        ("978000000031", "Circuit Analysis I", "John Doe", 2020, "Engineering", 5),
        ("978000000032", "Circuit Analysis II", "John Doe", 2021, "Engineering", 5),
        ("978000000033", "Engineering Mechanics", "Jane Smith", 2019, "Mechanical", 4),
        ("978000000034", "Thermodynamics", "Jane Smith", 2018, "Mechanical", 4),
        ("978000000035", "Fluid Mechanics", "Bob Johnson", 2020, "Mechanical", 3),
        ("978000000036", "Control Systems", "Alice Brown", 2021, "Electrical", 6),
        ("978000000037", "Power Electronics", "Alice Brown", 2022, "Electrical", 6),
        ("978000000038", "Embedded Systems", "Charlie White", 2019, "Electronics", 4),
        ("978000000039", "VLSI Design", "Charlie White", 2020, "Electronics", 4),
        ("978000000040", "Computer Architecture", "David Black", 2018, "Computer", 5),
        ("978000000041", "Operating Systems", "David Black", 2019, "Computer", 5),
        ("978000000042", "Database Systems", "Eva Green", 2020, "Computer", 6),
        ("978000000043", "Compiler Design", "Eva Green", 2021, "Computer", 3),
        ("978000000044", "Computer Networks", "Frank Blue", 2019, "Computer", 7),
        ("978000000045", "Network Security", "Frank Blue", 2020, "Security", 4),
        ("978000000046", "Cyber Security Essentials", "George Red", 2021, "Security", 5),
        ("978000000047", "Ethical Hacking", "George Red", 2022, "Security", 5),
        ("978000000048", "Cloud Computing", "Helen Grey", 2020, "Cloud", 6),
        ("978000000049", "IoT Fundamentals", "Helen Grey", 2021, "IoT", 6),
        ("978000000050", "Robotics Introduction", "Ivan Gold", 2022, "Robotics", 3),
        ("978000000051", "Advanced Robotics", "Ivan Gold", 2023, "Robotics", 3),
        ("978000000052", "Artificial Neural Networks", "Kevin Silver", 2021, "AI", 4)
    ]

    print(f"Loading {len(books_data)} books into the system...")
    for b in books_data:
        lib.add_book(b[0], b[1], b[2], b[3], b[4], b[5])
    print("Books loaded successfully.")

    # --- 2. Data: List of 20 Members ---
    print("\nRegistering 20 Members...")
    for i in range(1, 21):
        # Generates IDs like "2024-EE-001" to "2024-EE-020"
        member_id = f"2024-EE-{i:03d}" 
        name = f"Student {i}"
        lib.add_member(member_id, name)
    print("Members registered successfully.")


def main():
    lib = LibrarySystem()

    # 1. Populate Data
    populate_library(lib)

    # 2. Test Search by Title (Hash Table -> AVL)
    print("\n--- Test 1: Search by Title ---")
    title = "Microelectronic Circuits"
    book = lib.search_by_title(title)
    if book:
        print(f"Found: {book}")
    else:
        print(f"Error: '{title}' not found.")

    # 3. Test Search by Author (Hash Table w/ Collision Handling)
    # Robert Martin has 3 books in our list. The system should find all of them.
    print("\n--- Test 2: Search by Author (Multiple Books) ---")
    author = "Robert Martin"
    books = lib.search_by_author(author)
    print(f"Books by {author} found: {len(books)}")
    for b in books:
        print(f" - {b.title} (ISBN: {b.isbn})")

    # 4. Test Borrowing Logic
    print("\n--- Test 3: Borrowing Logic ---")
    member_id = "2024-EE-005"
    isbn_to_borrow = "9780134685991" # Effective Python
    
    print(f"Student {member_id} is borrowing 'Effective Python'...")
    lib.borrow_book(member_id, isbn_to_borrow)
    
    # Verify copy count decreased
    book_after = lib.search_by_isbn(isbn_to_borrow)
    print(f"Copies remaining: {book_after.available_copies}")

    # 5. Test Borrowing Limit (Max 5 Books)
    print("\n--- Test 4: Borrowing Limit (Edge Case) ---")
    member_limit_test = "2024-EE-010"
    limit_books = [
        "9780132350884", # Clean Code
        "9780201633610", # Design Patterns
        "9780321125217", # DDD
        "9780321356680", # Effective Java
        "9780262033848"  # Intro to Algos
    ]
    
    # Borrow 5 books successfully
    print(f"Student {member_limit_test} borrowing 5 books...")
    for isbn in limit_books:
        lib.borrow_book(member_limit_test, isbn)
    
    # Try to borrow 6th book (Should Fail)
    print("Attempting to borrow 6th book (Should Fail):")
    lib.borrow_book(member_limit_test, "9781491901427") # Flask Web Dev

    # 6. Test Returning
    print("\n--- Test 5: Returning Book ---")
    lib.return_book(member_limit_test, "9780132350884") # Return Clean Code
    print("Returned 1 book. Attempting to borrow 'Flask Web Dev' again (Should Succeed):")
    lib.borrow_book(member_limit_test, "9781491901427")

if __name__ == "__main__":
    main()