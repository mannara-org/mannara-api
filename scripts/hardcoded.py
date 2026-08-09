SPECIALTIES = [
    {
        "name": "SCIENCES ET TECHNOLOGIES",
        "acronyme": "ST",
        "cycle": "Licence",
    },
    {
        "name": "Intelligence Artificiel Applique",
        "acronyme": "I2A",
        "cycle": "Master",
    },
]

STUDENTS = {
    "ST": {
        "academicLevels": [
            {
                "nb_sections": 3,
                "nb_groups_per_section": 5,
                "nb_students_per_group": 25,
            },
            {
                "nb_sections": 2,
                "nb_groups_per_section": 5,
                "nb_students_per_group": 25,
            },
        ]
    },
    "I2A": {
        "academicLevels": [
            {
                "nb_sections": 1,
                "nb_groups_per_section": 5,
                "nb_students_per_group": 25,
            },
            {
                "nb_sections": 1,
                "nb_groups_per_section": 4,
                "nb_students_per_group": 25,
            },
        ]
    },
}

# specialty_acronyme -> array of semester objects
SEMESTERS = {
    "ST": [
        {
            "number": 1,
            "courses": [
                "Algorithmique - Informatique",
                "Bureautique",
                "Chimie I",
                "Physique I",
                "Mathematique I",
                "Methodologie de la redaction I",
                "Techniques de Communication et d'Expression I",
                "Metier en Science et Technologie I",
            ],
        },
        {
            "number": 2,
            "courses": [
                "Bureautique",
                "Chimie II",
                "Physique II",
                "Mathematique II",
                "Methodologie de la redaction II",
                "Techniques de Communication et d'Expression II",
                "Metier en Science et Technologie II",
            ],
        },
    ],
    "I2A": [
        {
            "number": 1,
            "courses": [],
        },
        {
            "number": 2,
            "courses": [
                {"name": "Deep Learning", "coef": 3, "hasTP": True, "hasTD": False},
                {
                    "name": "Méthod de conception avancées",
                    "coef": 2,
                    "hasTP": False,
                    "hasTD": True,
                },
                {
                    "name": "Optimization et métaheuristiques",
                    "coef": 3,
                    "hasTP": True,
                    "hasTD": False,
                },
                {
                    "name": "Processus stochastiques",
                    "coef": 2,
                    "hasTP": False,
                    "hasTD": True,
                },
                {
                    "name": "Algorithmique avancée et complexité",
                    "coef": 2,
                    "hasTP": True,
                    "hasTD": False,
                },
                {
                    "name": "Calcul haute performance",
                    "coef": 2,
                    "hasTP": True,
                    "hasTD": False,
                },
                {
                    "name": "WEB avancé et micro-services",
                    "coef": 2,
                    "hasTP": True,
                    "hasTD": False,
                },
                {
                    "name": "Séminaire et Workshops",
                    "coef": 1,
                    "hasTP": False,
                    "hasTD": False,
                },
            ],
        },
    ],
}
