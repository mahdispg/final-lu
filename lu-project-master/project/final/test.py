@app.put("/students/{student_id}", response_model=models.Student)
def update_student(student_id: str, student: models.StudentCreate, db: Session = Depends(crud.get_student)):
    db_student = crud.update_student(db, student_id, student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student




def update_student(db: Session, student_id: str, student: models.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.student_id == student_id).first()
    for key, value in student.dict().items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student