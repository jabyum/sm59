"""
1- User (username, phone_number, email, city, birthday, password, reg_date)
2- Photo (photo_path, post_id, profile_id, photo_date)
3- Hashtags (name)
4- Post(user_id, text, hashtag, post_date)
5- Comment (user_id, text, post_id, com_date)
"""
from sqlalchemy import (Column, Integer,
                        String, ForeignKey, Date, DateTime)
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base
from pytz import timezone
tashkent_tz = timezone("Asia/Tashkent")
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    city = Column(String, nullable=True)
    birthday = Column(Date, nullable=True)
    password = Column(String)
    reg_date = Column(DateTime, default=datetime.now(tashkent_tz))
    post_fk = relationship("Post", back_populates="user_fk")

class Photo(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    photo_path = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=True)
    profile_id = Column(Integer, ForeignKey('userinfo.id'), nullable=True)
    photo_date = Column(DateTime, default=datetime.now(tashkent_tz))
    user_fk = relationship('User', lazy='subquery')
    post_fk = relationship('Post', lazy='subquery')
class Hashtag(Base):
    __tablename__ = 'hashtag'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    text = Column(String, nullable=True)
    hashtag = Column(String, ForeignKey("hashtag.name"))
    post_date = Column(DateTime, default=datetime.now(tashkent_tz))
    user_fk = relationship("User", lazy="subquery", back_populates="post_fk",
                           cascade="all, delete", passive_deletes=True)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    text = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))
    com_date = Column(DateTime, default=datetime.now(tashkent_tz))
    user_fk = relationship("User", lazy="subquery")
    post_fk = relationship("Post", lazy="subquery")