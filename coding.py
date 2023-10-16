from colleges import college_db
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


def school_by_major(m: List[str]) -> List[str]:
    result = []

    for c in college_db:
        major = get_majors(c)
        for a in major:
            if a == m[0]:
                result.append(get_school(c))

    return result

def schools_greater(m: List[str]) -> List[str]:
    result = []

    for c in college_db:
        if get_students(c) >= int(m[0]):
            result.append(get_school(c))

    return result

def schools_less(m: List[str]) -> List[str]:
    result = []

    for c in college_db:
        if get_students(c) < int(m[0]):
            result.append(get_school(c))

    return result

def school_by_location(m: List[str]) -> List[str]:
    result = []

    for c in college_db:
        if get_location(c) == m[0]:
            result.append(get_school(c))

    return result

def school_by_sport(m: List[str]) -> List[str]:
    result = []
    
    for c in college_db:
        sport = get_sports(c)
        for s in sport:
            if s == m[0]:
                result.append(get_school(c))

    return result
