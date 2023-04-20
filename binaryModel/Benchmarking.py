# This is a sample Python script.
# import minizinc
import time
from minizinc import Instance, Model, Solver
import numpy as np

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    model = Model("../MiniZinc/binarymodel.mzn")
    chuffed = Solver.lookup("chuffed")

    problemInstances = [[8, 4, 5]
                        # ,[8, 4, 6], [8, 4, 7]  # 10 weeks
                         ,[5, 3, 4]
                        #, [5, 3, 5], [5, 3, 6],  # 7 weeks
                        ,[7, 5, 3]
                        # , [7, 5, 4], [7, 5, 5],  # 6 weeks
                         ,[10, 5, 4]
                        #, [10, 5, 5], [10, 5, 6],  # 9 weeks
                         ,[9, 6, 3]
                        #, [9, 6, 4], [9, 6, 5],  # 6 weeks
                        # [12, 4, 6], [12, 4, 7], [12, 4, 8],  # 11 weeks
                         ,[6, 2, 11]  # 11 weeks
                        ]
    for instanceOfGolfer in problemInstances:
        print('===========----------===========----------===========----------===========----------===========')
        print('instance: ', instanceOfGolfer)
        instance = Instance(chuffed, model)
        instance["groups"] = instanceOfGolfer[0]
        instance["groupSize"] = instanceOfGolfer[1]
        instance["weeks"] = instanceOfGolfer[2]
        start = time.time()
        result = instance.solve()
        end = time.time() - start
        print('Time taken: ', end)

        print('Solution: ', result['assignments'])
        assignments = np.array(result['assignments']).reshape((instanceOfGolfer[2], instanceOfGolfer[0], (instanceOfGolfer[0] * instanceOfGolfer[1])))

        # Loop over the weeks and print the groups/players for each week
        for i in range(instanceOfGolfer[2]):
            print("Week ", i)
            for j in range(instanceOfGolfer[1]):
                group_players = np.where(assignments[i, j, :] == 1)[0]
                print("Group ", j, ": Players ", group_players)

