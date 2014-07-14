import datetime
import exceptions
from connection import Connection
from errors import *


def connect(*args, **kwargs):
    return Connection(*args, **kwargs)

# DBAPI2 Constants

threadsafety = 1
apilevel = "2.0"
paramstyle = "pyformat"

# Data Types & Constructors

Date = datetime.date
Time = datetime.time
Timestamp = datetime.datetime


def DateFromTicks(ticks):
    return Date(*time.localtime(ticks)[:3])


def TimeFromTicks(ticks):
    return Time(*time.localtime(ticks)[3:6])


def TimestampFromTicks(ticks):
    return Timestamp(*time.localtime(ticks)[:6])


Binary = memoryview
STRING = str
BINARY = buffer
NUMBER = int
DATETIME = int
ROWID = int
