# 

import datetime
from sqlalchemy import (Column, Integer, String, Date, DateTime)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

from spotify_app.models.user import (association_table, Base)

# Base = declarative_base()


class Track(Base):
    __tablename__ = 'tracks'
    id = Column(Integer, primary_key=True)    
    
    title = Column(String)
    artist = Column(String)
    album = Column(String)
    timestamp = Column(DateTime)
    played_at = Column(Date)
    inserted_at = Column(DateTime, default=datetime.datetime.utcnow)    
    # users = relationship("User", secondary=association_table, backref='track')
    
    
    def __repr__(self):
        return f"<Track(title='{self.title}')>"

