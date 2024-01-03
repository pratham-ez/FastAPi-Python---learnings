from sqlalchemy.orm import declarative_base , sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote

# Replace 'your_username', 'Your@Password123', and 'your_database' with your actual credentials
username = 'postgres'
password = 'Pratham123'
hostname = 'localhost'
port = 5432
database = 'Person'

# URL encode the password
encoded_password = quote(password)

# Create the connection URL
connection_url = f"postgresql://{username}:{encoded_password}@{hostname}/{database}"

# Create the engine
engine = create_engine(connection_url, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)