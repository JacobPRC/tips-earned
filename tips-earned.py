import numpy as np
import csv
import pandas as pd


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


def tips_earned():
    data = pd.read_csv(
        r"C:\Users\jacob\Downloads\tips-earned - Sheet1.csv")

    total_hours = np.repeat([0], len(data.Date))
    workers = []
    earned_tips = []

    for item in data.columns[2:]:
        hours = data[item]
        workers.append(item)
        for idx, hour in enumerate(hours):
            daily_hours = hour + total_hours[idx]
            total_hours[idx] = daily_hours

    tips = data.Tips
    for index, tip in enumerate(tips):
        for item in data.columns[2:]:
            hour = data[item][index]
            percent_worked = (hour / total_hours[index])
            worker_tips = round(tip * percent_worked, 2)
            earned_tips.append(worker_tips)

    data = list(chunks(earned_tips, len(data.columns) - 2))
    print(data)

    try:
        output_data(workers, data)
        print("We are printing a csv file to show how much tips your employees earned per hour. Please open using excel or google spreadsheets")
    except:
        print("Looks like you already have a cvs file named employee_tips_earn.csv, please delete it and try again")


tips_earned()


# def tips_earned(workers, tips):
#     total_hours = np.repeat([0], len(tips))
#     names = []
#     earned_tips = []

#     for worker in workers:
#         hours = worker.hours_worked
# #         name = worker.name
# #         names.append(name)
#         for idx, hour in enumerate(hours):
#             print(hour, worker.name)
# #             daily_hours = hour + total_hours[idx]
# #             total_hours[idx] = daily_hours

# #     for index, tip in enumerate(tips):
# #         for worker in workers:
# #             percent_worked = (worker.hours_worked[index] / total_hours[index])
# #             worker_tips = round(tip * percent_worked, 2)
# #             earned_tips.append(worker_tips)

# #     rows = list(chunks(earned_tips, len(workers)))

# #     print("We are printing a csv file to show how much tips your employees earned per hour. Please open using excel or google spreadsheets")

# #     output_data(names, rows)


# tips_earned([jacob, tessa, derick, morgan], tips)

# def output_data(data, columns):
#     employee_tips = pd.DataFrame(data, columns=columns)
#     employee_tips.to_csv("employee-tips-earned.csv")


# # Shout out to Ned Batchelder on stack overflow for this consise code


# def chunks(lst, n):
#     for i in range(0, len(lst), n):
#         yield lst[i:i + n]
