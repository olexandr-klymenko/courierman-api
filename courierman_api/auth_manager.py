from fastapi_login import LoginManager

SECRET = "3e7d146240317ce9a5581aee8e27488e51fca138187e6798"

manager = LoginManager(SECRET, tokenUrl="/api/auth/token")

fake_db = {"101": {"password": "101"}}


@manager.user_loader
def load_user(phone_number: str):
    user = fake_db.get(phone_number)
    return user
