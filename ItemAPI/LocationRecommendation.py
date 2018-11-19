# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:41:19 2018

@author: Abhishek
"""

import pandas as pd
import numpy as np

def get_school_recommendations(test_indices):    
    school_laptops = pd.read_csv("Datasets/school_laptops.csv", index_col="Laptop_id") 
    laptops = pd.read_csv('Datasets/laptops_with_photo_url.csv')
    laptops.reset_index()
    photos = laptops['photo_url']
    counter = 0
    indi_dicts = []
    for index in test_indices:
        counter += 1
        indi_dicts.append({'Company':school_laptops['Company'][index],
                               'Product':school_laptops['Product'][index],
                               'Price_euros':school_laptops['Price_euros'][index],
                               'Cpu':school_laptops['Cpu'][index],
                               'Gpu':school_laptops['Gpu'][index],
                                'Memory':school_laptops['Memory'][index],
                                'photo_url':photos[counter]})
        
    final_dict = {'count':len(indi_dicts), 'results':indi_dicts}
    return final_dict

def get_hospital_recommendations(test_indices):    
    hospital_laptops = pd.read_csv("Datasets/hospital_laptops.csv", index_col="Laptop_id") 
    laptops = pd.read_csv('Datasets/laptops_with_photo_url.csv')
    laptops.reset_index()
    photos = laptops['photo_url']
    counter = 0
    indi_dicts = []
    for index in test_indices:
        counter += 1
        indi_dicts.append({'Company':hospital_laptops['Company'][index],
                               'Product':hospital_laptops['Product'][index],
                               'Price_euros':hospital_laptops['Price_euros'][index],
                               'Cpu':hospital_laptops['Cpu'][index],
                               'Gpu':hospital_laptops['Gpu'][index],
                                'Memory':hospital_laptops['Memory'][index],
                                'photo_url':photos[counter]})
        
    final_dict = {'count':len(indi_dicts), 'results':indi_dicts}
    return final_dict

def location_similarity(location, company_type):
    laptops = []
    if(company_type == "Education"):
        schools = pd.read_csv("Datasets/schools_users.csv",index_col="company_id")
        school_orders = pd.read_csv("Datasets/school_orders.csv") 
        groups = schools.groupby("location").groups
        company_ids = groups[location]
        
        for company in company_ids:
            df = school_orders[school_orders["company_id"]==company]
            for laptop in df["laptop_id"].values:
                laptops.append(laptop)
              
        laptops = set(laptops)
        laptops = list(laptops)    
        return get_school_recommendations(laptops)
     
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
    
        laptops = set(laptops)
        laptops = list(laptops)    
        return get_hospital_recommendations(laptops)
