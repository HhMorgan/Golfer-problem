# This is a sample Python script.
# import minizinc
import time
from minizinc import Instance, Model, Solver


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    model = Model("../MiniZinc/golfer.mzn")
    chuffed = Solver.lookup("chuffed")

    problemInstances = [[8, 4, 5], [8, 4, 6], [8, 4, 7],  # 10 weeks
                        [5, 3, 4], [5, 3, 5], [5, 3, 6],  # 7 weeks
                        [7, 5, 3], [7, 5, 4], [7, 5, 5],  # 6 weeks
                        [10, 5, 4], [10, 5, 5], [10, 5, 6],  # 9 weeks
                        [9, 6, 3], [9, 6, 4], [9, 6, 5],  # 6 weeks
                        [12, 4, 6], [12, 4, 7], [12, 4, 8],  # 11 weeks
                        [6, 2, 11]  # 11 weeks
                        ]
    for instanceOfGolfer in problemInstances:
        print('===========----------===========----------===========----------===========----------===========')
        print('instance: ', instanceOfGolfer)
        instance = Instance(chuffed, model)
        instance["groupsNum"] = instanceOfGolfer[0]
        instance["groupSize"] = instanceOfGolfer[1]
        instance["weeksNum"] = instanceOfGolfer[2]
        start = time.time()
        result = instance.solve()
        end = time.time() - start
        print('Time taken: ', end)

        # print('Solution: ', result['assignment'])
        for i in range(instanceOfGolfer[2]):
            print('Week ', i)
            print(result['assignment'][i])
