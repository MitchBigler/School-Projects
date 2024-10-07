''' Course Class for Project 4 of CS 2420 '''

class Course:
    ''' Course object '''
    def __init__(self, number=0, name="", credit_hour=0.0, grade=0.0):
        if not isinstance(number, int):
            raise ValueError
        if not isinstance(name, str):
            raise ValueError
        if not isinstance(credit_hour, float):
            raise ValueError
        if not isinstance(grade, float):
            raise ValueError
        
        self._number = number
        self._name = name
        self._credit_hour = credit_hour
        self._grade = grade
          
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._number == other._number
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self._number < other._number
        return NotImplemented

    def __gt__(self, other):
        return not self.__le__(other)

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self._number <= other._number
        return NotImplemented

    def __ge__(self, other):
        return not self.__lt__(other)

    def __str__(self):
        return f'cs{self._number} {self._name} Grade: {self._grade} Credit Hours: {self._credit_hour}'

    def number(self):
        return self._number
    
    def name(self):
        return self._name
       
    def credit_hr(self):
        return self._credit_hour
    
    def grade(self):
        return self._grade