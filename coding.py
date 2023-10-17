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


def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("colleges located in %"), school_by_location),
    (str.split("colleges with % major"), school_by_major),
    (str.split("what colleges have a sports team for %"), school_by_sport),
    (str.split("colleges with less than _ students"), schools_less),
    (str.split("colleges with more than or equal to _ students"), schools_greater),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            answer = act(mat)
            return answer if answer else ["No answers"]

    return ["I don't understand"]


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")




query_loop()