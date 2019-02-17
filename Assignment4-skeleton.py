'''
author: Student Name

For this assignment, you will create a Python program that meets the following requirements:

Extends the Score Reporting Program, shown in the third demonstration video for this week
(code + data files accompanying these instructions), but providing an option 4. (1 point)

In the menu of options, adds an option for 4, whose instruction is: "display a list of students whose score on
a particular exam is the highest". Then, when option 4 is chosen, displays a prompt asking for the
exam number (1 or 2). (1 point)

When the user chooses option 4, and then enters an exam number, the program validates the entry by checking
to see that the option chosen is either 1 or 2. When any other value is chosen by the user, an appropriate error
is displayed (similar to the error message shown in the case of option 3). (2 points)

When the user chooses a correct test for option for, displays a list of all students whose score matches
the highest score on the chosen exam. (6 points)

Submit your work in the form of a Python file (.py extension), with your name and "assignment_4" in its filename.
In a docstring at the top of the file, include your name, and "application assignment 4".
'''

# read the file from the current directory. Putting the exam-scores.csv file in the same directory as you put
# this program will work. Or you can change the string below to point to the file when you open it.
fileObj = open("./exam-scores.csv")
lines = fileObj.readlines()  # readlines returns a list of all the lines in the
dict_scores = {}

for line in lines[1:]:  # for lines starting at 2 (excluding 1 because it is the
    lst_items = line.strip().split(",")  # strip removes the newline character a
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
            lst = []
            for stdname in dict_scores:
                lst.append(dict_scores[stdname][test_no - 1])
            maxscore = max(lst)
            print("The highest score was", maxscore)
            for stdname in dict_scores:
                if dict_scores[stdname][test_no -1] == maxscore:
                    print(stdname)
            # maxScore = 0
            # for key in dict_scores:
            #     if maxScore < dict_scores[key][test_no - 1]:
            #         maxScore = dict_scores[key][test_no - 1]
            # print("The max. score on test %d is %f" %(test_no, maxScore))
            # for key in dict_scores:
            #     if maxScore == dict_scores[key][test_no - 1]:
            #         print(key)

        #At this point you have the maximum score on this test stored in maxScore
        #TODO Loop through the list and print everyone who has a score == to maxScore.
        # Your loop will look a lot like the one used above to find the maxScore

    #end our new code

    else:
        print("%d is an invalid choice" %(choice))