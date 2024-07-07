from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

#se khat paeen baray rafe moshkele unknown parent packaje mibashad
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

###

from project import crud, models,schemas

from project.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#student

@app.post("/Createstudent/", response_model=schemas.Student)
def create_student(student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student.stid)
    print(db_student)
    if db_student:
        raise HTTPException(status_code=400, detail="student already registered")
    schemas.validate_student(student)
    error_akhs_dars = {}
    scourseids = student.scourseids.split(",")
    for code in scourseids:
        db_rel_course_student = crud.get_course(db, Course_id=code)
        if db_rel_course_student is None:
            error_akhs_dars["lcourseids"] = "کد درس انتخاب شده جزو دروس اريه شده نمی باشد"
    lids = student.lids.split(",")
    for code in lids:
        db_rel_PS = crud.get_ostad(db, ostad_id=code)
        if db_rel_PS is None:
            error_akhs_dars["lids"] = "استاد انتخابی شما در سیستم موجود نمی باشد"
    if error_akhs_dars:
        raise HTTPException(detail=error_akhs_dars , status_code=400)
    return crud.create_student(db=db, student=student)


@app.get("/Getstudent/{student_id}", response_model=schemas.Student_response)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    return db_student

@app.put("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: str, student: schemas.Student, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, student_id, student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    schemas.validate_student(student)
    error_akhs_dars = {}
    scourseids = student.scourseids.split(",")
    for code in scourseids:
        db_rel_course_student = crud.get_course(db, Course_id=code)
        if db_rel_course_student is None:
            error_akhs_dars["lcourseids"] = "کد درس انتخاب شده جزو دروس اريه شده نمی باشد"
    lids = student.lids.split(",")
    for code in lids:
        db_rel_PS = crud.get_ostad(db, ostad_id=code)
        if db_rel_PS is None:
            error_akhs_dars["lids"] = "کد استاد انتخاب شده جزو اساتید نمی باشد"
    if error_akhs_dars:
        raise HTTPException(detail=error_akhs_dars , status_code=400)
    return db_student


    
@app.delete("/Delstudent/{student_id}", response_model=schemas.Student)
def del_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    crud.removestudent(db , Student_id=student_id)
    return db_student





#ostad

@app.post("/Createostad/", response_model=schemas.ostad)
def create_ostad(ostad: schemas.ostad, db: Session = Depends(get_db)):
    db_ostad = crud.get_ostad(db, ostad_id=ostad.lid)
    print(db_ostad)
    if db_ostad:
        raise HTTPException(status_code=400, detail="ostad already registered")
    schemas.validate_ostad(ostad)
    lcourseids = ostad.lcourseids.split(",")
    error_akhs_dars = {}
    for code in lcourseids:
        db_rel_course_ostad = crud.get_course(db, Course_id=code)
        if db_rel_course_ostad is None:
            error_akhs_dars["lcourseids"] = "کد درس انتخاب شده جزو دروس اريه شده نمی باشد"
    if error_akhs_dars:
        raise HTTPException(detail=error_akhs_dars , status_code=400)
    return crud.create_professoe(db=db, ostad=ostad)


@app.get("/Getostad/{ostad_id}", response_model=schemas.ostad_response)
def read_ostad(ostad_id: int, db: Session = Depends(get_db)):
    db_ostad = crud.get_ostad(db, ostad_id=ostad_id)
    if db_ostad is None:
        raise HTTPException(status_code=404, detail="ostad not found")
    return db_ostad



@app.put("/ostad/{ostad_id}", response_model=schemas.ostad)
def update_ostad(ostad_id: str, ostad: schemas.ostad, db: Session = Depends(get_db)):
    db_ostad = crud.update_ostad(db, ostad_id, ostad)
    if db_ostad is None:
        raise HTTPException(status_code=404, detail="ostad not found")
    schemas.validate_ostad(ostad)
    error_akhs_dars = {}
    lcourseids = ostad.lcourseids.split(",")
    for code in lcourseids:
        db_rel_course_ostad = crud.get_course(db, Course_id=code)
        if db_rel_course_ostad is None:
            error_akhs_dars["lcourseids"] = "کد درس انتخاب شده جزو دروس اريه شده نمی باشد"
    if error_akhs_dars:
        raise HTTPException(detail=error_akhs_dars , status_code=400)
    return db_ostad



@app.delete("/Delostad/{ostad_id}", response_model=schemas.ostad)
def del_ostad(ostad_id: int, db: Session = Depends(get_db)):
    db_ostad = crud.get_ostad(db, ostad_id=ostad_id)
    if db_ostad is None:
        raise HTTPException(status_code=404, detail="ostad not found")
    crud.removeostad(db , ostad_id=ostad_id)
    return db_ostad
    



#course

@app.post("/Createcourse/", response_model=schemas.Course)
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, Course_id=course.cid)
    print(db_course)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already registered")
    schemas.validate_course(course)
    return crud.create_cource(db=db, course=course)


@app.get("/Getcourse/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, Course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course




@app.put("/course/{courseid}", response_model=schemas.Course)
def update_course(courseid: str, course: schemas.Course, db: Session = Depends(get_db)):
    schemas.validate_course(course)
    db_course = crud.update_course(db, courseid, course)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course



@app.delete("/Delcourse/{course_id}", response_model=schemas.Course)
def del_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, Course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    crud.removecourse(db, Course_id=course_id)
    return db_course

