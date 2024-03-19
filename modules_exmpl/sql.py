from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker
from faker.providers import internet
fake = Faker()
# fake = Faker(['ja_JP'])
fake.add_provider(internet)

# Create a SQLite database engine
engine = create_engine('sqlite:///example.db')  # Create an SQLite database engine with logging enabled

# Create a base class for our declarative class definitions
Base = declarative_base()
#
# 	1.	Automatic table creation: When we define our mapped classes (like the User class in the provided code) by subclassing Base, SQLAlchemy can automatically create corresponding database tables for us.
# 	2.	Common functionality: Base includes common functionalities and methods that are shared among all mapped classes, such as querying, metadata handling, and table reflection.
# 	3.	Configuration and conventions: Base allows us to specify global configuration options and conventions for our database models, such as naming conventions for tables and columns.
#
# Overall, using Base = declarative_base() simplifies the process of defining mapped classes and interacting with the database in SQLAlchemy by providing a consistent and convenient base class to build upon.


# Define a class representing a table in the database
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    ipv4 = Column(String)

# Create the tables in the database
Base.metadata.create_all(engine)  # Create tables in the database based on the defined class structures

# Create a session to interact with the database
Session = sessionmaker(bind=engine)  # Create a session factory bound to the database engine
session = Session()  # Create a session object for interacting with the database

# Define a list to store objects
new_users = [
    User(name=fake.name(), age=40, ipv4=fake.ipv4()),
    User(name=fake.name(), age=50, ipv4=fake.ipv4()),
    User(name=fake.name(), age=55, ipv4=fake.ipv4()),
    User(name=fake.name(), age=30, ipv4=fake.ipv4()),  # Generate fake user data including ipv4 address
    User(name=fake.name(), age=35, ipv4=fake.ipv4())
]

# Add objects to the session
session.add_all(new_users)

# Commit the changes to the database
session.commit()

# Query the database for all users
users = session.query(User).all()
for user in users:
    print(user.name, user.age, user.ipv4)

# Drop the tables from the database
# Base.metadata.drop_all(engine)

session.commit()  # Commit the transaction before closing the session
session.close()  # Close the session to release resources