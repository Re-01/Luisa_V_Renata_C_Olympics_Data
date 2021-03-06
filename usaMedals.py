import csv
import matplotlib.pyplot as plt
import numpy as np

category = []
gold = []
silver = []
bronze = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            print('stripping out categories')
            category.append(row)
            line_count += 1

        else:
            if row[7] == "Gold":
                print('gold')
                gold.append(row[7])
            elif row[7] == "Silver":
                print('silver')
                silver.append(row[7])
            elif row[7] == "Bronze":
                bronze.append(row[7])
                line_count += 1

print(len(gold), 'gold medals have won since \'1924')
print(len(silver), 'silver medals have been won since \'1924')
print(len(bronze), 'bronze medals have been won since \'1924')

totalMedals = len(gold) + len(silver) + len(bronze)

# percentages of all medals
gold_pertencage = int(len(gold)) / totalMedals * 100
silver_pertencage = int(len(silver)) / totalMedals * 100
bronze_pertencage = int(len(bronze)) / totalMedals * 100

print(gold_pertencage, silver_pertencage, bronze_pertencage)

print('processed', line_count, 'lines of data. Total medals:', totalMedals)

# Pie Chart
labels = "Gold", "Silver", "Bronze"
sizes = [167, 319, 167]
colors = ["lightseagreen", "palegreen", "deepskyblue"]


plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("USA MEDALS HAVE WON")
plt.xlabel("Medals since 1924")
plt.show()

# Horizontal bar chart
# Fixing random state for reproducibility
np.random.seed(19680801)

labels = "Gold", "Silver", "Bronze"
sizes = 159, 171, 127
colors = ["lightseagreen", "palegreen", "deepskyblue"]

plt.rcdefaults()
fig, ax = plt.subplots()

y_ind = np.arange(len(labels))
error = np.random.rand(len(labels))
ax.barh(y_ind, sizes, xerr=error, align='center', color=colors)
ax.set_yticks(y_ind)
ax.set_yticklabels(labels)
ax.invert_yaxis()
ax.set_xlabel("Total medals")
ax.set_title("USA MEDALS HAVE WON SINCE 1924")
plt.show()
