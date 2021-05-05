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
        finalval+=f"""------------------------Date: {date}-----------------------------------------\n
        
{tabulate(availableDates[date],headers=["Name","Vaccine type","slots","Age","Paid/Free"],tablefmt='html')}
        
---------------------------------------------------------------------------------\n"""
    return finalval
        

def prettyreturnByAge(availableDates):
    finalval=""
    for date in availableDates:
        finalval+=f"""------------------------Date: {date}-----------------------------------------\n
        
{tabulate(availableDates[date],headers=["Name","Vaccine type","slots","Paid/Free"],tablefmt='html')}
        
---------------------------------------------------------------------------------\n"""
    return finalval