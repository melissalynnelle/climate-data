import csv


class DailyDischarge:
    def __init__(self) -> None:
        self.data = []

        with open("data/Daily_Discharge.csv") as file:
            reader = csv.DictReader(file)

            for row in reader:
                self.data.append(row)


if __name__ == "__main__":
    daily_discharge = DailyDischarge()
    print(daily_discharge.data)
