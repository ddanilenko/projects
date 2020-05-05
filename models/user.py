from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, PasswordType
from sqlalchemy_utils import force_auto_coercion

from database import Base

force_auto_coercion()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(length=50))
    last_name = Column(String(length=50))
    email = Column(EmailType(length=50))
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ))
    city = Column(String)
    district = Column(String)
    projects = relationship(
        "Project",
        secondary="project_responsibility",
        back_populates="responsible"
    )
    roles = relationship(
        "Role",
        secondary="user_roles",
        back_populates="users"
    )

    def __repr__(self):
        return f"{self.first_name} {self.last_name} from {self.city}"
