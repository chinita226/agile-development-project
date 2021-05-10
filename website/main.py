from website import create_app, db
from website.config import DevSettings

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
