from datetime import datetime
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import func
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, column_property

class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.now)
  udpated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
  user = relationship('User')
  comments = relationship('Comment', cascade='all,delete')
  votes = relationship('Vote', cascade='all,delete')
  # totalling the votes for the post
  vote_count = column_property(
    select([func.count(Vote.id)]).where(Vote.post_id == id)
  )