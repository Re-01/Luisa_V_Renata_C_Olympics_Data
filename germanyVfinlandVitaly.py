import csv
import matplotlib.pyplot as plt

category = []
germany = []
finland = []
italy = []


with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            category.append(row)
            line_count += 1
        elif row[4] == "GER":
            germany.append([int(row[0]), row[5], row[6], row[7]])
        elif row[4] == "FIN":
            finland.append([int(row[0]), row[5], row[6], row[7]])
            line_count += 1
        elif row[4] == "ITA":
            italy.append([int(row[0]), row[5], row[6], row[7]])
            line_count += 1

silver_1924 = []
silver_1948 = []
silver_1972 = []


# Silver medals in Germany
for medal in germany:
    if medal[0] == 1924 and medal[3] == "Silver":
        silver_1924.append(medal)

    if medal[0] == 1948 and medal[3] == "Silver":
        silver_1948.append(medal)

    if medal[0] == 1972 and medal[3] == "Silver":
        silver_1972.append(medal)

# Silver medals in Finland
for medal in finland:
    if medal[0] == 1924 and medal[3] == "Silver":
        silver_1924.append(medal)

    if medal[0] == 1948 and medal[3] == "Silver":
        silver_1948.append(medal)

    if medal[0] == 1972 and medal[3] == "Silver":
        silver_1972.append(medal)

# Silver medals in Italy
for medal in italy:
    if medal[0] == 1924 and medal[3] == "Silver":
        silver_1924.append(medal)

    if medal[0] == 1948 and medal[3] == "Silver":
        silver_1948.append(medal)

    if medal[0] == 1972 and medal[3] == "Silver":
        silver_1972.append(medal)

print('Silver medals in Germany won from \'1924 to 1972', len(germany))
print('Silver medals in Finland has won since \'1924 to 1972', len(finland))
print('Silver medals in Italy won in \'1924 to 1972', len(italy))


totalSilverMedals = len(germany) + len(finland) + len(italy)

# percentages of three countries for silver medals
germany_pertencage = int(len(germany)) / totalSilverMedals * 100
finland_pertencage = int(len(finland)) / totalSilverMedals * 100
italy_pertencage = int(len(italy)) / totalSilverMedals * 100

print(germany_pertencage, finland_pertencage, italy_pertencage)

print('count', line_count, 'total silver medals:', totalSilverMedals)

labels = "Germany", "Finland", "Italy"
sizes = [germany_pertencage, finland_pertencage, italy_pertencage]
colors = ["dimgrey", "darkgrey", "gainsboro"]
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("SILVER MEDALS WON IN THREE COUNTRIES")
plt.xlabel("Silver Medals from 1924, 1948, and 1972")
plt.show()
