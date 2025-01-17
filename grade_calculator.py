#A program that accept student grade score then display the grade letter to the student

grade_score=int(input('\nPlease enter your grade percentage : '))

if grade_score >= 90:
    grade_letter = 'A'
elif grade_score >= 80:
    grade_letter = 'B'
elif grade_score >= 70:
    grade_letter = 'C'
elif grade_score >= 60:
    grade_letter = 'D'
else:
    grade_letter = 'F'

print(f'\nYour letter grade is : {grade_letter}\n')

if grade_score >= 70:
    print(f'Congratulations! you passed the class \n')
else:
    print(f'Stay focused and you\'ll get it next time!\n')
