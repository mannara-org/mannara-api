
from pydantic import BaseModel


class Student(BaseModel):
    surname: str
    name: str
    matricule: str
    email: str


class TeachingAssistant(BaseModel):
  surname: str | None
  name: str | None
  email: str | None
  phoneNumber: str


class Group(BaseModel):
    number: int
    teachingAssistant: TeachingAssistant

    students: list[Student]


class Section(BaseModel):
    identifier: str

    groups: list[Group]


class AcademicLevel(BaseModel):
    level: int

    sections: list[Section]


class Specialty(BaseModel):
    name: str | None
    acronyme: str | None
    cycle: str | None


class Course(BaseModel):
    name: str
    coef: int
    hasTP: bool
    hasTD: bool


class Semester(BaseModel):
    number: int

    courses: list[Course]


Model = ( Student
         | Group
         | TeachingAssistant
         | Section
         | AcademicLevel
         | Specialty
         | Course
         | Semester )
