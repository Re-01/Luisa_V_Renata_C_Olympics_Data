import csv
import matplotlib.pyplot as plt
import numpy as np

category = []
usa = []
canada = []
norway = []


with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            category.append(row)
            line_count += 1
        elif row[4] == "USA":
            usa.append([int(row[0]), row[5], row[6], row[7]])
        elif row[4] == "CAN":
            canada.append([int(row[0]), row[5], row[6], row[7]])
            line_count += 1
        elif row[4] == "NOR":
            norway.append([int(row[0]), row[5], row[6], row[7]])
            line_count += 1

bronze_1924 = []
bronze_1928 = []
bronze_2014 = []


# Bronze medals in USA
for medal in usa:
    if medal[0] == 1924 and medal[3] == "Bronze":
        bronze_1924.append(medal)

    if medal[0] == 1928 and medal[3] == "Bronze":
        bronze_1928.append(medal)

    if medal[0] == 2014 and medal[3] == "Bronze":
        bronze_2014.append(medal)

# Bronze medals in Canada
for medal in canada:
    if medal[0] == 1924 and medal[3] == "Bronze":
        bronze_1924.append(medal)

    if medal[0] == 1928 and medal[3] == "Bronze":
        bronze_1928.append(medal)

    if medal[0] == 2014 and medal[3] == "Bronze":
        bronze_2014.append(medal)

# Bronze medals in Norway
for medal in norway:
    if medal[0] == 1924 and medal[3] == "Bronze":
        bronze_1924.append(medal)

    if medal[0] == 1928 and medal[3] == "Bronze":
        bronze_1928.append(medal)

    if medal[0] == 2014 and medal[3] == "Bronze":
        bronze_2014.append(medal)

print('Bronze medals in USA won from \'1924, 1928, and 2014', len(usa))
print('Bronze medals in Canada won from \'1924, 1928, and 2014', len(canada))
print('Bronze medals in Norway won from \'1924, 1928, and 2014', len(norway))

totalBronzeMedals = len(usa) + len(canada) + len(norway)

# percentages of three countries for bronze medals
usa_pertencage = int(len(usa)) / totalBronzeMedals * 100
canada_pertencage = int(len(canada)) / totalBronzeMedals * 100
norway_pertencage = int(len(norway)) / totalBronzeMedals * 100

print(usa_pertencage, canada_pertencage, norway_pertencage)

print('count', line_count, 'total bronze medals:', totalBronzeMedals)

#Pie Chart 
labels = "USA", "Canada", "Norway"
sizes = [176, 107, 127]
colors = ["rosybrown", "firebrick", "red"]
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("BRONZE MEDALS WON IN THREE COUNTRIES")
plt.xlabel("Bronze Medals from 1924, 1928, 2014")
plt.show()

# Horizontal bar chart
# Fixing random state for reproducibility
np.random.seed(19680801)

labels = "USA", "Canada", "Norway"
sizes = 159, 171, 127
colors = ["rosybrown", "firebrick", "red"]

plt.rcdefaults()
fig, ax = plt.subplots()

y_ind = np.arange(len(labels))
error = np.random.rand(len(labels))
ax.barh(y_ind, sizes, xerr=error, align='center', color=colors)
ax.set_yticks(y_ind)
ax.set_yticklabels(labels)
ax.invert_yaxis()
ax.set_xlabel("Total all medals")
ax.set_title("BRONZE WON IN THREE COUNTRIES FROM 1924, 1928, 2014")
plt.show()
