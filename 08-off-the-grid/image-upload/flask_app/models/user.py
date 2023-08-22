from flask_login import UserMixin
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from flask_app.extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False, unique=True)
    profile_pic = Column(String(60), nullable=False, server_default="default.png")
    password = Column(String(60), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
