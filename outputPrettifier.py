from tabulate import tabulate
def prettyprint(availableDates):
    for date in availableDates:
        print(f"------------------------Date: {date}-----------------------------\n")
        print("Name \t \t \t Vaccine type \t \t Available vaccines\n")
        print(tabulate(availableDates[date]))
        print(f"---------------------------------------------------------------------\n")
        


def prettyreturnAllAge(availableDates):
    finalval=""
    for date in availableDates:
        finalval+=f"""{tabulate(availableDates[date],headers=["Name","Address","Vaccine type","slots","Age","Paid/Free","date"],tablefmt='html')}\n"""
    return finalval
        

def prettyreturnByAge(availableDates):
    finalval=""
    for date in availableDates:
        finalval+=f"""{tabulate(availableDates[date],headers=["Name","Address","Vaccine type","slots","Paid/Free","date"],tablefmt='html')}\n"""
    return finalval