from typing import List, Tuple

college_db: List[Tuple[str, List[str], int, str, List[str]]] = [
    (
        "depaul university", #school
        [
            "biology",
            "biochemistry",
            "acconting",
            "finance",
        ], # majors
        20917, # students
        "chicago, illinois", # location
        [
            "basketball",
            "cross country",
            "soccer",
            "tennis",
            "track & field",
        ], # sports

    ),
    (
        "loyola university chicago", 
        [
            "business",
            "marketing",
            "social science",
            "psychology",
        ],
        11703,
        "chicago, illinois", 
        [
            "basketball",
            "cross country",
            "soccer",
            "tennis",
            "track & field",
            "volleyball",
        ], 

    ),
    (
        "illinois institute of technology", 
        [
            "engineering",
            "computer and information sciences and support services",
            "architecture and related services",
        ],
        6947,
        "chicago, illinois", 
        [
            "basketball",
            "cross country",
            "lacrosse",
            "swimming & diving",
            "volleyball",
        ], 

    ),
    (
        "yale university", 
        [
            "mathematics and statistics",
            "multi/interdisciplinary studies",
            "history",
            "engineering",
        ],
        14776,
        "new haven, connecticut", 
        [
            "ice hockey",
            "golf",
            "squash",
            "basketball",
        ], 

    ),
]