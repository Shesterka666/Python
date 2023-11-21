from sqlalchemy import Table, Column, Integer, ForeignKey,String,create_engine
from sqlalchemy.orm import relationship,declarative_base,sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)

association_table = Table('student_course_association', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))
    
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
s1 = Student(
    id = 1,
    name = 'Kol',
)
c1 = Course(
    id = 1,
    name = 'ML',
    student_id =1
)
# session.add(s1)
# session.add(c1)
session.add_all([s1, c1])
session.commit()
print(session.query(Student).all())
print(session.query(Course).filter(Course.student_id == 1).all())
session.query(Student).filter(
    Student.name.ilike("Kol")
).update({"Kek": 60}, synchronize_session='fetch')
session.commit()
i = session.query(Student).filter(Student.name == 'Kek').one()
session.delete(i)
session.commit()