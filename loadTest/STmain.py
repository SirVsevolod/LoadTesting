from locust import HttpUser, task, between
import random as rnd
from loadTest import DOPFunc


class UserTest(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def CreateUser(self):
        login = rnd.choice(DOPFunc.get_name_list())
        data ={
            "login": login,
            "password": "123123",
            "discription": "aaaaaaaaaaaaaaaaaaaa"
        }
        self.client.post('/user', json=data)



    @task(2)
    def GetUser(self):
        login = rnd.choice(DOPFunc.get_name_list())
        self.client.get(f"/users/{login}", name="/users/{login}")


    @task(3)
    def HelloWorld(self):
        self.client.get("/", name='helloWorld')

