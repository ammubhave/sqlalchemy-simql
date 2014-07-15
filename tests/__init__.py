from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils import Factory


def setup_db(self):
    """Setup initial db and models"""
    self.engine = create_engine('simql://')
    #Base.metadata.create_all(self.engine)
    Session = sessionmaker()
    Session.configure(bind=self.engine)
    self.session = Session()
    self.factory = Factory(self.session)
