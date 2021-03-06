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

print(len(gold), 'Gold medals have won since \'1924')
print(len(silver), 'Silver medals have been won since \'1924')
print(len(bronze), 'bronze medals have been won since \'1924')

totalMedals = len(gold) + len(silver) + len(bronze)

# percentages of all medals
gold_pertencage = int(len(gold)) / totalMedals * 100
silver_pertencage = int(len(silver)) / totalMedals * 100
bronze_pertencage = int(len(bronze)) / totalMedals * 100

print(gold_pertencage, silver_pertencage, bronze_pertencage)

print('count', line_count, 'Total all medals:', totalMedals)


# Pie Chart
labels = "Gold", "Silver", "Bronze"
sizes = [66, 147, 221]
colors = ["gold", "darkgray", "brown"]
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("FINLAND MEDALS HAVE WON")
plt.xlabel("Medals since 1924")
plt.show()

# Stacked Bar Graph
labels = "Gold", "Silver", "Bronze"
sizes = 66, 147, 221
ind = np.arange(len(labels))
colors = ["gold", "darkgray", "brown"]
width = 0.39

plt.bar(ind, sizes, color=colors)

plt.ylabel('Count of all medals')
plt.xticks(ind, labels)
plt.title("FINLAND MEDALS HAVE WON SINCE 1924")
plt.show()
