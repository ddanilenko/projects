from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database import Base


class Status(Base):
    __tablename__ = "status"

    title = Column(String(length=50), primary_key=True)

    projects = relationship("Project")

    def __repr__(self):
        return f"This is the {self.title} status"
