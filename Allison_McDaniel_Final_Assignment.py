"""
Name: Student
Description of program
"""


def get_data(fname):
    fileObj = open(fname)
    lines = fileObj.readlines()
    expense_list  = []

    for line in lines[1:]:  # for lines starting at 2 (excluding 1 because it is the
        line_items = line.strip().split(",")  # strip removes the newline character
        expense_list.append([line_items[0], line_items[1], line_items[2]])

    return expense_list


def print_expenses(expense_list):
    """
    display all of the expense records, one per line
    :param expense_list: A list of lists. Each item in the list is a list of Day, amount, category
    :return: None
    """
    for line in expense_list:
        print("Day:", line[0])
        print("Amount:", line[1])
        print("Category:", line[2], "\n")


def display_for_category(expense_list):
    choice = input("""Choose a category to see expenses for where "b” or “B” for beverages; “f” or “F” for food; “e” or 
    “E” for entertainment; “t” or “T” for travel, “c” or “C” for clothing: """)
    choice = choice.lower()
    results = []
    categories = {"b": "beverages", "f": "food", "e": "entertainment", "t": "travel", "c": "clothing"}
    for each in expense_list:
        if each[2].lower() == categories[choice]:
            results.append(each)
    print_expenses(results)


def summarize_by_weekday(expense_list):
    """
    Requirement 3 to display the total amount of money spent on each weekday, aggregated per day.
    That is, display “Monday: $35”, “Tuesday: $54”, etc., where $35 is the sum of dollar amounts for a
    ll Mondays present in the data file, $54 is the sum of dollar amounts for all Tuesdays present in the data file,
    and so on.
    :param expense_list:
    :return: None
    """
    daysDict = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0,
                "Friday": 0, "Saturday": 0, "Sunday": 0}
    for line in expense_list:
        key = line[0]
        val = float(daysDict[key])
        val = val + float(line[1])
        daysDict[key] = val

    for k,v in daysDict.items():
        print(k, '${:,.2f}'.format(v))

def run_ui(expenses):
    while True:
        choice = int(input("\n\nEnter 1 display all of the expense records" +\
                            " \n2 to display all of the expense records for a particular category" + \
                           " \n3 to display the total amount of money spent on each weekday, aggregated per day" + \
                           " \n0 to quit. "))
        if choice == 0:
            print("Good bye!")
            quit()
        elif choice == 1:
            print_expenses(expenses)
            continue
        elif choice == 2:
            display_for_category(expenses)
            continue
        elif choice == 3:
            summarize_by_weekday(expenses)
            continue
        else:
            print("Please enter a valid choice ")


if __name__ == '__main__':
    expense_data = get_data("./expenses.csv")
    run_ui(expense_data)

