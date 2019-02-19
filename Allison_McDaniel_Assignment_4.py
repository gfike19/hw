'''
Allison McDaniel

This progtam is to find information on students test scores.
'''

fileObj = open("./exam-scores.csv")
lines = fileObj.readlines()
dict_scores = {}

for line in lines[1:]:
    lst_items = line.strip().split(",")  
    print(lst_items)
    dict_scores[lst_items[0]] = (float(lst_items[1]), float(lst_items[2]))

print(dict_scores)

while True:
    print("\nEnter 1 to see all the scores")
    print("2 to see a particular student's score")
    print("3 to see the class average on a particular test")
    print("4 to see a list of students whose score on a particular exam is the highest")
    choice = int(input("and 0 to quit."))

    if choice == 0:
        print("Good bye!")
        quit()
    elif choice == 1:
        print("Here are all the students' scores:")
        for stdname in dict_scores:
            print("%s: %f  %f" %(stdname, dict_scores[stdname][0], dict_scores[stdname][1]))
    elif choice == 2:
        student_name = input("Provide the student's name whose scores you would like to retrieve: ")
        if not student_name in dict_scores:
            print("Student %s is not present in our records!" % student_name)
        else:
            print("Student %s's scores are: %s" % (student_name,
                                                   str(dict_scores[student_name][0]) +
                                                   " " + str(dict_scores[student_name][1])))
    elif choice == 3:
        test_no = int(input("Enter the number for the test: 1 for the first test and 2 for the second test:  "))
        if not test_no in (1, 2):
            print("Please enter a valid test number: either 1 or 2. You have entered: %d" %test_no)
        else:
            total = 0
            for key in dict_scores:
                total += dict_scores[key][test_no - 1]
            print("The avg. score on test %d is %f" %(test_no, total/len(dict_scores)))


    elif choice == 4:
        test_no = int(input("Enter the number for the test: 1 for the first test and 2 for the second test:  "))
        if not test_no in (1, 2):
            quit()
        else:
            maxScore = 0
            for key in dict_scores:
                if maxScore < dict_scores[key][test_no - 1]:
                    maxScore = dict_scores[key][test_no - 1]
            print("The max. score on test %d is %f" %(test_no, maxScore))
            for key in dict_scores:
                if maxScore == dict_scores[key][test_no - 1]:
                    print(key)

    else:
        print("%d is an invalid choice" %(choice))