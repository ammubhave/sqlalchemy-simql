from models import Base
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import sessionmaker
from utils import Factory


def setup_db(self):
    """Setup initial db and models"""
    self.engine = create_engine('sqlite://')
    Base.metadata.create_all(self.engine)
    Session = sessionmaker()
    Session.configure(bind=self.engine)
    self.session = Session()
    self.factory = Factory(self.session)
