

import os
import csv

months = []
revenue = []
revenue_change = []
lines = []
voter_id_values = []
total_votes = []
candidate_votes = []
unique_candidate = []
candidate_values = []
budget_process = False

# Function for generating needed lists
def define_lists(line_data, field_name):
    field_values = []

    for count, item in enumerate(line_data):
        for count, key in enumerate(item.keys()):
            if key == field_name:
                field_val = item.get(field_name)
                field_values.append(field_val)
    return field_values


# open and assign csv file to string variable and read into output variable
with open("C:/Users/vasqu/PyCharmProjects/venv_conda/python_challenge/py_challenge_git/PyBank/election_data.csv", "r") as csv_input:
    if csv_input.name != "election_data.csv":
        budget_process = False
    reader = csv.DictReader(csv_input)
    print(csv_input.name)
    for row in reader:
        lines.append(dict(row))
csv_input.close()

# set-up needed list for aggregating considering which process will be run
if not budget_process:
    voter_id_values = define_lists(lines, "Voter ID")
    candidate_values = define_lists(lines, "Candidate")
    total_votes = len(set(voter_id_values))
    unique_candidate = set(candidate_values)
else:
    date_values = define_lists(lines, "Date")
    profit_loss_values = define_lists(lines, "Profit/Losses")
    unique_months = set(date_values)
    total_revenue = sum(profit_loss_values)

""""""'''''''''''''''''''''''''''
Main test for Poll or Budget Routine
""""""'''''''''''''''''''''''''''''

if not budget_process:
    # Prep dictionary for sharper summary
    candidate_votes = dict()

    for name in unique_candidate:
        candidate_votes[name] = 0

    # assemble dictionary poll lists
    poll = zip(voter_id_values, candidate_values)
    # assemble dictionary poll listsassign votes to candidates
    for voter_id_, candidate in poll:
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1

    sort_by_votes = sorted(candidate_votes.values(), reverse=True)

    Winner = list(candidate_votes.keys())[list(candidate_votes.values()).index(sort_by_votes[0])]


    print("Election Results")

    print("_____________________________")

    print("Total Votes: " + str(total_votes))

    print("_____________________________")

    for key, value in candidate_votes.items():

        print(key + ": " + str(round(((value/total_votes)*100),2)) + "%  (" + str(value) + ")")

    print("_____________________________")

    print ("Winner : " + Winner)

    print("_____________________________")

    csv_path = os.path.join("election_data.csv")
    path = os.path.join("../PyPoll", "Poll_Result_.txt")

    with open(path, "w", newline='') as txtfile:

        txtfile.write("Election Results\n")

        txtfile.write("_____________________________\n")

        txtfile.write("Total Votes: " + str(total_votes) + "\n")

        txtfile.write("_____________________________\n")

        for key, value in candidate_votes.items():

            txtfile.write(key + ": " + str(round(((value/total_votes)*100),2)) + "%  (" + str(value) + ")\n")

        txtfile.write("_____________________________\n")

        txtfile.write("Winner : " + Winner + "\n")

        txtfile.write("_____________________________")

else:

    total_revenue = dict()

    for name in unique_months:
        unique_months = 0

    p_l_values = zip(date_values, profit_loss_values)

    for month_yy, money_val in p_l_values:
        if money_val in month_yy:
            unique_months += money_val

    sort_by_total_revenue = sorted(total_revenue.values(), reverse=True)

    Winner = list(date_values.keys())[list(date_values.values()).index(sort_by_total_revenue[0])]

    print("P&L Results")

    print("_____________________________")

    print("Total Revenue: " + str(total_revenue))

    print("_____________________________")

    for key, value in date_values.items():
        print(key + ": " + str(round(((value / total_revenue) * 100), 2)) + "%  (" + str(value) + ")")

    print("_____________________________")

    print("Winner : " + Winner)

    print("_____________________________")

    csv_path = os.path.join("budget_data.csv")
    path = os.path.join("../Pybank", "P&L_Result_.txt")

    with open(path, "w", newline='') as txtfile:

        txtfile.write("P&L Results\n")

        txtfile.write("_____________________________\n")

        txtfile.write("Total Revenue: " + str(total_revenue) + "\n")

        txtfile.write("_____________________________\n")

        for key, value in date_values.items():
            txtfile.write(key + ": " + str(round(((value / total_revenue) * 100), 2)) + "%  (" + str(value) + ")\n")

        txtfile.write("_____________________________\n")

        txtfile.write("Winner : " + Winner + "\n")

        txtfile.write("_____________________________")

