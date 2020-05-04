from app import app
from database import Base, engine


def main(args=None):
    Base.metadata.create_all(engine)
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pass
