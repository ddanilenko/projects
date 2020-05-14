from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship

from models.base_model import BaseModel


class Project(BaseModel):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=200), unique=True)
    description = Column(String(length=1200))
    level_title = Column(String, ForeignKey("level.title"))
    status_title = Column(String, ForeignKey("status.title"))
    format_title = Column(String, ForeignKey("format.title"))
    author_id = Column(Integer, ForeignKey("user.id"))
    tags = Column(ARRAY(String(length=50)))

    project_types = relationship(
        "ProjectType",
        secondary="project_types",
        back_populates="projects"
    )
    responsible = relationship(
        "User",
        secondary="project_responsibility",
        back_populates="projects"
    )
    project_votes = relationship(
        "User",
        secondary="user_project_votes",
        back_populates="votes"
    )

    def __repr__(self):
        return f"This is the {self.title} project from {self.author} and it has {self.status} status"
