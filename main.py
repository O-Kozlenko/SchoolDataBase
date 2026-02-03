import csv
from csv import DictWriter
with open("config.txt", "r") as pepe:
    min_score = int(pepe.read())

with open("students.csv", "r", encoding="utf-8") as file:
    data = list(csv.DictReader(file, delimiter=','))

for student in data:
    student["score"] = int(student["score"])
print(data)
