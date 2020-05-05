from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database import Base


class Role(Base):
    __tablename__ = "role"

    title = Column(String(length=50), primary_key=True)

    users = relationship(
        "User",
        secondary="user_roles",
        back_populates="roles"
    )

    def __repr__(self):
        return f"{self.title} role"
