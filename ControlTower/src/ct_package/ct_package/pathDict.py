# destination coordinates define
robotXY_Dict = {
    "R1" : [-0.1, 2.5, 0],
    "R2" : [-0.1, 1.5, 0],
    "R3" : [-0.1, 0.3, 0]
}

storeXY_Dict = {
    "S11" : [1.7, 2.8, 160],
    "S12" : [1.7, 1.7, 160],
    "S21" : [1.7, 1.3, 160],
    "S22" : [1.7, 0.3, 160]
}

kioskXY_Dict = {
    "K11" : [0.3, 3.2, 80],
    "K12" : [1.15, 2.8, 80],
    "K21" : [1.15, 0.5, -80],
    "K22" : [0.3, 0.5, -80]
}


# wayList = [[0, 0, 0]] * 7
# wayList[0] = [0.3, 2.6, 0]      # way1
# wayList[1] = [0.3, 1.5, -80]    # way2
# wayList[2] = [0.3, 0.3, -80]    # way3
# wayList[3] = [1.15, 0.3, 160]   # way4
# wayList[4] = [1.15, 1.3, 160]   # way5
# wayList[5] = [1.15, 1.8, 80]    # way6
# wayList[6] = [1.15, 2.5, 80]    # way7


# 각 노드를 4개 방향별로 지정해 놓는 방법
wayList = [[0, 0, 0]] * 28
wayList[0] = [0.5, 2.6, 0]      # way1 / 0
wayList[1] = [0.5, 2.6, 80]      # way1 / 80
wayList[2] = [0.5, 2.6, -80]      # way1 / -80
wayList[3] = [0.5, 2.6, 160]      # way1 / 160

wayList[4] = [0.5, 1.5, 0]    # way2 / 0
wayList[5] = [0.5, 1.5, 80]    # way2 / 80
wayList[6] = [0.5, 1.5, -80]    # way2 / -80
wayList[7] = [0.5, 1.5, 160]    # way2 / 160

wayList[8] = [0.5, 0.3, 0]    # way3
wayList[9] = [0.5, 0.3, 80]    # way3
wayList[10] = [0.5, 0.3, -80]    # way3
wayList[11] = [0.5, 0.3, 160]    # way3

wayList[12] = [1.15, 0.3, 0]   # way4
wayList[13] = [1.15, 0.3, 80]   # way4
wayList[14] = [1.15, 0.3, -80]   # way4
wayList[15] = [1.15, 0.3, 160]   # way4

wayList[16] = [1.15, 1.3, 0]   # way5
wayList[17] = [1.15, 1.3, 80]   # way5
wayList[18] = [1.15, 1.3, -80]   # way5
wayList[19] = [1.15, 1.3, 160]   # way5

wayList[20] = [1.15, 1.8, 0]    # way6
wayList[21] = [1.15, 1.8, 80]    # way6
wayList[22] = [1.15, 1.8, -80]    # way6
wayList[23] = [1.15, 1.8, 160]    # way6

wayList[24] = [1.15, 2.5, 0]    # way7
wayList[25] = [1.15, 2.5, 80]    # way7
wayList[26] = [1.15, 2.5, -80]    # way7
wayList[27] = [1.15, 2.5, 160]    # way7


# path define
callPathDict = {
    "R1" : {
        "S11" : [[0, 24]],              # 1, 7
        "S12" : [[0, 25, 20],           # 1, 7, 6
                 [1, 4, 20]],           # 1, 2, 6
        "S21" : [[1, 4, 16],            # 1, 2, 5
                 [0, 25, 21, 16]],      # 1, 7, 6, 5
        "S22" : [[1, 4, 17, 12],        # 1, 2, 5, 4
                 [1, 5, 8, 12],         # 1, 2, 3, 4
                 [0, 25, 21, 17, 12]],  # 1, 7, 6, 5, 4
    },
    "R2" : {
        "S11" : [[6, 0, 24],            # 2, 1, 7
                 [4, 22, 24]],          # 2, 6, 7
        "S12" : [[4, 20]],              # 2, 6
        "S21" : [[4, 16]],              # 2, 5
        "S22" : [[4, 17, 12],           # 2, 5, 4
                 [5, 8, 12]],           # 2, 3, 4
    },
    "R3" : {
        "S11" : [[10, 6, 0, 24],        # 3, 2, 1, 7
                 [10, 4, 22, 24],       # 3, 2, 6, 7
                 [8, 14, 18, 22, 24]],  # 3, 4, 5, 6, 7
        "S12" : [[10, 4, 20],           # 3, 2, 6
                 [8, 14, 18, 20]],      # 3, 4, 5, 6
        "S21" : [[8, 14, 16],           # 3, 4, 5
                 [10, 4, 16]],          # 3, 2, 5
        "S22" : [[8, 12]],              # 3, 4
    },
}

