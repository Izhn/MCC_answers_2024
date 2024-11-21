import os
from pathlib import Path
# from collections import Counter
question = "3-MagicalOrb"
folder_path = Path(rf"C:\Users\User\Downloads\MCC-DATA\{question}")
num_text_files = len(list(folder_path.glob('input*.txt')))

if __name__ == "__main__":


    def write(ans, i):
        global question
        with open(rf"C:\Users\User\Downloads\MCC-DATA\{question}\output{i}.txt", "w") as file:
            
            for num in ans:
                file.write(f"{num}\n")


    def MagicOrb(T, list2):
        ans_list = []

        for i in range(T):
            curr = 0
            curr_list = list2[i][1]
            curr_list.sort()
            for j in range(list2[i][0]):
                curr += curr_list[j] * 2**j
            ans = curr % (10**9 + 7)
            # print(ans)
            ans_list.append(ans)

        return ans_list

    for i in range(1, num_text_files):
    # for i in range(1,2):
        # print("-------------------")
        curr_path = folder_path / f"input{str(i)}.txt"
        with open(curr_path, "r") as file:
            content = file.read()

        lines = content.splitlines()
        T = int(lines[0])
        list2 = [(int(lines[(i*2-1)]) , list(map(int, lines[(i*2)].split()))) for i in range(1, T + 1)]

        a = MagicOrb(T, list2)
        print(i)
        write(a, i)

