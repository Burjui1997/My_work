from sqlalchemy import create_engine, Integer, String, Column, select, update, delete, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("database_url")


def create_engine(database_url):
    engine = create_engine(database_url)
    return engine


def get_session(engine):
    session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    return session


Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    UserID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    Password = Column(String, nullable=True)
    Email = Column(String)
    VKID = Column(String, nullable=True)
    id = Column(Integer, ForeignKey("Users.UserID"), nullable=False)


def add_user(session, user_data: dict):
    user = User(**user_data)
    session.add(user)
    session.commit()
    return user.UserID


def get_user_by_id(session, id: int):
    user = session.select(User).filter(User.UserID == id).first()
    return {
        'UserID': user.id,
        'FirstName': user.FirstName,
        'LastName': user.LastName,
        'Password': user.Password,
        'Email': user.Email,
        'VKID': user.VKID
    }


def get_all_users(session):
    users = session.select(User).all()
    result = []
    for user in users:
        result.append({
            'UserID': user.UserID,
            'FirstName': user.FirstName,
            'LastName': user.LastName,
            'Password': user.Password,
            'Email': user.Email,
            'VKID': user.VKID
        })
    return result


def update_user(session, user_data):
    user = session.select(User).filter(User.UserID == user_data['UserID']).first()
    user.FirstName = user_data['FirstName']
    user.LastName = user_data['LastName']
    user.Password = user_data['Password']
    user.Email = user_data['Email']
    user.VKID = user_data['VKID']
    session.commit()
    return user.UserID


def delete_user_by_id(session, id: int):
    user = session.select(User).filter_by(UserID=id)
    session.delete(user)
    session.commit()
    return user.UserID
