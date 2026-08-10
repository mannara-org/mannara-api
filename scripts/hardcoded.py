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
                {
                    "name": "Algorithmique - Informatique",
                    "coef": 2,
                    "hasTP": True,
                    "hasTD": False,
                },
                {
                    "name": "Bureautique",
                    "coef": 1,
                    "hasTP": True,
                    "hasTD": False,
                },
                {
                    "name": "Chimie I",
                    "coef": 3,
                    "hasTP": True,
                    "hasTD": True,
                },
                {
                    "name": "Physique I",
                    "coef": 3,
                    "hasTP": True,
                    "hasTD": True,
                },
                {
                    "name": "Mathematique I",
                    "coef": 3,
                    "hasTP": True,
                    "hasTD": True,
                },
                {
                    "name": "Methodologie de la redaction I",
                    "coef": 1,
                    "hasTP": False,
                    "hasTD": False,
                },
                {
                    "name": "Techniques de Communication et d'Expression I",
                    "coef": 1,
                    "hasTP": True,
                    "hasTD": False,
                },
                {
                    "name": "Metier en Science et Technologie I",
                    "coef": 1,
                    "hasTP": False,
                    "hasTD": False,
                },
            ],
        },
        {
            "number": 2,
            "courses": [
                {
                    "name": "Bureautique",
                    "coef": 2,
                    "hasTP": True,
                    "hasTD": False,
                },
                {
                    "name": "Chimie II",
                    "coef": 3,
                    "hasTP": True,
                    "hasTD": True,
                },
                {
                    "name": "Physique II",
                    "coef": 3,
                    "hasTP": True,
                    "hasTD": True,
                },
                {
                    "name": "Mathematique II",
                    "coef": 3,
                    "hasTP": True,
                    "hasTD": True,
                },
                {
                    "name": "Methodologie de la redaction II",
                    "coef": 1,
                    "hasTP": False,
                    "hasTD": False,
                },
                {
                    "name": "Techniques de Communication et d'Expression II",
                    "coef": 1,
                    "hasTP": False,
                    "hasTD": False,
                },
                {
                    "name": "Metier en Science et Technologie II",
                    "coef": 1,
                    "hasTP": False,
                    "hasTD": False,
                },
            ],
        },
    ],
    "I2A": [
        {
            "number": 1,
            "courses": [
                {
                    "name": "Data Science in Python",
                    "coef": 2,
                    "hasTP": True,
                    "hasTD": False,
                },
                {
                    "name": "Traitement et Analyse D'image",
                    "coef": 3,
                    "hasTP": True,
                    "hasTD": False,
                },
                {
                    "name": "Machine Learning",
                    "coef": 3,
                    "hasTP": True,
                    "hasTD": False,
                },
                {
                    "name": "Résaux avancées",
                    "coef": 3,
                    "hasTP": True,
                    "hasTD": False,
                },
                {
                    "name": "Base de Donnée avancées",
                    "coef": 3,
                    "hasTP": True,
                    "hasTD": False,
                },
            ],
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
