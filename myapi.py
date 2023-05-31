from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name": "Jon",
        "age": 41,
        "class": "Year 3"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {"name": "Eltro Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The Id of Student", gt=0, lt=6)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student_by_name(*,student_id: int , name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return {"Data":"Data Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Err": "Student already exists."}
    
    students[student_id] = student
    return students[student_id]


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student Doesnt exists."}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year        

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student Doesn't exists."}

    del students[student_id]
    return {"Message": "Student Deleted.."}











