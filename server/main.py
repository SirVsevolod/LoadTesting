from fastapi import FastAPI, Depends, HTTPException
import server.shema as shm
import server.services as serv
import sqlalchemy.orm as orm
import uvicorn

app = FastAPI()


@app.get("/")
def home():
    return {"key": "helloworld"}


@app.get("/users/{user}", response_model=shm.BaseUser)
def getUser(user: str, db: orm.Session = Depends(serv.get_db)):
    db_user = serv.get_user_by_login(db=db, login=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail='Not Found')
    return db_user



@app.post("/user")
def createUser(users: shm.CreateUser, db: orm.Session = Depends(serv.get_db)):
    db_user = serv.get_user_by_login(db=db, login=users.login)
    if db_user:
        raise HTTPException(status_code=400, detail="you can't use this login")
    return serv.create_user(db=db, user=users)

if __name__ == "__main__":
    uvicorn.run(app)