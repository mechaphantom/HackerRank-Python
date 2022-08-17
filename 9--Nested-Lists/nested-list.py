#Solution for Python 3
def secondLowestMarks(students):
    lowest_mark = min(students, key = lambda stu: stu[1])[1];
    students = [stu for stu in students if stu[1] != lowest_mark]
    #filter(lambda stu: stu[1] == lowest_mark, students);
    second_lowest_mark = min(students, key = lambda stu: stu[1])[1];
    return sorted([stu[0] for stu in students if stu[1] == second_lowest_mark]);

def secondLowestMarks2(students):
    "If there's a tie for lowest mark we include all."
    students.sort();
    picked_students = sorted(filter(lambda x: x[1] == students[1][1], students));
    return [stu[0] for stu in picked_students];

if __name__ == "__main__":
    num_students = int(input());
    students = [[input(),float(input())] for i in range(num_students)];
    for student in secondLowestMarks(students):
        print(student);
        
#Solution for Python 2
"""
d={} 
for _ in range(int(raw_input())): 
    Name=raw_input() 
    Grade=float(raw_input()) 
    d[Name]=Grade 
v=d.values()
second=sorted(list(set(v)))[1] 
second_lowest=[] 
for key,value in d.items():  
    if value==second: 
        second_lowest.append(key) 
second_lowest.sort() 
for name in second_lowest: 
    print(name)
"""