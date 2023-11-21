from sqlalchemy import Column, Index, Integer, MetaData, select, String, ForeignKey,Table, create_engine
from sqlalchemy.orm import declarative_base, relationship,Session

Base = declarative_base()
engine = create_engine("sqlite:///:memory:",echo=True)
metadata_obj = MetaData()

#association_table = Table('student_course_association', Base.metadata,
    #Column('courses_id', Integer, ForeignKey('students.id')),
    #Column('student_id', Integer, ForeignKey('courses.id')))

class StudentsCourses(Base):
    __tablename__ = "studbook"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    courses_id = Column(Integer)
    __table_args__ = (Index("student_id","courses_id", unique=True),)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)

   
with Session(engine) as session:
    with session.begin():
        Base.metadata.create_all(engine)
        stu = Student(id = 1, name = "Kek")
        session.add(stu)
    with session.begin():
        res = session.execute(select(Student).where(Student.id == 1 ))
        print(res.scalar())