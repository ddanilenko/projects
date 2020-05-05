from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database import Base


class Level(Base):
    __tablename__ = "level"

    title = Column(String(length=50), primary_key=True)

    projects = relationship("Project")

    def __repr__(self):
        return f"{self.title} level"
