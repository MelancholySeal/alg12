#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys


def edit_dist(a, b, len_a, len_b):
    """
    Поиск расстояния редактирования и восстановление решения.
    """
    def edit_dist_td(i, j):
        """
        Динамическое программирование сверху вниз
        """
        if matrix[i][j] == infinity:
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            else:
                ins = edit_dist_td(i, j-1) + 1
                delete = edit_dist_td(i-1, j) + 1
                sub = edit_dist_td(i-1, j-1) + (a[i-1] != b[j-1])
                matrix[i][j] = min(ins, delete, sub)

        return matrix[i][j]

    def restore():
        """
        Восстановление решения
        """
        str_re1, str_re2 = [], []
        i, j = len_a, len_b
        while (i, j) != (0, 0):
            if i != 0 and matrix[i][j] == matrix[i-1][j] + 1:
                str_re1.append(a[i-1])
                str_re2.append('-')
                i -= 1

            elif j != 0 and matrix[i][j] == matrix[i][j-1] + 1:
                str_re1.append('-')
                str_re2.append(b[j-1])
                j -= 1

            elif matrix[i][j] == matrix[i-1][j-1] + (a[i-1] != b[j-1]):
                str_re1.append(a[i-1])
                str_re2.append(b[j-1])
                i -= 1
                j -= 1

        str_re1.reverse()
        str_re2.reverse()

        return (str_re1, str_re2)


    def edit_dist_bu():
        """
        Динамическое программирование снизу вверх
        """
        matrix = []
        for i in range(len_a+1):
            matrix.append([i])
        for j in range(1, len_b+1):
            matrix[0].append(j)
        for i in range(1, len_a+1):
            for j in range(1, len_b+1):
                c = a[i-1] != b[j-1]
                matrix[i].append(min(
                    matrix[i-1][j] + 1,
                    matrix[i][j-1] + 1,
                    matrix[i-1][j-1] + c
                ))
        return matrix

    
    infinity = math.inf
    matrix = [[infinity] * (len_b+1) for _ in range(len_a+1)]
    edit_1, edit_2 = edit_dist_td(len_a, len_b), edit_dist_bu()
    solution = restore()

    if matrix == edit_2:
        return edit_1, solution
    
    else:
        print("Неверно", file=sys.stderr())
        exit(1)


def main():
    str_1 = "editing"
    str_2 = "distance"
    edit, solution = edit_dist(
        str_1, 
        str_2, 
        len(str_1), 
        len(str_2)
    )

    print(edit)
    for item in solution:
        print(item)


if __name__ == '__main__':
    main()