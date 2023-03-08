from ast import Str
from sqlalchemy import BigInteger, String,Column,sql
from utils.tb_api.tb_yura import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = "users"
    user_id = Column(BigInteger,primary_key = True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    username = Column(String(200))
    referral_id = Column(BigInteger)
    status = Column(String(30))


    query: sql.select

