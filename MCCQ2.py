import os
from pathlib import Path
# from collections import Counter
question = "2-Gifts"
folder_path = Path(rf"C:\Users\User\Downloads\MCC-DATA\{question}")
num_text_files = len(list(folder_path.glob('input*.txt')))

if __name__ == "__main__":

    def write(ans, i):
        global question
        with open(rf"C:\Users\User\Downloads\MCC-DATA\{question}\output{i}.txt", "w") as file:
            file.write(ans)


    def Gifts(list1, list2):
        n, m = list1
        curr = 0
        ans_list = []
        l = list2.copy()
        l.sort()
        tR = l.pop(m - 1)
        for i in range(n):
            if list2[i] < tR:
                curr += 1
                ans_list.append(1)
            else:
                ans_list.append(0)
                # continue
        for i in range(n):
            if curr != m and list2[i] == tR:
                curr +=1
                ans_list[i] = 1

        return " ".join(map(str, ans_list))
   
    for i in range(1, num_text_files):
    # for i in range(1,2):
        # print("-------------------")
        curr_path = folder_path / f"input{str(i)}.txt"
        with open(curr_path, "r") as file:
            content = file.read()

        lines = content.splitlines()
        list1 = list(map(int, lines[0].split()))
        list2 = list(map(int, lines[1].split()))

        a = Gifts(list1, list2)
        write(a, i)
