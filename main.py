import openpyxl
from faker import Faker 
import random

fake = Faker()

wb = openpyxl.Workbook()
sheet = wb.active

headers = ['date', 'patient_id', 'patient_gender', 'patient_age', 
           'patient_sat_score', 'patient_first_inital', 'patient_last_name',
           'patient_race', 'patient_admin_flag', 'patient_waittime', 
           'department_referral']

sheet.append(headers)

for i in range(300000):

    date = fake.date_between(start_date='today', end_date='+30d')

    patient_id = fake.ssn()

    patient_gender = random.choice(['M', 'F'])

    patient_age = random.randint(0, 100)

    patient_sat_score = random.randint(0, 10)

    patient_first_inital = fake.random_element(elements=[
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ])

    patient_last_name = fake.last_name()

    patient_race = random.choice([
        'White', 'African American', 'Native American/Alaska Native',
        'Asian', 'Native Hawaiian/Pacific Islander'
    ]) 

    patient_admin_flag = random.choice([True, False])

    patient_waittime = random.randint(0, 60)

    department_referral = random.choice([
        'General Practice', 'Cardiology', 'Dermatology',
        'Neurology', 'Oncology', 'None'
    ])

    row = [date, patient_id, patient_gender, patient_age, 
           patient_sat_score, patient_first_inital, patient_last_name,
           patient_race, patient_admin_flag, patient_waittime, 
           department_referral]

    sheet.append(row)

wb.save('healthcare_data2.xlsx')