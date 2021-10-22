import numpy as np
import csv


class Worker:
    def __init__(self, name, hours_worked):
        self.name = name
        self.hours_worked = hours_worked


jacob = Worker("Jacob", [5, 5, 5, 5, 5, 4.5, 5])
tessa = Worker("Tessa", [8, 8, 8, 8, 8, 1, 1])
derick = Worker("Derick", [0, 0, 1, 2.5, .25, 8, 8])
morgan = Worker("Morgan", [0, 0, 4, 5.5, 2, 6, 9])

tips = [1000, 500, 345.66, 333.10, 345.99, 999.10, 810.75]

# Next steps:
# Less for loops?
# create a pdf or csv with the data outputted
# Start being able to read csv and change the function to adapt to that
# maybe calculate base pay and what a paycheck would be as a last step


def output_data(fields, rows):
    filename = "employee_tips_earned.csv"

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

# Shout out to Ned Batchelder on stack overflow for this consise code


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def tips_earned(workers, tips):
    total_hours = np.repeat([0], len(tips))
    names = []
    earned_tips = []

    for worker in workers:
        hours = worker.hours_worked
        name = worker.name
        names.append(name)
        for idx, hour in enumerate(hours):
            daily_hours = hour + total_hours[idx]
            total_hours[idx] = daily_hours

    for index, tip in enumerate(tips):
        for worker in workers:
            percent_worked = (worker.hours_worked[index] / total_hours[index])
            worker_tips = round(tip * percent_worked, 2)
            earned_tips.append(worker_tips)

    rows = list(chunks(earned_tips, len(workers)))

    print("We are printing a csv file to show how much tips your employees earned per hour. Please open using excel or google spreadsheets")

    output_data(names, rows)


tips_earned([jacob, tessa, derick, morgan], tips)
