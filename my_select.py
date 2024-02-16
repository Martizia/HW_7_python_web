from sqlalchemy import func, desc, select
from models import Student, Teacher, Subject, Group, Grade
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:qwertY789@localhost/hw7')
Session = sessionmaker(bind=engine)
session = Session()


def select_1():
    result = session.query(Student.name, func.round(func.avg(Grade.c.value), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2():
    result = session.query(Student.name, func.round(func.avg(Grade.c.value), 2).label('avg_grade'))\
        .select_from(Student).join(Grade).where(Grade.c.subject_id == 3).group_by(Student.name)\
        .order_by(desc('avg_grade')).limit(1).all()
    return result


def select_3():
    result = session.query(Group.name, func.round(func.avg(Grade.c.value), 2).label('avg_grade'))\
        .select_from(Group).join(Student).join(Grade).where(Grade.c.subject_id == 1)\
        .group_by(Group.name).order_by(desc('avg_grade')).all()
    return result


def select_4():
    result = session.query(func.round(func.avg(Grade.c.value), 2).label('avg_grade'))\
        .select_from(Grade).all()
    return result


def select_5():
    result = session.query(Teacher.name, Subject.name).select_from(Subject).join(Teacher)\
        .where(Teacher.id == 2).all()
    return result


def select_6():
    result = session.query(Group.name, Student.name).select_from(Student).join(Group).where(Group.id == 3).all()
    return result


def select_7():
    result = session.query(Group.name, Subject.name, Student.name, Grade.c.value).select_from(Student)\
        .join(Grade).join(Subject).join(Group).where(Group.id == 1).where(Subject.id == 5).all()
    return result


def select_8():
    result = session.query(Teacher.name, func.round(func.avg(Grade.c.value), 2).label('avg_grade'))\
        .select_from(Teacher).join(Subject).join(Grade).where(Teacher.id == 2).group_by(Teacher.name).all()
    return result


def select_9():
    result = session.query(Student.name, Subject.name).select_from(Subject).distinct()\
        .join(Grade).join(Student).where(Student.id == 35).all()
    return result


def select_10():
    result = session.query(Student.name, Teacher.name, Subject.name).select_from(Subject)\
        .distinct().join(Grade).join(Student).join(Teacher).where(Student.id == 14)\
        .where(Teacher.id == 3).all()
    return result


if __name__ == '__main__':
    print(select_1())
    print(select_2())
    print(select_3())
    print(select_4())
    print(select_5())
    print(select_6())
    print(select_7())
    print(select_8())
    print(select_9())
    print(select_10())