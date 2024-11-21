import os
from pathlib import Path
import math

# from collections import Counter
question = "5-ExplodingArrow"
folder_path = Path(rf"C:\Users\User\Downloads\MCC-DATA\{question}")
num_text_files = len(list(folder_path.glob('input*.txt')))

if __name__ == "__main__":

    def write(ans, i):
        global question
        with open(rf"C:\Users\User\Downloads\MCC-DATA\{question}\output{i}.txt", "w") as file:
            
            file.write(str(ans))


    def destroy_targets(N, M, K, X, list2):
        # print("Hi")
        # print(list2)
        curr_list = list2.copy()
        curr_a = 0
        curr_t = 0
        d_list = []
        nj = 0
        # print(curr_list)
        for j in range(N):
            
            d = max(0, M * X - (j)**2)
            # print(d)
            if d == 0:
                continue
            d_list.append(d)
        
        nj = len(d_list)

        while curr_a < K:
            if curr_t == N - 1 and curr_list[-1] <= 0:
                return True
            if curr_list[curr_t] <= 0:
                curr_t += 1
                continue
  
            curr_a += 1


            for i, d in enumerate(d_list):

                if curr_t + i >= N:
                    continue

                curr_list[curr_t + i] -= d
            # print(curr_list, d_list, X)

            if max(curr_list) <= 0:
                return True
            
        return False
    

    def ExplodingArrow(N, M, K, list2):
        # print("Hi")
        # worst possible scenariao would be the highest hp of target is at the back and you have only K arrow
        ub = int(math.ceil((N - 1)**2 * (max(list2)/K))/ M)
        # ub = max(list2)

        l, r = 1, ub

        X = r

        while l <= r:
            print(X,l,r)
            # print(l, r, X)

            # print(list2)
            # print(l, r, X)
            m = (l + r) // 2
            # print(m, l, r, X)
            if destroy_targets(N, M, K, m, list2):
                X = m
                r = m - 1
            
            else:
                l = m + 1
        # print(X)
        return X

    # for i in range(1, num_text_files + 1):
    for i in range(1,2):
        # print("-------------------")
        curr_path = folder_path / f"input{str(7)}.txt"
        with open(curr_path, "r") as file:
            content = file.read()

        lines = content.splitlines()
        # print(lines)
        # print(lines)
        T = list(map(int, lines[0].split()))
        N, M, K = T
        list2 = list(map(int, lines[(1)].split()))
        # print(N)
        # print(destroy_targets(N, M, K,4, list2))
        a = ExplodingArrow(N, M, K, list2)
        print(a)
        write(a, i)
