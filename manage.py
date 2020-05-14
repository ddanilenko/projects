from app import app


def main(args=None):
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pass
