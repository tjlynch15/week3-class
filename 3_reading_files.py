import csv

# 1. Simplest approach

file = open("landmarks.csv")

reader = csv.reader(file)

for row in reader:
  if row:
    print(row[0], "is at", row[2])

file.close()



# 2. Automatically close the file
#
# with open("landmarks.csv") as file:
#   reader = csv.reader(file)
#   for row in reader:
#     if row:
#       print(row[0])




# 3. If the first line is a header row

with open("landmarks.csv") as file:
  reader = csv.reader(file)
  next(reader)  # skip the header line
  for row in reader:
    if row:
      print(row[0])
