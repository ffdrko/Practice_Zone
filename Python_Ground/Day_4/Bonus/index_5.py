filenames = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentation.txt")

for file in filenames:
    file = file.replace(".", "-")
    print(file)

for file in filenames:
    file = file.replace(".", "-", 1)
    print(file)