from sqlalchemy import Column, Integer, ForeignKey

from database import Base


class ProjectTypes(Base):
    __tablename__ = "project_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("project.id"))
    project_type_id = Column(Integer, ForeignKey("project_type.id"))
