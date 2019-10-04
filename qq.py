# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

# code-

l = []
a=[]
p=[]
t=[]
s=[]
r=[]
x=int(input("enter total number of students:-"))
for j in range(x):
    name = input("enter name:-")
    score = float(input("enter marks:-"))
    if(score>=0):
        l.append([name, score])
        l.sort(reverse=True, key=lambda l: l[1])
    else:
        p.append([name,score])
        p.sort(reverse=True, key=lambda p: p[1])
if(len(l)>3):
    if (l[-1][1] == l[-2][1]):
        if (l[-3][1] != l[-4][1]):
            print(l[-3][0])
        else:
            if (l[-3][1] == l[-4][1]):
                if (l[-4][1] == l[-5][1]):
                    a.append(l[-3][0])
                    a.append(l[-4][0])
                    a.append(l[-5][0])
                    a.sort(reverse=False, key=lambda a: a[0])
                    print(a[0])
                    print(a[1])
                    print(a[2])
                else:
                    a.append(l[-3][0])
                    a.append(l[-4][0])
                    a.sort(reverse=False, key=lambda a: a[0])
                    print(a[0])
                    print(a[1])
    else:
        if (l[-2][1] != l[-3][1]):
            print(l[-2][0])
        else:
            if (l[-2][1] == l[-3][1]):
                if (l[-3][1] == l[-4][1]):
                    a.append(l[-2][0])
                    a.append(l[-3][0])
                    a.append(l[-4][0])
                    a.sort(reverse=False, key=lambda a: a[0])
                    print(a[0])
                    print(a[1])
                    print(a[2])
                else:
                    a.append(l[-2][0])
                    a.append(l[-3][0])
                    a.sort(reverse=False, key=lambda a: a[0])
                    print(a[0])
                    print(a[1])

else:
    if (len(l) == 1):
        print(l[-1][0])
    elif(len(l)==0):
        if (len(p) > 3):
            if (p[-1][1] == p[-2][1]):
                if (p[-3][1] != l[-4][1]):
                    print(p[-3][0])
                else:
                    if (p[-3][1] == p[-4][1]):
                        if (p[-4][1] == p[-5][1]):
                            t.append(p[-3][0])
                            t.append(p[-4][0])
                            t.append(p[-5][0])
                            t.sort(reverse=False, key=lambda t: t[0])
                            print(t[0])
                            print(t[1])
                            print(t[2])
                        else:
                            t.append(p[-3][0])
                            t.append(p[-4][0])
                            t.sort(reverse=False, key=lambda t: t[0])
                            print(t[0])
                            print(t[1])
            else:
                if (p[-2][1] != p[-3][1]):
                    print(p[-2][0])
                else:
                    if (p[-2][1] == p[-3][1]):
                        if (p[-3][1] == p[-4][1]):
                            t.append(p[-2][0])
                            t.append(p[-3][0])
                            t.append(p[-4][0])
                            t.sort(reverse=False, key=lambda t: t[0])
                            print(t[0])
                            print(t[1])
                            print(t[2])
                        else:
                            t.append(p[-2][0])
                            t.append(p[-3][0])
                            t.sort(reverse=False, key=lambda t: t[0])
                            print(t[0])
                            print(t[1])

if(len(l) == 3):
        if (l[-1][1] == l[-2][1]):
            if (l[-2][1] == l[-3][1]):
                a.append(l[-1][0])
                a.append(l[-2][0])
                a.append(l[-3][0])
                a.sort(reverse=False, key=lambda a: a[0])
                print(a[0])
                print(a[1])
                print(a[2])
        elif(l[-1][1] != l[-2][1]):
            if (l[-2][1] == l[-3][1]):
                a.append(l[-2][0])
                a.append(l[-3][0])
                a.sort(reverse=False, key=lambda a: a[0])
                print(a[1])
                print(a[0])
            else:
                if (l[-2][1] != l[-3][1]):
                    print(l[-2][0])
