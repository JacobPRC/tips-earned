import numpy as np


class Worker:
    def __init__(self, name, hours_worked):
        self.name = name
        self.hours_worked = hours_worked


jacob = Worker("Jacob", [5, 5, 5, 5, 5, 4.5, 5])
tessa = Worker("Tessa", [8, 8, 8, 8, 8, 1, 1])
derick = Worker("Derick", [0, 0, 1, 2.5, .25, 8, 8])
morgan = Worker("Morgan", [0, 0, 4, 5.5, 2, 6, 9])

tips = [1000, 500, 345.66, 333.10, 345.99, 999.10, 810.75]


def tips_earned(workers, tips):

    total_hours = [0, 0, 0, 0, 0, 0, 0]

    for worker in workers:
        hours = worker.hours_worked
        for idx, hour in enumerate(hours):
            daily_hours = hour + total_hours[idx]
            total_hours[idx] = daily_hours

    for index, tip in enumerate(tips):
        for worker in workers:
            percent_worked = (worker.hours_worked[index] / total_hours[index])
            worker_tips = round(tip * percent_worked, 2)
            print(
                f"On day {index + 1} {worker.name} earned ${worker_tips} in tips")


tips_earned([jacob, tessa, derick, morgan], tips)
