import numpy as np
import pandas as pd


# Next steps:
# Less for loops?
# maybe calculate base pay and what a paycheck would be as a last step


def output_data(data, columns):
    employee_tips = pd.DataFrame(data, columns=columns)
    employee_tips.to_csv("employee-tips-earned.csv")


# Shout out to Ned Batchelder on stack overflow for this consise code for getting chunks of a list


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def tips_earned():
    data = pd.read_csv(
        r"C:\Users\jacob\Downloads\tips-earned - Sheet1.csv")

    total_hours = np.repeat([0], len(data.Date))
    workers = []
    earned_tips = []

    for worker in data.columns[2:]:
        hours = data[worker]
        workers.append(worker)
        for idx, hour in enumerate(hours):
            daily_hours = hour + total_hours[idx]
            total_hours[idx] = daily_hours

    tips = data.Tips
    for index, tip in enumerate(tips):
        for employee in data.columns[2:]:
            hour = data[employee][index]
            percent_worked = (hour / total_hours[index])
            worker_tips = round(tip * percent_worked, 2)
            earned_tips.append(worker_tips)

    output = list(chunks(earned_tips, len(data.columns) - 2))

    output_data(output, workers)
    print("We are printing a csv file to show how much tips your employees earned per hour. Please open using excel or google spreadsheets")


tips_earned()
