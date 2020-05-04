from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Format(Base):
    __tablename__ = "format"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    types = relationship("Type")
    projects = relationship("Project")

    def __repr__(self):
        return f"{self.title} format"
