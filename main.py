import csv

def main():
    with open('data.csv') as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))

        print(", ".join(csv_reader[0]))
        print(", ". join(csv_reader[1]))

if __name__ == "__main__":
    main()