from colleges import colleges_db
from match import match
from typing import List, Tuple, Callable, Any

def get_school(c: List[Tuple[str, List[str], int, str, List[str]]]) -> str:
    return c[0]

def get_majors(c: List[Tuple[str, List[str], int, str, List[str]]]) -> List[str]:
    return c[1]

def get_students(c: List[Tuple[str, List[str], int, str, List[str]]]) -> int:
    return c[2]

def get_location(c: List[Tuple[str, List[str], int, str, List[str]]]) -> str:
    return c[3]

def get_sports(c: List[Tuple[str, List[str], int, str, List[str]]]) -> List[str]:
    return c[4]


def college_by_location(matches: List[str]) -> List[str]:
    """Finds all colleges located in the same place"""

    result = []
    for c in colleges_db:
        if str(matches[0]) == get_location(c):
            result.append(get_school(c))
    #return result
    print(result)
        #print(get_year(movie))
        #print(matches[0])
def students_by_college(matches: List[str]) -> List[str]:

    result = []
    for c in colleges_db:
        if int(matches[0]) == get_school(c):
            result.append(get_students(c))
    #return result
    print(result)
        #print(get_year(movie))
        #print(matches[0])



if __name__ == "__main__":
    assert isinstance(college_by_location(["chicago, illinois"]), list), "college_by_location not returning a list"
    assert isinstance(students_by_college(["20917"]), list), "students_by_college not returning a list"