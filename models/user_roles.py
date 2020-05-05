from sqlalchemy import Column, Integer, ForeignKey, String

from database import Base


class UserRoles(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    role_title = Column(String, ForeignKey("role.title"))
