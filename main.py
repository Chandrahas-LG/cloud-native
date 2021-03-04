from fastapi import FastAPI
from pydantic import BaseModel 
from fastapi.encoders import jsonable_encoder

app=FastAPI()
class Name(BaseModel):
    student_name:str
    student_id:str
    sec:str

@app.get("/")
def basic():
    return "student details"

@app.get("/student")
def det(name_var:Name):
    return a

a=[]

@app.post("/details")
def name(name_var:Name):
    item=dict()
    name_encoded = jsonable_encoder(name_var)
    fname = name_encoded['student_name']
    pname = name_encoded['student_id']
    sec = name_encoded['sec']
    item.update({"student_name":fname,
    "student_id":pname,
    "student_sec":sec})
    a.append(item)
    return "registered"

@app.put("/details/{student_id}")
async def update_item(student_id:str,name_var:Name):
    update_item_encoded = jsonable_encoder(name_var)
    for p in a:
        if p['student_id']==student_id:
            p['student_sec'] = "B"
    return a

@app.delete("details/{student_id}")
def del_item(student_id:str,name_var:Name):
    for p in a:
        if p['student_id'] == student_id:
            del p
    return a                 