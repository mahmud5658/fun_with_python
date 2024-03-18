print('Welcome to Samantha\'s Quiz Grading System!')
correct_answer = input('Enter the correct answers for the quiz (in uppercase letters):')
n = int(input("Enter the number of students: "))


for i in range(1,n+1):
    student_answer = input('Enter the responses for student {}: '.format(i))
    count=0
    for j in range(0,len(correct_answer)):
        if correct_answer[j]==student_answer[j]:
            count+=1
    print('Student {}: {}/{}'.format(i,count,len(correct_answer)))
  