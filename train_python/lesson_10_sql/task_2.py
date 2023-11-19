from sqlalchemy import Column, Integer, MetaData, select, String, ForeignKey,Table, create_engine
from sqlalchemy.orm import declarative_base, relationship,Session

Base = declarative_base()
engine = create_engine("sqlite:///:memory:",echo=True)
metadata_obj = MetaData()

association_table = Table('student_course_association', Base.metadata,
    Column('courses_id', Integer, ForeignKey('students.id')),
    Column('student_id', Integer, ForeignKey('courses.id')))

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses_id = relationship("Course", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship("Student", back_populates="courses")

    with Session(engine) as session:
        with session.begin():
            metadata_obj.create_all(engine)
            stu = Student(id = 1, name = "Kek", courses_id = 1)
            session.add(stu)
        with session.begin():
            res = session.execute(select(Student).where(Student.id == 1 ))
            print(res.scalar())