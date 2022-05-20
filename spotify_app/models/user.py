# 
from sqlalchemy import (Table, Column, Integer, String, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

association_table = Table('user_tracks', Base.metadata,
    Column('id', Integer, primary_key=True),                          
    Column('user_id', ForeignKey('users.id')),
    Column('track_id', ForeignKey('tracks.id')),
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nickname = Column(String)    
    # M-M relationship
    tracks = relationship("Child", secondary=association_table, backref='user')
    

    def __repr__(self):
        return f"<User(nickname='{self.nickname}')>"

