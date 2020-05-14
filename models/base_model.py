from database import Base


class BaseModel(Base):
    __abstract__ = True

    def add_associates(self, associated_type, associated_list):
        self.__getattribute__(associated_type).extend(associated_list)
