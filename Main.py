from datetime import date
import ageFiltered
today = date.today()
num_weeks = 5        # number of weeks to search through for
district_id = 149    # district id of gurgaon-188, south delhi-149,SE Del-144. SW-Del-150
select_age_flag = 0  # 1 for age based search,0 to search and return for both ages.
age= 45              # Enter your age
paid_necessary=0     # returns only paid centers if 1, returns unpaid as well if 0







'''
DON'T TOUCH IF YOU DON'T KNOW WHAT YOU'RE DOING
'''
age=ageFiltered.getAgeGroup(age)
ageFiltered.getPaid(select_age_flag,num_weeks,today,district_id,age)
if paid_necessary==0:
    ageFiltered.getUnpaid(select_age_flag,num_weeks,today,district_id,age)

