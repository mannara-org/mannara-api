
from sqlmodel import SQLModel

# -------------- PEDAGOGICAL STRUCTURE --------------


class DegreeProgramBase(SQLModel):
    name: str
    acronyme: str
    cycle: str

    academicLevels: list[AcademicLevelBase]


class AcademicLevelBase(SQLModel):
    level: int

    sections: list[SectionBase]


class SectionBase(SQLModel):
    identifier: str

    groups: list[GroupBase]


class GroupBase(SQLModel):
    number: int

    students: list[StudentBase]


class StudentBase(SQLModel):
    surname: str
    name: str
    matricule: str
    email: str


# -------------- PEDAGOGICAL STRUCTURE --------------

class CourseBase(SQLModel):
    name: str


class SemesterBase(SQLModel):
    number: int

    courses: list[SemesterCoursesBase]


class SemesterCoursesBase(SQLModel):

    course: CourseBase

    hasTD: bool
    hasTP: bool

    numTD: bool
    numTP: bool

    coef: int


class ProfessorBase(SQLModel):
    surname: str
    name: str
    email: str
    phoneNumber: str

    teacherCourses: list[CourseTeacherBase]
    assistingCourses: list[CourseAssistantBase]


class CourseTeacherBase(SQLModel):
    course: CourseBase
    section: SectionBase


class CourseAssistantBase(SQLModel):
    course: CourseBase
    group: GroupBase

    role: str


Model = ( StudentBase
         | GroupBase
         | SectionBase
         | AcademicLevelBase
         | DegreeProgramBase
         | CourseBase
         | SemesterBase
         | SemesterCoursesBase
         | ProfessorBase
         | CourseTeacherBase
         | CourseAssistantBase )
