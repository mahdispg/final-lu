from typing import Union

from pydantic import BaseModel


#student

class Student(BaseModel):
    stid: str
    fname: str
    lname: str
    father: str
    birth: str
    ids : str
    borncity:str
    address: str
    postalcode: str
    cphone: str
    hphone: str
    department: str
    major : str
    married: str
    id : str
    scourseids : str
    lids : str


#Professor

class Professor(BaseModel):
    lid: str
    fname: str
    lname: str
    id : str
    department: str
    major : str
    birth: str
    borncity:str
    address: str
    postalcode: str
    cphone: str
    hphone: str
    lcourseids : str

#course

class Course(BaseModel):
    cid: str = ""
    cname: str = ""
    department: str = ""
    credit: int

