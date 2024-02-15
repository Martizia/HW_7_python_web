from faker import Faker
import random
from datetime import datetime
from models import Base, Student, Teacher, Group, Subject, grade
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://martizia:qwertY789@localhost/hw7")
Session = sessionmaker(bind=engine)
session = Session()

# Ініціалізація Faker
fake = Faker('uk-UA')

if __name__ == '__main__':
    # Заповнення груп
    groups = [Group(name=fake.word()) for _ in range(3)]
    session.add_all(groups)
    session.commit()

    # Заповнення студентів
    students = [Student(name=fake.name(), group_id=random.choice(groups).id) for _ in range(50)]
    session.add_all(students)
    session.commit()

    # Заповнення викладачів
    teachers = [Teacher(name=fake.name()) for _ in range(5)]
    session.add_all(teachers)
    session.commit()

    # Заповнення предметів
    subjects = [Subject(name=fake.word(), teacher_id=random.choice(teachers).id) for _ in range(7)]
    session.add_all(subjects)
    session.commit()

    # Створення 20 оцінок для кожного студента по 5 оцінок з 4 предметів
    for student in students:
        subject_ids = random.sample(subjects, 4)
        for subject in subject_ids:
            num_grades = random.randint(3, 10)
            grades_data = [{'student_id': student.id,
                            'subject_id': subject.id,
                            'value': random.randint(1, 100),
                            'date': fake.date_between(start_date='-1y', end_date='today')}
                           for _ in range(num_grades)]
            session.execute(grade.insert(), grades_data)
        session.commit()
    session.close()