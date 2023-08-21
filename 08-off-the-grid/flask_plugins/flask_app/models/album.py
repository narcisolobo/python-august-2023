from flask_app.extensions import db
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Album(db.Model):
    __tablename__ = "albums"
    query = db.session.query_property()

    id = Column(Integer, primary_key=True, autoincrement="auto")
    title = Column(String(45), nullable=False)
    artist = Column(String(45), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    creator = relationship("User", backref="albums")
