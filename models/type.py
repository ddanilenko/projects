from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Type(Base):
    __tablename__ = "type"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    format_id = Column(Integer, ForeignKey("format.id"))

    # projects =

    def __repr__(self):
        return f"{self.title} type"
