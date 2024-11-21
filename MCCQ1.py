import os
from pathlib import Path
question = "1-CornerCover"
folder_path = Path(rf"C:\Users\User\Downloads\MCC-DATA\{question}")
num_text_files = len(list(folder_path.glob('input*.txt')))

if __name__ == "__main__":

    def CornerCover(N, list2):

        for i in range(N):
            curr_list = list2[i]
            n, m ,A, B = curr_list
            if m > n:
                n, m = m, n
            if B > A:
                A, B = B, A
            # print(A,n,B,m)
            if A > n or B > m:
                print("NO")
                continue

            if A == n or B == m:
                print("YES")
                continue

            elif (A == m or B == n) and A <= m and B <= n:
                print("YES")
                continue

            else:
                print("NO")
                continue
                
        return
   
    for i in range(1, num_text_files + 1):
    # for i in range(1,2):
        print("-------------------")
        curr_path = folder_path / f"input{str(5)}.txt"
        with open(curr_path, "r") as file:
            content = file.read()

        lines = content.splitlines()
        N = int(lines[0])
        list2 = [list(map(int, lines[i].split())) for i in range(1, N + 1)]

        CornerCover(N, list2)

