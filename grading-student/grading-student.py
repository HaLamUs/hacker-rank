#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def findClosestMultipleOfFive(grade):
    return ((grade // 5) + 1) * 5

def groundUp(grade, nextMultiple):
    if nextMultiple - grade < 3:
        return nextMultiple
    else:
        return grade
    
    
# 1. find next multiple of 5 from given
# 2. ground up if meet condition 
# 3. print
def gradingStudents(grades):
    newGrades = []
    for grade in grades:
        if grade < 38:
            newGrades.append(grade)
        else:
            nextMultiple = findClosestMultipleOfFive(grade)
            newGrade = groundUp(grade, nextMultiple)
            newGrades.append(newGrade)
    return newGrades



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
