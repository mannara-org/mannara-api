from .hardcoded import SPECIALTIES, STUDENTS

import json
import random
import faker

fake = faker.Faker("fr_DZ")


def gen_matricule():
    return str(random.randint(100_000_000_000, 999_999_999_999))


def gen_phoneNumber():
    return (
        "0"
        + random.choice(["5", "6", "7"])
        + str(random.randint(10_000_000, 99_999_999))
    )


academicLevels = {}

for accronyme in STUDENTS.keys():

    academicLevels[accronyme] = []

    for level, data in enumerate(STUDENTS[accronyme]["academicLevels"]):
        sections = []
        academicLevels[accronyme].append(
            {
                "number": level,
                "sections": sections,
            }
        )

        for section_nb in range(1, data["nb_sections"] + 1):
            groups = []
            sections.append(
                {
                    "number": section_nb,
                    "groups": groups,
                }
            )
            for group_nb in range(1, data["nb_groups_per_section"] + 1):
                students = []
                (name, surname) = fake.name().split(" ")
                groups.append(
                    {
                        "number": group_nb,
                        "teachingAssistant": {
                            "name": name,
                            "surname": surname,
                            "email": f"{name}.{surname}@gmail.com",
                            "phoneNumber": gen_phoneNumber(),
                        },
                        "students": students,
                    }
                )
                for _ in range(0, data["nb_students_per_group"]):
                    (name, surname) = fake.name().split(" ")
                    students.append(
                        {
                            "name": name,
                            "surname": surname,
                            "matricule": gen_matricule(),
                            "email": f"{name}.{surname}@gmail.com",
                        }
                    )


with open("collections/specialties.json", "w") as f:
    json.dump(SPECIALTIES, f, indent=2)


with open("collections/academicLevels.json", "w") as f:
    json.dump(academicLevels, f, indent=2)
