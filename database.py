from dotenv import load_dotenv
import os
from sqlmodel import create_engine, SQLModel
from . import models


# Load the environment variables
load_dotenv()

# Set constants for the database connection
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOSTNAME = os.getenv("DB_HOSTNAME")
DB_DATABASE = os.getenv("DB_DATABASE")

# Create the database connection
postgresql_url = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_DATABASE}"
engine = create_engine(postgresql_url, echo=True)

# Create the tables
SQLModel.metadata.create_all(engine)
