import random
import string
from models import User


def _generate_str(length=5, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(length))


def _generate_int(low=0, hi=10000):
    return random.choice(range(low, hi))


class Factory():
    def __init__(self, session):
        self.session = session

    def create_user(self, name=_generate_str(), age=_generate_int()):
        user = User(name=name, age=age)
        self.session.add(user)
        self.session.commit()
        return user
