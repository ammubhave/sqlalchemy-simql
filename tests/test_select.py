import unittest
from models import User
from tests import setup_db
from unittest import TestCase


class TestSelectStatement(TestCase):

    def setUp(self):
        setup_db(self)

    def test_normal_select(self):
        user = self.factory.create_user()
        users = self.session.query(User)
        self.assertEqual(1, len(users.all()))
        self.assertEqual(user, users[0])

if __name__ == '__main__':
    unittest.main()
