from sqlalchemy import Column, Integer, ForeignKey

from database import Base


class ProjectResponsibility(Base):
    __tablename__ = "project_responsibility"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("project.id"))
    responsible_id = Column(Integer, ForeignKey("user.id"))
