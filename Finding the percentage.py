if __name__ == '__main__':
    n = int(input())  
    student_marks = {}  

    for _ in range(n):
        name, *line = input().split() 
        scores = list(map(float, line))  
        student_marks[name] = scores  

    query_name = input() 
    scores = student_marks[query_name] 

    
    Avg = sum(scores) / len(scores)
    print(f"{Avg:.2f}")  
