from sqlalchemy import BigInteger,ForeignKey, Column,  Integer, MetaData, String, create_engine, select
from sqlalchemy.orm import  registry, declarative_base, Session, mapped_column,Mapped

engine = create_engine("sqlite:///:memory:",echo=True)
Base = declarative_base()

class AbstractModel(Base, object):
    __tablename__ = 'AbstractModel'
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

class UserModel(Base, AbstractModel):
    __tablename__ = 'users'
    user_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column()
    fullname: Mapped[str] = mapped_column()

class AdressModel(Base, AbstractModel):
    __tablename__ = 'addressess'
    email: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

with Session(engine) as session:
    with session.begin():
        Base.metadata.create_all(engine)
        user = UserModel(user_id = 1, name = "Kek", fullname = 'Full Name')
        session.add(user)
    with session.begin():
        res = session.execute(select(UserModel).where(UserModel.id == 1 ))
        print(res.scalar())