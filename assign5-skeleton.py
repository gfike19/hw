'''
author: Student Name
'''

def get_data():
    fileObj = open("./exam-scores.csv")
    lines = fileObj.readlines()  
    dict_scores = {}

    for line in lines[1:]:  
        lst_items = line.strip().split(",")  
        dict_scores[lst_items[0]] = (float(lst_items[1]), float(lst_items[2]))

    return dict_scores

def print_menu():
    print("\nEnter 1 to see all the scores")
    print("2 to see a particular student's score")
    print("3 to see the class average on a particular test")
    print("4 to see the students with the highest score")
    userchoice = int(input("and 0 to quit."))
    return userchoice

def display_all_data(dict_scores):
    print("Here are all the students' scores:")
    for stdname in dict_scores:
        print("%s: %f  %f" %(stdname, dict_scores[stdname][0], dict_scores[stdname][1]))

def display_specific_student_score(dict_scores):
    student_name = input("Provide the student's name whose scores you would like to retrieve: ")
    if not student_name in dict_scores:
        print("Student %s is not present in our records!" % student_name)
    else:
        print("Student %s's scores are: %s" % (student_name,
                                            str(dict_scores[student_name][0]) +
                                            " " + str(dict_scores[student_name][1])))

def display_average_score(dict_scores):
    test_no = int(input("Enter the number for the test: 1 for the first test and 2 for the second test:  "))
    if not test_no in (1, 2):
        print("Please enter a valid test number: either 1 or 2. You have entered: %d" %test_no)
    else:
        total = 0
        for key in dict_scores:
            total += dict_scores[key][test_no - 1]
        print("The avg. score on test %d is %f" %(test_no, total/len(dict_scores)))


def get_max_score(dict_scores, test_no):
    maxScore = 0
    for key in dict_scores:
        if (maxScore < dict_scores[key][test_no - 1]):
            maxScore = dict_scores[key][test_no - 1]
    return maxScore

def display_max_scores_on_test(dict_scores):
    test_no = int(input("Enter the number for the test: 1 for the first test and 2 for the second test:  "))
    if not test_no in (1, 2):
        print("Please enter a valid test number: either 1 or 2. You have entered: %d" %test_no)
    else:
        maxScore = get_max_score(dict_scores, test_no)
        print("max score is " + str(maxScore))
        for key in dict_scores:
            if (dict_scores[key][test_no - 1] == maxScore):
                print("%s had a test score of %d" %(key, dict_scores[key][test_no - 1]))
    

def run_ui():
    dict_scores = get_data()
    while True:
        choice = print_menu()

        if choice == 0:
            print("Good bye!")
            quit()
        elif choice == 1:
            display_all_data(dict_scores)
        elif choice == 2:
            display_specific_student_score(dict_scores)
        elif choice == 3:
            display_average_score(dict_scores)
        elif choice == 4:
            display_max_scores_on_test(dict_scores)
        else:
            print("%d is an invalid choice" %(choice))

if __name__ == '__main__':
    run_ui()