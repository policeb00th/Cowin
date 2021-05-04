def prettyprint(availableDates):
    for date in availableDates:
        print(f"\t------------------------Date: {date}-----------------------------\n")
        print("\tName \t \t \t Vaccine type \t \t Available vaccines\n")
        for centerDetails in availableDates[date]:
            print(f"\t{centerDetails[0]}\t \t{centerDetails[1]}\t \t{centerDetails[2]}")
        print(f"\t---------------------------------------------------------------------\n")