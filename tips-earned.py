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
        name = worker.name
        hours = worker.hours_worked
        print(name, hours)
        for idx, hour in enumerate(hours):
            print(f"BEFORE {total_hours}")
            daily_hours = hour + total_hours[idx]
            total_hours[idx] = daily_hours
            print(total_hours)

    # worker_a = workers[0].hours_worked
    # worker_b = workers[1].hours_worked
    # worker_c = workers[2].hours_worked
    # worker_d = workers[3].hours_worked
    # ab_hours = np.add(worker_a, worker_b)
    # cd_hours = np.add(worker_c, worker_d)
    # total_hours = np.add(ab_hours, cd_hours)

    # print(total_hours)

    # for index, tip in enumerate(tips):

    #     for idx, worker in enumerate(workers):
    #         print(worker.hours_worked[idx])
    # percent_worked = worker.hours_worked[idx] / total_hours[index]

    # worker_tips = round(tip * percent_worked, 2)

    # print(f"On this day {worker.name} made ${worker_tips} in tips")

    # worker_a_percent_worked = (worker_a[idx] / total_hours[idx])
    # worker_b_percent_worked = (worker_b[idx] / total_hours[idx])
    # worker_c_percent_worked = (worker_c[idx] / total_hours[idx])
    # worker_d_percent_worked = (worker_d[idx] / total_hours[idx])

    # worker_a_tips = round(tip * worker_a_percent_worked, 2)
    # worker_b_tips = round(tip * worker_b_percent_worked, 2)
    # worker_c_tips = round(tip * worker_c_percent_worked, 2)
    # worker_d_tips = round(tip * worker_d_percent_worked, 2)
    # print(
    #     f"Tips Earned: Worker A: {worker_a_tips}, Worker B: {worker_b_tips}, Worker C: {worker_c_tips}, Worker D: {worker_d_tips},")
tips_earned([jacob, tessa, derick, morgan], tips)
