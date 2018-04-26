# Test Average and Grade
# 4/19/2018
# CTI-110 P5HW1
# Joshua Allen

def main():


    score1 = float(input("Enter Test Score 1: "))
    score2 = float(input("Enter Test Score 2: "))
    score3 = float(input("Enter Test Score 3: "))
    score4 = float(input("Enter Test Score 4: "))
    score5 = float(input("Enter Test Score 5: "))
    print()

    testAverage = calc_average(score1, score2, score3, score4, score5)
    letGrade = determine_grade(testAverage)

    print ("score\t\tPercentage\tGrade")
    print ("score 1: \t", score1, "\t\t", determine_grade( score1))
    print ("score 2: \t", score2, "\t\t", determine_grade( score2))
    print ("score 3: \t", score3, "\t\t", determine_grade( score3))
    print ("score 4: \t", score4, "\t\t", determine_grade( score4))
    print ("score 5: \t", score5, "\t\t", determine_grade( score5))
    print ()
    print ("Percent Average:  ", testAverage)
    print ("Average Grade: ", determine_grade(testAverage))

def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average

def determine_grade(score):

    if( score < 60 ):
        return "F"
    elif( score < 70 ):
        return "D"
    elif( score < 80 ):
        return "C"
    elif( score < 90 ):
        return "B"
    elif( score < 101):
        return "A"
main()
