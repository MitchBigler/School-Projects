import random
import pytest
import math
from main import *
from course import Course
from slist import SList



def test_course_creation():
    # make sure that an empty course is correct
    c = Course()
    assert c.name() == ""
    assert c.number() == 0
    assert c.credit_hr() == 0.0
    assert c.grade() == 0.0


def test_course_creation_with_parameters():
    c = Course(1234, "Test Name", 3.0, 3.72)
    assert c.number() == 1234
    assert c.name() == "Test Name"
    assert c.credit_hr() == 3.0
    assert c.grade() == 3.72


    with pytest.raises(ValueError):
        Course("cat")
    with pytest.raises(ValueError):
        Course(1234, None)
    with pytest.raises(ValueError):
        Course(1234, "Test Name", "cat")
    with pytest.raises(ValueError):
        Course(1234, "Test Name", 3.0, "cat")
    with pytest.raises(ValueError):
        Course(-1)
    with pytest.raises(ValueError):
        Course(1234, "Test Name", -2.1)
    with pytest.raises(ValueError):
        Course(1234, "Test Name", 0.0, -2.0)


def test_empty_courselist():
    cl = SList()
    assert cl._head == None
    assert len(cl) == 0
    assert calculate_gpa(cl) == 0.0
    assert is_sorted(cl)

def test_insert():
    random.seed(0)
    cl = SList()
    for _ in range(37):
        cl.insert(Course(random.randrange(1000, 7000), "test", 1.0, 2.0))

    assert len(cl) == 37
    assert is_sorted(cl)

def test_remove():
    random.seed(0)
    cl = SList()
    courseNumbers = []
    for _ in range(37):
        courseNumbers.append(random.randrange(1000, 7000))
    for number in courseNumbers:
        cl.insert(Course(number, "test", 1.0, 2.0))

    course = cl.find(courseNumbers[0])
    assert course.number() == courseNumbers[0]
    course = cl.find(courseNumbers[10])
    assert course.number() == courseNumbers[10]
    course = cl.find(courseNumbers[36])
    assert course.number() == courseNumbers[36]

    for i in range(0, 30, 3):
        cl.remove(courseNumbers[i])

    assert len(cl) == 27
    assert is_sorted(cl)

def test_remove_all():
    cl = SList()
    cl.insert(Course(1000))
    for _ in range(20):
        cl.insert(Course(1200))
    cl.insert(Course(1800))
    assert len(cl) == 22
    cl.remove_all(1200)
    assert len(cl) == 2


def test_gpa():
    random.seed(0)
    cl = SList()
    total_credits = 0.0
    total_grade_points = 0.0
    for _ in range(10):
        credits = random.uniform(1.0, 5.0)
        grade = random.uniform(0.0, 4.0)
        total_credits += credits
        total_grade_points += credits * grade
        cl.insert(Course(1234, "Test", credits, grade))

    assert math.isclose(calculate_gpa(cl), total_grade_points / total_credits)

def test_iterate_list():
    cl = SList()
    cl.insert(Course(1000))
    for _ in range(20):
        cl.insert(Course(1200))
    totalCourses = 0
    for _ in cl:
        totalCourses += 1
    assert totalCourses == 21



    