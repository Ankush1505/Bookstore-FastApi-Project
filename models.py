from database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, Float, text, ForeignKey

class Book(Base):

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE')
    price = Column(Float, nullable=False, server_default='0.0')
    inventory = Column(Integer, nullable=False, server_default='0')

    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))

class Vote(Base):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True, nullable=False)
