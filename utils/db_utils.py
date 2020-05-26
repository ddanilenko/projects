from werkzeug.exceptions import NotFound

from database import session


def base(func):
    def wrap(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseException as e:
            session.rollback()
            return {"message": e.args}, 500

    return wrap


def create(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        session.add(result)
        session.commit()
        return result, 201

    return wrap


def get(func):
    def wrap(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result, 200
        except NotFound as e:
            return {"message": e.description}, 404

    return wrap


def update(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        session.commit()
        return result, 200

    return wrap


def delete(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        session.delete(result)
        session.commit()
        return [], 200

    return wrap
