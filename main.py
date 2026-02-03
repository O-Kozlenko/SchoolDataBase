import csv
import json
from csv import DictWriter
from os import write

with open("config.txt", "r") as file:
    min_score = int(file.read())

with open("students.csv", "r", encoding="utf-8") as file:
    students = list(csv.DictReader(file, delimiter=','))

for student in students:
    student["score"] = int(student["score"])

retest_list = []
for student in students:
    if student["score"] < min_score:
        retest_list.append(student)

with open("retest.csv", "w", encoding="utf-8") as file:
    zagolovok = ["id","name","surname","score"]
    writer = csv.DictWriter(file,fieldnames=zagolovok)
    writer.writeheader()
    for student in retest_list:
        writer.writerow(student)

success_list = []

for student in students:
    if student["score"] >= min_score:
        student["passed"] = True
        success_list.append(student)

with open("best_students.json","w", encoding="utf-8") as file:
    json.dump(success_list, file, ensure_ascii=False, indent=2)