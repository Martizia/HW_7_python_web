from sqlalchemy import func, desc
from models import Student, Teacher, Subject, Group, grade
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:qwertY789@localhost/postgres', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def select_1():
    top_students = session.query(Student.name, func.round(func.avg(grade.grade), 2).label('avg_grade'))\
        .select_from(grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()


print(select_1())