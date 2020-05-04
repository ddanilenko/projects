from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Level(Base):
    __tablename__ = "level"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    projects = relationship("Project")

    def __repr__(self):
        return f"{self.title} level"
