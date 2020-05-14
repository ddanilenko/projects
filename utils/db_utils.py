from sqlalchemy.exc import IntegrityError

from database import session


def base(func):
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IntegrityError as e:
            session.rollback()
            return {"message": e._message().split("=(")[1].split("\n")[0]}

    return wrap


def create(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        session.add(result)
        session.commit()
        return result

    return wrap
