from slist import SList
from course import Course

def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.grade() * course.credit_hr()
        credits += course.credit_hr()
    if credits == 0:
        return 0
    return sumGrades / credits

def is_sorted(lyst):
    for i in range(0, lyst.size()  - 1):
        if lyst[i] > lyst[i + 1]:
            return False
    return True

def main():
    test_list = SList()
    print(test_list)
    test_list.insert(Course(100, "math", 3.0, 1.0))
    test_list.insert(Course(200, "english", 3.0, 1.0))
    test_list.insert(Course(50, "prog", 3.0, 1.0))
    print(test_list)
    test_list.remove(100)
    print(test_list)
    print(test_list.find(50))
if __name__ == "__main__":
    main()