import numpy as np
import pandas as pd

laptops = pd.read_csv("Datasets/laptops_with_photo_url.csv")
laptops.reset_index(inplace=True)
laptops.drop(["Unnamed: 0", "index"], axis=1, inplace=True)

user_data= pd.read_csv("Datasets/user_companies_data.csv", index_col="company_id")

#column_names_old = ["company_id","company_name", "location", "company_type","laptop_id"]
column_names = ["company_id", "laptop_id"]
##
#school_laptops = pd.read_csv("school_laptops.csv")
#hospital_laptops = pd.read_csv("hospital_laptops.csv")

#schools = user_data[user_data["company_type"] == "Education"]
#schools.to_csv("schools_users.csv",index=True)
#
#hospitals = user_data[user_data["company_type"] == "HealthCare"]
#hospitals.to_csv("hospitals_users.csv",index=True)
#
#stores = user_data[user_data["company_type"] == "RetailStores"]
#stores.to_csv("stores_users.csv",index=True)
#
#banks = user_data[user_data["company_type"] == "Bank"]
#banks.to_csv("banks_users.csv",index=True)
#

#schools = pd.read_csv("schools_users.csv")
#stores = pd.read_csv("stores_users.csv")
#
#hospitals = pd.read_csv("hospitals_users.csv")
#banks = pd.read_csv("banks_users.csv")

#schools.drop(["primary_color", "secondary_colour"], axis=1, inplace=True)
#stores.drop(["primary_color", "secondary_colour"], axis=1, inplace=True)
#hospitals.drop(["primary_color", "secondary_colour"], axis=1, inplace=True)
#banks.drop(["primary_color", "secondary_colour"], axis=1, inplace=True)        

#school_orders = pd.DataFrame(columns=column_names)
#for company_id in range(200, 300):
#    for counter in range(5):
#        laptop_id = np.random.choice(school_laptops["Laptop_ID"],1)
#        df = pd.DataFrame({"company_id" : company_id, "laptop_id" : laptop_id[0]}, index=range(1))
#        school_orders = pd.concat([school_orders, df], ignore_index=True, axis=0)
      
school_orders = pd.DataFrame(columns=column_names)
school_laptops = pd.read_csv("Datasets/school_laptops.csv")

for company_id in range(200, 300):
    for counter in range(5):
        laptop_id = np.random.choice(school_laptops["Laptop_id"],1)
        df = pd.DataFrame({"company_id" : company_id, "laptop_id" : laptop_id[0]}, index=range(1))
        school_orders = pd.concat([school_orders, df], ignore_index=True, axis=0)

#school_orders.to_csv("school_orders.csv",index=False)
school_orders.to_csv("school_orders.csv",index=False)

school_orders = pd.read_csv("school_orders.csv")
hospital_orders = pd.read_csv("hospital_orders.csv")



