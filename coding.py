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



