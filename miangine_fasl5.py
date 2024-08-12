l5=[]
l4 = []
l3=[]
l =[]
l2=[]
d={}
l1=[]
import csv
# For the average
from statistics import mean 
def calculate_averages(input_file_name='scorse.csv',output_file_name='natige.csv',mode='w'):
    with open('scorse.csv') as file:
        reader = csv.reader(file)
    file = open('scorse.csv',mode='r')
    for lines in file:
        lines = lines.strip()
        j_lines = lines.split(",")
        names = j_lines[0]
        l5.append(names)
        scores = j_lines[1:]
        for i in j_lines[1:]:
            l.append(int(i))
        m_scores = mean(l)
        l.clear()
        l1.append(m_scores)
    for names,avarages in zip(l5,l1):
        print(names,avarages)    
calculate_averages()
def calculate_sorted_averages(input_file_name='scorse.csv',output_file_name='natige.csv',mode='w'):
    with open('scorse.csv') as file:
        reader = csv.reader(file)
    file = open('scorse.csv',mode='r')
    for lines in file:
        lines = lines.strip()
        j_lines = lines.split(",")
        l2.append(j_lines)
        f = l2.sort()
    for u in l2:
        l6=[]
        names = u[0]
        l6.append(names)
        scores = u[1:]
        for g in u[1:]:
            l3.append(int(g))
        m_scores = mean(l3)
        l3.clear()
        l4.append(m_scores)
        for names,jj in zip(l6,l4):
            print(names,m_scores)
def calculate_three_best(input_file_name='scorse.csv',output_file_name='natige.csv',mode='w'):
    with open('scorse.csv') as file:
        reader = csv.reader(file)
    file = open('scorse.csv',mode='r')
    for lines in file:
        lines = lines.strip()
        j_lines = lines.split(",")
        names = j_lines[0]
        l5.append(names)
        scores = j_lines[1:]
        for i in j_lines[1:]:
            l.append(int(i))
        m_scores = mean(l)
        l.clear()
        l1.append(m_scores)
    for names,avarages in zip(l5,l1):
        d[names] = avarages
    s_d = dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
    n=0
    for names,avarages in zip(s_d.keys(),s_d.values()):
        n+=1
        print(names,avarages)
        if n ==3:
            break
calculate_three_best()
def calculate_three_worst(input_file_name='scorse.csv',output_file_name='natige.csv',mode='w'):
    with open('scorse.csv') as file:
        reader = csv.reader(file)
    file = open('scorse.csv',mode='r')
    for lines in file:
        lines = lines.strip()
        j_lines = lines.split(",")
        names = j_lines[0]
        l5.append(names)
        scores = j_lines[1:]
        for i in j_lines[1:]:
            l.append(int(i))
        m_scores = mean(l)
        l.clear()
        l1.append(m_scores)
    for names,avarages in zip(l5,l1):
        d[names] = avarages
    s_d = dict(sorted(d.items(),key=lambda x:x[1]))
    n=0
    for names,avarages in zip(s_d.keys(),s_d.values()):
        n+=1
        print(avarages)
        if n ==3:
            break    
calculate_three_worst()
def calculate_average_of_averages(input_file_name='scorse.csv',output_file_name='natige.csv',mode='w'):
    with open('scorse.csv') as file:
        reader = csv.reader(file)
    file = open('scorse.csv',mode='r')
    for lines in file:
        lines = lines.strip()
        j_lines = lines.split(",")
        scores = j_lines[1:]
        for i in j_lines[1:]:
            l.append(int(i))
        m_scores = mean(l)
        l.clear()
        l1.append(m_scores)
    s = mean(l1)
    print(s)
calculate_average_of_averages()
