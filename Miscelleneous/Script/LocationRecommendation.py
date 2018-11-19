# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:41:19 2018

@author: Abhishek
"""

import pandas as pd
import numpy as np

def get_recommendations(test_indices):
        
    laptops = pd.read_csv('Datasets/laptops_with_photo_url.csv')
    indi_dicts = []
    for i in range(len(test_indices)):
        indi_dicts.append({'Company':laptops['Company'][i],
                               'Product':laptops['Product'][i],
                               'Price_euros':laptops['Price_euros'][i]})
        
    final_dict = {'count':len(indi_dicts), 'results':indi_dicts}

    return final_dict

def location_similarity(location, company_type):
    laptops = []
    if(company_type == "Education"):
        schools = pd.read_csv("Datasets/schools_users.csv",index_col="company_id")
        school_orders = pd.read_csv("Datasets/school_orders.csv") 
        groups = schools.groupby("location").groups
#        print(schools.groupby("location").count())
#        print(groups)
        company_ids = groups[location]
        
        for company in company_ids:
            df = school_orders[school_orders["company_id"]==company]
            for laptop in df["laptop_id"].values:
                laptops.append(laptop)
                
    elif(company_type == "Healthcare"):
        hospitals = pd.read_csv("Datasets/hospitals_users.csv",index_col="company_id")
        hospital_orders = pd.read_csv("Datasets/hospital_orders.csv")
        groups = hospitals.groupby("location").groups
        print(hospitals.groupby("location").count())
        company_ids = groups[location]
        
        for company in company_ids:
            df = hospital_orders[hospital_orders["company_id"]==company]
            for laptop in df["laptop_id"].values:
                laptops.append(laptop)
        
    return get_recommendations(laptops)

location_similarity("PA|Panama","Education")