from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    title = Column(String)

    # user =

    def __repr__(self):
        return f"{self.title} role"
