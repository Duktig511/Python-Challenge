# access csv functions
import csv


def define_lists(line_data, field_name):
    field_values = []

    for count, item in enumerate(line_data):
        for count, key in enumerate(item.keys()):
            if key == field_name:
                field_val = item.get(field_name)
                field_values.append(field_val)
    return field_values


lines = []
poll_process = False

# open and assign csv file to string variable and read into output variable
with open("budget_data.csv", "r") as csv_input:
    if csv_input.name != "budget_data.csv":
        poll_process = True
    reader = csv.DictReader(csv_input)
    print(csv_input.name)
    for row in reader:
        lines.append(dict(row))
csv_input.close()

if not poll_process:
    date_values = define_lists(lines, "Date")
    profit_loss_values = define_lists(lines, "Profit/Losses")
else:
    voter_id_values = define_lists(lines, "Voter ID")
    candidate_values = define_lists(lines, "Candidate")
print(date_values[:40])
print(profit_loss_values[:40])