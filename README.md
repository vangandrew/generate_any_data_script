# Fake Healthcare Data Generator

This Python script generates randomized fake healthcare data for analytics and testing purposes. It can create large sample datasets of realistic-looking healthcare records.

Overview
The script uses the Faker library to generate fake data for fields like patient names, IDs, demographics, visit dates, and medical data.

It outputs the fake data to an Excel file, with columns for each field. The user can configure the number of rows to generate.

Usage
The main dependencies are:

- Faker
- OpenPyXL

## Contents
The generated Excel file will contain columns for:

Date
Patient ID
Patient Gender
Patient Age
Test Score
Patient Initial
Patient Last Name
Patient Race
Admin Flag
Wait Time
Referral Department
All data is randomly generated and not based on real records.


## Benefits
- Allows generating large sample datasets for analytics, dashboards, and machine learning
- Data scientists can use for model training and testing
- Healthcare companies can use for app testing and staging environments
- Protects patient privacy since all data is fake
