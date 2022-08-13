def calculate_average(query_name):
    for key, value in student_marks.items():
        if(any(x <= 100 for x in value) and any(x >= 0 for x in value)):
            total = sum(student_marks[query_name])
    print(format(total/3, ".2f"))
        
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if(n <= 10 and n >= 2):
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
        calculate_average(query_name)