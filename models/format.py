from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database import Base


class Format(Base):
    __tablename__ = "format"

    title = Column(String(length=50), primary_key=True)

    project_types = relationship("ProjectType")
    projects = relationship("Project")

    def __repr__(self):
        return f"{self.title} format"
