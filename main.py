from fastapi import FastAPI , status
from pydantic import BaseModel 
from database import SessionLocal
from typing import List
import models


app = FastAPI()
db = SessionLocal()



class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class Person(OurBaseModel):
    id:int
    firstname:str
    lastname:str
    isMale:bool

@app.get('/' ,  response_model=List[Person] , status_code=status.HTTP_200_OK)
def getAll_Persons():
    getAllPersons = db.query(models.Person).all()
    return getAllPersons

@app.post('/addperson' ,  response_model=Person , status_code=status.HTTP_201_CREATED)
def add_Person(person:Person):
    newPerson = models.Person(
        id = person.id,
        firstname = person.firstname,
        lastname = person.lastname,
        isMale = person.isMale
    )

    db.add(newPerson)
    db.commit()

    return person

@app.put('/update_person/{id}' , response_model=Person , status_code=status.HTTP_201_CREATED)
def updateperson(id : int , person:Person) :
    find_person = db.query(models.Person).filter(models.Person.id == id).first()

    find_person.firstname = person.firstname
    find_person.lastname = person.lastname
    find_person.isMale = person.isMale
    
    db.commit()     
    return find_person

