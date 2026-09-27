
from scripts.hardcoded import SPECIALTIES, STUDENTS_DISTRIBUTION, SEMESTERS
from scripts.generators import gen_students

import json


with open("collections/specialties.json", "w") as f:
    json.dump(
        {
            "meta": {"collectionName": "specialties", "aggregated": False, "aggregatedBy": None},
            "data": SPECIALTIES,
        },
        f,
        indent=2,
    )


with open("collections/academicLevels.json", "w") as f:
    json.dump(
        {
            "meta": {
                "collectionName": "academicLevels",
                "aggregated": True,
                "aggregatedBy": {"model": "Specialty", "field": "acronyme"},
            },
            "data": gen_students(STUDENTS_DISTRIBUTION),
        },
        f,
        indent=2,
    )

with open("collections/semesters.json", "w") as f:
    json.dump(
        {
            "meta": {
                "collectionName": "semesters",
                "aggregated": True,
                "aggregatedBy": {"model": "Specialty", "field": "acronyme"},
            },
            "data": SEMESTERS,
        },
        f,
        indent=2,
    )
