import os
from pathlib import Path
import math

# from collections import Counter
question = "6-XORstring"
folder_path = Path(rf"C:\Users\User\Downloads\MCC-DATA\{question}")
num_text_files = len(list(folder_path.glob('input*.txt')))

if __name__ == "__main__":

    def write(ans, i):
        global question
        with open(rf"C:\Users\User\Downloads\MCC-DATA\{question}\output{i}.txt", "w") as file:
            
            file.write(str(ans))


    def count_pairs(list2, N):
        dict_a = {'00': 0, '01': 0, '11': 0}
        p = N - 1  
        
        for i in range(p):
            pair = list2[i:i+2]  
            if pair == '00':
                dict_a['00'] += (i+1) * (p-i)
            elif pair == '01' or pair == '10':
                dict_a['01'] += (i+1) * (p-i)  
            elif pair == '11':
                dict_a['11'] += (i+1) * (p-i)
        # print(dict_a)
        return dict_a


    def transform(dict_a):

        a = dict_a['11']
        b = dict_a['01']
        c = dict_a['00']

        dict_a['11'] = 0
        dict_a['11'] += b
        dict_a['01'] += 2*a
        dict_a['00'] += c

        return dict_a
    

    def Findsum(N, K, list2):

        dict_a = count_pairs(list2, N)

        for _ in range(K):
            dict_a = transform(dict_a)

        return (dict_a['00'] + dict_a['11']) % 998244353

    for i in range(1, num_text_files + 1):
    # for i in range(1,2):
        curr_path = folder_path / f"input{str(i)}.txt"
        with open(curr_path, "r") as file:
            content = file.read()

        lines = content.splitlines()

        T = list(map(int, lines[0].split()))
        N, K = T
        list2 = lines[1]
        a = Findsum(N, K, list2)
        print(a)
        write(a, i)
