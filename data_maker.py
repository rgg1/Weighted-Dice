import csv
import random
import time

num_rolls = 0
total_normal = 0
total_weighted = 0

fieldnames = ["num_rolls", "total_normal", "total_weighted"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "num_rolls": num_rolls,
            "total_normal": total_normal,
            "total_weighted": total_weighted
        }
        csv_writer.writerow(info)
        print(num_rolls, total_normal, total_weighted)

        num_rolls += 1
        total_normal += random.randint(1, 6)
        total_weighted += random.choice([1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6])
        # weighted die where chance of rolling a 4 is 50% higher than rolling any other number

    time.sleep(1)
