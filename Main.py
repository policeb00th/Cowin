import requests
import outputPrettifier
from datetime import date
import ageFiltered
today = date.today()
num_weeks = 5        # number of weeks to search through for
district_id = 188    # district id of gurgaon-188, south delhi-149,SE Del-144. SW-Del-150
select_age_flag = 1  # 0 for age based search,1 to search and retu for both ages.
age= 45              # 18 returns centers with available vaccines for 18-44 year olds, 45 returns centers with available vaccines for 45+ year olds
paid_necessary=0     # returns only paid centers if 1, returns unpaid as well if 0
ageFiltered.getPaid(select_age_flag,num_weeks,today,district_id,age)
if paid_necessary==0:
    ageFiltered.getUnpaid(select_age_flag,num_weeks,today,district_id,age)

