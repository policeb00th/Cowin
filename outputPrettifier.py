def prettyprint(availableDates):
    for date in availableDates:
        print(f"------------------------Date: {date}-----------------------------\n")
        print("Name \t \t \t Vaccine type \t \t Available vaccines\n")
        for centerDetails in availableDates[date]:
            print(f"{centerDetails[0]}\t \t{centerDetails[1]}\t \t{centerDetails[2]}")
        print(f"---------------------------------------------------------------------\n")