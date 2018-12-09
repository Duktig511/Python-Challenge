#access csv functions
import csv



months = []
revenue_change = []
lines = []
poll_process = False
j = 0

total_revenue = [0]

def define_lists(line_data,field_name):
   field_values = []
   for count, item in enumerate(line_data):
       for count, key in enumerate(item.keys()):
           if key == field_name:
               field_val = item.get(field_name)
               field_values.append(field_val)
   return  field_values


# open and assign csv file to string variable and read into output variable
with open("C:/Users/vasqu/PyCharmProjects/venv_conda/python_challenge/py_challenge_git/PyBank/budget_data.csv", "r") as csv_input:

    if csv_input.name != "budget_data.csv":
        poll_process = False
    reader = csv.DictReader(csv_input)
    for row in reader:
        lines.append(dict(row))
    csv_input.close()

date_values = define_lists(lines, "Date")
profit_loss_values = define_lists(lines, "Profit/Losses")
months = date_values
unique_months = set(months)
revenue = profit_loss_values
for item in revenue:
    j += 1
    total_revenue.append(revenue[sum([])])


for i in range(0, len(profit_loss_values) - 1):
    revenue_change.append(int(profit_loss_values[i + 1]) - int(profit_loss_values[i]))

avg_rev_change = sum(revenue_change) / len(revenue_change)

# find maximum and minimum revenue
max_revenue = max(profit_loss_values)
min_revenue = min(profit_loss_values)

# capture corresponding dates of max & min revenue
max_revenue_date = months[profit_loss_values.index(max_revenue)]
min_revenue_date = months[profit_loss_values.index(min_revenue)]


print(max_revenue)
print("Financial Analysis")

print("---------------------------")

print("Total Months: " + str(len(unique_months)))

print("Total Revenue: $" + str(total_revenue))

print("Average Revenue Change: $" + str(avg_rev_change))

print("Greatest Increase in Revenue: " + max_revenue_date + " ($" + str(max_revenue) + ")")

print("Greatest Decrease in Revenue: " + min_revenue_date + " ($" + str(min_revenue) + ")")