deliPathDict = {
    "S11" : {
        "K11" : [[27, 2]],              # 7, 1
        "K12" : [[None]],               # Direct
        "K21" : [[25, 21, 17, 13]],     # 7, 6, 5, 4
        "K22" : [[27, 1, 5, 9],         # 7, 1, 2, 3
                 [25, 23, 5, 9],        # 7, 6, 2, 3
                 [25, 21, 17, 15, 9]],  # 7, 6, 5, 4, 3
    },
    "S12" : {
        "K11" : [[22, 27, 2],           # 6, 7, 1
                 [23, 6, 2]],           # 6, 2, 1
        "K12" : [[22, 26]],             # 6, 7
        "K21" : [[21, 17, 13]],         # 6, 5, 4
        "K22" : [[23, 5, 9],            # 6, 2, 3
                 [21, 17, 15, 9]],      # 6, 5, 4, 3
    },
    "S21" : {
        "K11" : [[19, 6, 2],            # 5, 2, 1
                 [18, 22, 27, 2]],      # 5, 6, 7, 1
        "K12" : [[18, 22, 26]],         # 5, 6, 7
        "K21" : [[17, 13]],             # 5, 4
        "K22" : [[19, 5, 9],            # 5, 2, 3
                 [17, 15, 9]],          # 5, 4, 3
    },
    "S22" : {
        "K11" : [[14, 19, 6, 2],        # 4, 5, 2, 1
                 [15, 10, 6, 2],        # 4, 3, 2, 1
                 [14, 18, 22, 27, 2]],  # 4, 5, 6, 7, 1
        "K12" : [[14, 18, 22, 26]],     # 4, 5, 6, 7
        "K21" : [[None]],               # Direct
        "K22" : [[15, 9]],              # 4, 3
    }
}

returnPathDict = {
    "K11" : {
        "R1" : [[None]],                # Direct
        "R2" : [[1]],                   # 1
        "R3" : [[1, 5]],                # 1, 2
    },
    "K12" : {
        "R1" : [[27, 3]],               # 7, 1
        "R2" : [[27, 1],                # 7, 1
                [25, 23, 7]],           # 7, 6, 2
        "R3" : [[27, 1, 5],             # 7, 1, 2
                [25, 23, 5],            # 7, 6, 2
                [25, 21, 17, 15, 11]],  # 7, 6, 5, 4, 3
    },
    "K21" : {
        "R1" : [[15, 10, 6],            # 4, 3, 2
                [14, 19, 6],            # 4, 5, 2
                [14, 18, 22, 27, 3]],   # 4, 5, 6, 7, 1
        "R2" : [[15, 10],               # 4, 3
                [14, 19, 7]],           # 4, 5, 2
        "R3" : [[15, 11]],              # 4, 3
    },
    "K22" : {
        "R1" : [[10, 6]],               # 3, 2
        "R2" : [[10]],                  # 3
        "R3" : [[None]],                # Direct
    }
}






# # path define
# callPathDict = {
#     "R1" : {
#         "S11" : [[1, 7]],
#         "S12" : [[1, 7, 6], 
#                  [1, 2, 6]],
#         "S21" : [[1, 2, 5],
#                  [1, 7, 6, 5]],
#         "S22" : [[1, 2, 5, 4],
#                  [1, 2, 3, 4],
#                  [1, 7, 6, 5, 4]],
#     },
#     "R2" : {
#         "S11" : [[2, 1, 7],
#                  [2, 6, 7]],
#         "S12" : [[2, 6]],
#         "S21" : [[2, 5]],
#         "S22" : [[2, 5, 4],
#                  [2, 3, 4]],
#     },
#     "R3" : {
#         "S11" : [[3, 2, 1, 7],
#                  [3, 2, 6, 7],
#                  [3, 4, 5, 6, 7]],
#         "S12" : [[3, 2, 6],
#                  [3, 4, 5, 6]],
#         "S21" : [[3, 4, 5],
#                  [3, 2, 5]],
#         "S22" : [[3, 4]],
#     },
# }

# deliPathDict = {
#     "S11" : {
#         "K11" : [[7, 1]],
#         "K12" : [[None]],
#         "K21" : [[7, 6, 5, 4]],
#         "K22" : [[7, 1, 2, 3],
#                  [7, 6, 2, 3],
#                  [7, 6, 5, 4, 3]],
#     },
#     "S12" : {
#         "K11" : [[6, 7, 1],
#                  [6, 2, 1]],
#         "K12" : [[6, 7]],
#         "K21" : [[6, 5, 4]],
#         "K22" : [[6, 2, 3],
#                  [6, 5, 4, 3]],
#     },
#     "S21" : {
#         "K11" : [[5, 2, 1],
#                  [5, 6, 7, 1]],
#         "K12" : [[5, 6, 7]],
#         "K21" : [[5, 4]],
#         "K22" : [[5, 2, 3],
#                  [5, 4, 3]],
#     },
#     "S22" : {
#         "K11" : [[4, 5, 2, 1],
#                  [4, 3, 2, 1],
#                  [4, 5, 6, 7, 1]],
#         "K12" : [[4, 5, 6, 7]],
#         "K21" : [[None]],
#         "K22" : [[4, 3]],
#     }
# }

# returnPathDict = {
#     "K11" : {
#         "R1" : [[None]],
#         "R2" : [[1]],
#         "R3" : [[1, 2]],
#     },
#     "K12" : {
#         "R1" : [[7, 1]],
#         "R2" : [[7, 1],
#                 [7, 6, 2]],
#         "R3" : [[7, 1, 2],
#                 [7, 6, 2],
#                 [7, 6, 5, 4, 3]],
#     },
#     "K21" : {
#         "R1" : [[4, 3, 2],
#                 [4, 5, 2],
#                 [4, 5, 6, 7, 1]],
#         "R2" : [[4, 3],
#                 [4, 5, 2]],
#         "R3" : [[4, 3]],
#     },
#     "K22" : {
#         "R1" : [[3, 2]],
#         "R2" : [[3]],
#         "R3" : [[None]],
#     }
# }