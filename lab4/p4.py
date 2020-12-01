# 1155108381 1155110154 
# lab 4 p4

import csv

def get_average_grades(filename='grades.csv'):
    with open(filename,newline='') as csvfile:
        records = list(csv.reader(csvfile))
    assg, total = [0,0,0,0],[0,0,0,0]
    for score in records:
        for i in range(4):
            assg[i] += 1 if score[i] != '-1' else 0
            total[i] += float(score[i]) if score[i] != '-1' else 0
    average_grades_list = [total[i]/assg[i] for i in range(4)]    
    return average_grades_list

# print(get_average_grades())