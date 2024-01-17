import csv

with open('profiles1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["test"]
    writer.writerow(field)
    writer.writerow("field")