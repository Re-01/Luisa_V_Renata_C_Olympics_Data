import csv
import matplotlib.pyplot as plt

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

gold_1924 = []
gold_1928 = []
gold_2014 = []


# Gold medals in USA
for medal in usa:
    if medal[0] == 1924 and medal[3] == "Gold":
        gold_1924.append(medal)

    if medal[0] == 1928 and medal[3] == "Gold":
        gold_1928.append(medal)

    if medal[0] == 2014 and medal[3] == "Gold":
        gold_2014.append(medal)

# Gold medals in Canada
for medal in canada:
    if medal[0] == 1924 and medal[3] == "Gold":
        gold_1924.append(medal)

    if medal[0] == 1928 and medal[3] == "Gold":
        gold_1928.append(medal)

    if medal[0] == 2014 and medal[3] == "Gold":
        gold_2014.append(medal)

# Gold medals in Norway
for medal in norway:
    if medal[0] == 1924 and medal[3] == "Gold":
        gold_1924.append(medal)

    if medal[0] == 1928 and medal[3] == "Gold":
        gold_1928.append(medal)

    if medal[0] == 2014 and medal[3] == "Gold":
        gold_2014.append(medal)

print('Gold medals in USA won from \'1924, 1928, and 2014', len(usa))
print('Gold medals in Canada won from \'1924, 1928, and 2014', len(canada))
print('Gold medals in Norway won from \'1924, 1928, and 2014', len(norway))

totalGoldMedals = len(usa) + len(canada) + len(norway)

# percentages of three countries for silver medals
usa_pertencage = int(len(usa)) / totalGoldMedals * 100
canada_pertencage = int(len(canada)) / totalGoldMedals * 100
norway_pertencage = int(len(norway)) / totalGoldMedals * 100

print(usa_pertencage, canada_pertencage, norway_pertencage)

print('count', line_count, 'total gold medals:', totalGoldMedals)

labels = "USA", "Canada", "Norway"
sizes = [167, 315, 159]
colors = ["gold", "yellow", "moccasin"]
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("GOLD MEDALS WON IN THREE COUNTRIES")
plt.xlabel("Gold Medals from 1924, 1928, 2014")
plt.show()
