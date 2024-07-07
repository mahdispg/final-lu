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
    return crud.create_student(db=db, student=student)


@app.get("/Getstudent/{student_id}", response_model=schemas.Student)
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
    return db_student


    
@app.delete("/Delstudent/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    crud.removestudent(db , Student_id=student_id)
    return db_student





#professor

@app.post("/Createprofessor/", response_model=schemas.Professor)
def create_professor(professor: schemas.Professor, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, Professor_id=professor.lid)
    print(db_professor)
    if db_professor:
        raise HTTPException(status_code=400, detail="Professor already registered")
    return crud.create_professoe(db=db, professor=professor)


@app.get("/Getprofessor/{professor_id}", response_model=schemas.Professor)
def read_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, Professor_id=professor_id)
    if db_professor is None:
        raise HTTPException(status_code=404, detail="professor not found")
    return db_professor



@app.put("/prefessor/{prefessor_id}", response_model=schemas.Professor)
def update_prefessor(prefessor_id: str, prefessor: schemas.Professor, db: Session = Depends(get_db)):
    db_prefessor = crud.update_prefessor(db, prefessor_id, prefessor)
    if db_prefessor is None:
        raise HTTPException(status_code=404, detail="prefessor not found")
    return db_prefessor



@app.get("/Delprofessor/{professor_id}", response_model=schemas.Professor)
def del_professor(professor_id: int, db: Session = Depends(get_db)):
    db_professor = crud.get_professor(db, Professor_id=professor_id)
    if db_professor is None:
        raise HTTPException(status_code=404, detail="professor not found")
    crud.removeprefessor(db , Professor_id=professor_id)
    return db_professor
    



#course

@app.post("/Createcourse/", response_model=schemas.Course)
def create_course(course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, Course_id=course.cid)
    print(db_course)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already registered")
    return crud.create_cource(db=db, course=course)


@app.get("/Getcourse/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, Course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course




@app.put("/course/{course_id}", response_model=schemas.Course)
def update_course(course_id: str, course: schemas.Course, db: Session = Depends(get_db)):
    db_course = crud.update_course(db, course_id, course)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course



@app.get("/Delcourse/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, Course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    crud.removecourse(db, Course_id=course_id)
    return db_course

