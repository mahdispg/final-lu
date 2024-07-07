from sqlalchemy.orm import Session
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from project import models , schemas


#student tabale

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.stid == student_id).first()

def create_student(db: Session, student: schemas.Student):
    db_student = models.Student(
        stid=student.stid ,
        fname=student.fname,
        lname=student.lname,
        father=student.father,
        birth=student.birth,
        ids=student.ids,
        borncity=student.borncity,
        address=student.address,
        postalcode=student.postalcode,
        cphone=student.cphone,
        hphone=student.hphone,
        department=student.department,
        major=student.major,
        married=student.married,
        id=student.id,
        scourseids=student.scourseids,
        lids=student.lids,
    )            
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
    
def removestudent(db: Session , Student_id: int):
    db_student = db.query(models.Student).filter(models.Student.stid == Student_id).first()
    db.delete(db_student)
    db.commit()



def update_student(db: Session, student_id: str, student: models.Student):
    db_student = db.query(models.Student).filter(models.Student.stid == student_id).first()
    if db_student is None:
        return db_student
    else:
        for key, value in student.dict().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
        return db_student


#ostad tabale

def get_ostad(db: Session, ostad_id: int):
    return db.query(models.ostad).filter(models.ostad.lid == ostad_id).first()

def create_professoe(db: Session, ostad: schemas.ostad):
    db_ostad = models.ostad(
        lid=ostad.lid ,
        fname=ostad.fname,
        lname=ostad.lname,
        id=ostad.id,
        department=ostad.department,
        major=ostad.major,
        birth=ostad.birth,
        borncity=ostad.borncity,
        address=ostad.address,
        postalcode=ostad.postalcode,
        cphone=ostad.cphone,
        hphone=ostad.hphone,
        lcourseids=ostad.lcourseids,
    )            
    db.add(db_ostad)
    db.commit()
    db.refresh(db_ostad)
    return db_ostad


def update_ostad(db: Session, ostad_id: str, ostad: models.ostad):
    db_ostad = db.query(models.ostad).filter(models.ostad.lid == ostad_id).first()
    if db_ostad is None:
        return db_ostad
    else:
        for key, value in ostad.dict().items():
            setattr(db_ostad, key, value)
        db.commit()
        db.refresh(db_ostad)
        return db_ostad


def removeostad(db: Session , ostad_id: int):
    db_ostad = db.query(models.ostad).filter(models.ostad.lid == ostad_id).first()
    db.delete(db_ostad)
    db.commit()


#course tabale

def get_course(db: Session, Course_id: int):
    return db.query(models.Course).filter(models.Course.cid == Course_id).first()

def create_cource(db: Session, course: schemas.Course):
    db_course = models.Course(
        cid=course.cid,
        cname=course.cname,
        department=course.department,
        credit=course.credit,
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course



def update_course(db: Session, courseid: str, course: models.Course):
    db_course = db.query(models.Course).filter(models.Course.cid == courseid).first()
    if db_course is None:
        return db_course
    else:
        for key, value in course.dict().items():
            setattr(db_course, key, value)
        db.commit()
        db.refresh(db_course)
        return db_course



def removecourse(db: Session , Course_id: int):
    db_course = db.query(models.Course).filter(models.Course.cid == Course_id).first()
    db.delete(db_course)
    db.commit()