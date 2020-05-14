from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database import Base


class ProjectType(Base):
    __tablename__ = "project_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=50))
    format_title = Column(String, ForeignKey("format.title"))

    projects = relationship(
        "Project",
        secondary="project_types",
        back_populates="project_types"
    )

    def __repr__(self):
        return f"{self.title} type"
