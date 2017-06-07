import re

import numpy
import numpy as np


def spider_to_spider(file_param):



    file_read = open(file_param, 'r')
    file = file_read.readline()

    # file = file_read.readline()
    # print(file)


    final_list = []

    num_lines = sum(1 for line in open(file_param, 'r'))
    # num_lines -= 1
    matrix = [[0 for x in range(8)] for y in range(8)]
    probability_matrix = [[0 for x in range(3)] for y in range(3)]

    i = 0

    a = []

    while i < num_lines - 1:
        i += 1

        str1 = file_read.readline()
        # print(str1)
        # str1 = re.findall("-?\d+", str1)

        l = str1.rstrip('\n').split('\t')
        # l = list(l)
        # l = list(map(str, l[3:10]))
        # str1 = str1[11:]
        # print(l[3:])
        # l = ','.join(l[3:])
        # print(l)
        a.append(l[3:])

    array = a
    # print(a)
    # break

    degree_matrix = [[0 for x in range(8)] for y in range(num_lines - 1)]

    degree_index = 0

    for x in range(0, num_lines - 1):
        degree_index = 0
        for y in range(1, 5):
            # print("x = ", x , " y = ", y , " deg_index = ",degree_index)
            degree_matrix[x][degree_index] = numpy.math.sin(float(array[x][y]) * numpy.pi / 180)
            degree_matrix[x][degree_index + 1] = numpy.math.cos(float(array[x][y]) * numpy.pi / 180)
            degree_index += 2

            # print()

    # print(len(array))
    # print(len(array[0]))
    # print(len(degree_matrix))
    # print(len(degree_matrix[0]))

    temp_array = array

    array = degree_matrix

    # print(num_lines - 1)

    # print(array[0])
    # print()
    # print(degree_matrix[0])
    #
    #

    #
    #

    num_lines -= 1

    for k in range(0, 8):
        for l in range(0, 8):
            for i in range(0, num_lines - 1):
                # print("k = ", k, " l = ", l, " i = ", i)
                matrix[k][l] += float(array[i][k]) * float(array[i + 1][l])
            matrix[k][l] = matrix[k][l] / (num_lines - 1)

    # print(matrix)
    # print(" rows ", len(matrix), " cols ", len(matrix[0]))

    array = temp_array

    for k in range(0, 3):
        for l in range(5, 8):
            for i in range(0, num_lines - 1):
                # print("k = ", k, " l = ", l, " i = ", i)
                probability_matrix[k][l - 5] += numpy.float(array[i][k]) * numpy.float(array[i + 1][l - 5])
                # print(probability_matrix[k][j-5])
            probability_matrix[k][l - 5] = probability_matrix[k][l - 5] / (num_lines - 1)
            # print(k,i,j)

    # print(probability_matrix)
    # print(" rows ", len(probability_matrix), " cols ", len(probability_matrix[0]))




    final_matrix = [[0 for x in range(73)] for y in range(1)]
    index = 0
    for m in range(0, len(matrix)):
        for n in range(0, len(matrix[m])):
            final_matrix[0][index] = matrix[m][n]
            index += 1
    # index = 0
    for m in range(0, len(probability_matrix)):
        for n in range(0, len(probability_matrix[0])):
            final_matrix[0][index] = probability_matrix[m][n]
            index += 1

    # print(final_matrix[0])
    # print(" rows ", len(final_matrix), " cols ", len(final_matrix[0]))

    # break

    matrix = final_matrix

    # print(matrix[0])

    return list(matrix[0])

if __name__ == '__main__':
    file = '/home/farshid/Desktop/GPCR_seqs/hsa134.txt.spd3'
    print( spider_to_spider(file) )

