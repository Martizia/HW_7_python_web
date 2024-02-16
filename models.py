from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


# таблиця для зв'язку many-to-many між таблицями notes та tags
Grade = Table(
    "grades",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("student_id", Integer, ForeignKey("students.id", ondelete="CASCADE")),
    Column("subject_id", Integer, ForeignKey("subjects.id", ondelete="CASCADE")),
    Column('value', Integer),
    Column('date', DateTime),
)


# Таблиця groups з переліком груп студентів
class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


# Таблиця students, де зберігатимуться імена студентів та їх групи
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey(Group.id))
    groups = relationship('Group', backref='student')
    subject = relationship('Subject', secondary=Grade, backref='subjects')


# Таблиця teachers з переліком вчителів
class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


# Таблиця subjects з переліком предметів
class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    teacher_id = Column(Integer, ForeignKey(Teacher.id))
    teachers = relationship('Teacher', backref='subject')
