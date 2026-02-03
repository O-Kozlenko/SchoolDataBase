import csv
from csv import DictWriter
from os import write

with open("config.txt", "r") as file:
    min_score = int(file.read())

with open("students.csv", "r", encoding="utf-8") as file:
    data = list(csv.DictReader(file, delimiter=','))

for student in data:
    student["score"] = int(student["score"])

for i in data:
    if i["score"] < min_score:
        with open("retest.csv", "w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id","name","surname","score"])
            writer.writeheader()
            for student in data:
                writer.writerow(student)