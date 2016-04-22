from sqlalchemy import Column, Enum, LargeBinary, String

from database import Base

class User(Base):
    __tablename__ = 'users'

    username = Column(String(length=64), nullable=False, primary_key=True)
    _password = Column(LargeBinary(length=32), nullable=False, name='password')
    email = Column(String(length=256), nullable=False)
    role = Column(Enum('admin', 'user', name='role'), nullable=False)

    @property
    def password(self):
        return self._password
