import sqlalchemy
from server import db_handler as _database


class User(_database.Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    login = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    password = sqlalchemy.Column(sqlalchemy.String)
    discription = sqlalchemy.Column(sqlalchemy.String)