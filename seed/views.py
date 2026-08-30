from django.http import JsonResponse, HttpResponse

import json


def specialties(_):
    with open("collections/specialties.json", "r") as f:
        return JsonResponse(json.loads(f.read()), safe=False)


def academicLevels(_):
    with open("collections/academicLevels.json", "r") as f:
        return JsonResponse(json.loads(f.read()), safe=False)


def semesters(_):
    with open("collections/semesters.json", "r") as f:
        return JsonResponse(json.loads(f.read()), safe=False)
