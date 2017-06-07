import re
import numpy as np
import mysql.connector

def pssm_to_bigram(file_param):

    # return file_param
    # print(file_param.readline())
#
    file = open(file_param, 'r')
    # file  = file_param
    file.readline()
    file.readline()
    file.readline()
    final_list = []
    num_lines = sum(1 for line in open(file_param, 'r'))
    num_lines = num_lines - 6 - 3  # 6 from the bottom 3 from the top
    array = np.zeros(shape=(num_lines, 20))

    matrix = [[0 for x in range(20)] for y in range(20)]

    # num_lines = sum(1 for line in open('/home/farshid/Desktop/Enzyme_seqs/' + hsa, 'r'))

    # def __init__(self):




    # return str

    # def create_final_list(self):


    i = 0

    while i < num_lines:
        str1 = file.read(89)
        str1 = str1[11:]
        a = []

        str1 = re.findall("-?\d+", str1)

        file.readline()
        final_list.append(str1)
        i = i + 1

    array = final_list

    for m in range(0, 20):
        for n in range(0, 20):
            for i in range(0, num_lines - 1):
                matrix[m][n] += int(array[i][m]) * int(array[i + 1][n])
            matrix[m][n] = matrix[m][n] / num_lines
            # def write(self,matrix):

    # print(len( matrix) )
    # print(len( matrix[0]) )
    # print(sum(matrix , []))

    return sum(matrix , [])

# if __name__ == '__main__':
#
#     file_param = '/home/farshid/Desktop/GPCR_seqs/hsa134.txt.pssm'
#     print(pssm_to_bigram(file_param))