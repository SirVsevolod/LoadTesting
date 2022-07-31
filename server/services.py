import sqlalchemy.orm as _orm

from server import db_handler as _db, models as _models, shema as _schemas


def create_database():
    return _db.Base.metadata.create_all(bind=_db.engine)


def get_db():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(db: _orm.Session, user_id: int):
    return db.query(_models.User).filter(_models.User.id == user_id).first()


def create_user(db: _orm.Session, user: _schemas.CreateUser):

    db_user = _models.User(login=user.login, password=user.password, discription=user.discription)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_login(db: _orm.Session, login: str):
    return db.query(_models.User).filter(_models.User.login == login).first()