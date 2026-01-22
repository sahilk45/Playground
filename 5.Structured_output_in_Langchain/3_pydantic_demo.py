from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str = 'Sahil'  #can set default values
    age:Optional[int]=None
    email:EmailStr   #Built-in validation
    cgpa:float =Field(gt=0,lt=10,default=5,description="Marks of student")  #can apply contraints,defaults,description,regex

name_student = {'age':'21','email':'abc@gmail.com','cgpa':9}  #create a dict, automatic type conversion 

student = Student(**name_student)

# print(student) #if name is int in dict than will throw error

student_dict=dict(student)
print(student_dict['age'])

studen_json=student.model_dump_json()