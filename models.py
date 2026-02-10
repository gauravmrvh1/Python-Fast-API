from sqlalchemy import (
    Integer,
    BigInteger,
    String,
    Text,
    Boolean,
    Float,
    Numeric,
    Date,
    DateTime,
    Time,
    Enum,
    JSON,
    LargeBinary,

    Column,
    ForeignKey,
    UniqueConstraint,
    CheckConstraint,
    Index,
    func,
    text
)
from sqlalchemy.dialects.mysql import (
    TINYINT,
    MEDIUMINT,
    BIGINT,
    VARCHAR,
    LONGTEXT
)
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "pt_awc_users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    mobile_number  = Column(BigInteger, nullable=False, unique=True)
    aadhar_number  = Column(BigInteger, nullable=True, unique=True)

class Admin(Base):
    __tablename__ = "pt_admins"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(150), unique=True, index=True, nullable=False)