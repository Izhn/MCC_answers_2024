import os
from pathlib import Path
# from collections import Counter
question = "4-SimpleGame"
folder_path = Path(rf"C:\Users\User\Downloads\MCC-DATA\{question}")
num_text_files = len(list(folder_path.glob('input*.txt')))

if __name__ == "__main__":

    # def check(num, i):
    #     curr_path = folder_path / f"output{str(i)}.txt"
    #     with open(curr_path, "r") as file:
    #         content = file.read()   
    #     if int(content) == num:
    #         return True
    #     else:
    #         return False

    def write(ans, i):
        global question
        with open(rf"C:\Users\User\Downloads\MCC-DATA\{question}\output{i}.txt", "w") as file:
            
            file.write(str(ans))


    def SimpleGame(T, list2):

        X = 0
        Y = 0

        list2.sort(key= lambda x: x[0] + x[1], reverse=True)

        for i in range(T):
            
            if i % 2 == 0:
                X += list2[i][0]
            
            else:
                Y += list2[i][1]
        

        return X - Y
                
                




    # for i in range(1, num_text_files + 1):
    for i in range(1,2):
        # print("-------------------")
        curr_path = folder_path / f"input{str(4)}.txt"
        with open(curr_path, "r") as file:
            content = file.read()

        lines = content.splitlines()
        # print(lines)
        T = int(lines[0])
        list2 = [list(map(int, lines[(i)].split())) for i in range(1, T + 1)]

        a = SimpleGame(T, list2)
        print(a)
        write(a, i)
        # print(check(a, i))
