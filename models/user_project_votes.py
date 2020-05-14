from sqlalchemy import Column, Integer, ForeignKey

from database import Base


class UserProjectVotes(Base):
    __tablename__ = "user_project_votes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("project.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
