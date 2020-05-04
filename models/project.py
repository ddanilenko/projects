from sqlalchemy import Column, Integer, String, BLOB, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

from database import Base


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    description = Column(String)
    image = Column(BLOB)
    level_title = Column(Integer, ForeignKey("level.title"))
    status_title = Column(Integer, ForeignKey("status.title"))
    format_title = Column(Integer, ForeignKey("format.title"))

    # tags =
    # types =
    # author =
    # responsible =

    def __repr__(self):
        return f"This is the '{self.title}' project from {self.author} and it " \
               f"has {self.status} status"
