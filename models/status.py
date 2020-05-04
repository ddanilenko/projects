from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database import Base


class Status(Base):
    __tablename__= "status"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    projects = relationship("Project")

    def __repr__(self):
        return f"This is the {self.title} status"
