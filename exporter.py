import csv


def save_to_file(DB):

    file = open("news.csv", mode="w")

    writer = csv.writer(file)

    writer.writerow(["News Title", "Press Name", "link"])

    for num in range(5):
      for db in DB[num]:
        writer.writerow(list(db.values()))

    return
