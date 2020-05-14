from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=50))

    users = relationship(
        "User",
        secondary="user_roles",
        back_populates="roles"
    )

    def __repr__(self):
        return f"{self.title} role"
