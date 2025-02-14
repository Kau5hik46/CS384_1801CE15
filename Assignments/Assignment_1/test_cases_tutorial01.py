import tutorial01 as A1

inf = float('inf')

actual_answers = [9, 12, 8, 7, 0, 0, inf, [2, 6, 18, 54, 162]]
student_answers = []

test_case_1 = A1.add(4, 5)
student_answers.append(test_case_1)

test_case_2 = A1.subtract(14, 2)
student_answers.append(test_case_2)

test_case_3 = A1.multiply(4, 2)
student_answers.append(test_case_3)

test_case_4 = A1.divide(14, 2)
student_answers.append(test_case_4)

test_case_5 = A1.add('ans', 2)
student_answers.append(test_case_5)

test_case_6 = A1.add('ans', '2')
student_answers.append(test_case_6)

test_case_7 = A1.divide(14, 0)
student_answers.append(test_case_7)

a = 2 # starting number 
r = 3 # Common ratio 
n = 5 # N th term to be find 

gp = A1.printGP(a, r, n) 
gp = list(gp) 
student_answers.append(gp)

print(actual_answers)
print(student_answers)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == y:
        count_of_correct_test_cases += 1

print(f"Test Cases Passed = '{count_of_correct_test_cases}'  / '{total_test_cases}'")
