
import random

from typing import Any

import faker

from scripts.hardcoded import DEGREE_PROGRAMS, STUDENTS_DISTRIBUTION


fake = faker.Faker("fr_DZ")


def gen_matricule():
    return str(random.randint(100_000_000_000, 999_999_999_999))


def gen_phoneNumber():
    return (
        "0"
        + random.choice(["5", "6", "7"])
        + str(random.randint(10_000_000, 99_999_999))
    )


def pedagogical_structure():
    degree_programs = []
    for degree_program in DEGREE_PROGRAMS:

        academicLevels = []
        degree_program["academicLevels"] = academicLevels
        degree_programs.append(degree_program)

        for AL_data in STUDENTS_DISTRIBUTION:
            pass

    return degree_programs


print(pedagogical_structure())
