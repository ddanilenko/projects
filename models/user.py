from sqlalchemy import Column, Integer, String, BLOB, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType, PasswordType

from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(EmailType)
    password = Column(PasswordType(
                schemes=[
                    'pbkdf2_sha512',
                    'md5_crypt'
                ],
                deprecated=['md5_crypt']
            ))
    city = Column(String)
    district = Column(String)
    # role_id =
    #
    # projects =
    # role =

    def __repr__(self):
        return f"{self.first_name} {self.last_name} from {self.city}"
