from sqlalchemy import Integer, Column, String

from database import Base


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer)
    title = Column(String)

    # projects =

    def __repr__(self):
        return f"this is a {self.title} tag"
