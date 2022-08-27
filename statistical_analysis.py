#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: August
"""
#Import NumPy Package
import numpy as np
import pandas as pd
# Load insurance.txt data set as "insurance" 
insurance = np.loadtxt("C:/Users/augus/Documents/MATH 6380/Homeworks/HW-5/insurance.txt",\
                       dtype = {'names':('age','sex','bmi','children',\
                                         'smoker','region','expenses'),\
                                'formats':[float,'S100',float,float,\
                                           'S100','S100',float]},skiprows=1)
 # Extract the seven explanatory features   
age = insurance['age']
sex = insurance['sex']
bmi = insurance['bmi']
children = insurance['children']
smoker = insurance['smoker']
region = insurance['region']
expenses = insurance['expenses']

# 1. Mean, median, and std of age
age_mean = np.mean(age)
age_median = np.median(age)
age_std = np.std(age) 

# 2. Mean, median, and std of bmi
bmi_mean = np.mean(bmi)
bmi_median = np.median(bmi)
bmi_std = np.std(bmi) 

# Using Pandas to put insurance data into a dataframe
insu = pd.DataFrame(insurance)
    
# 3. Mean, median, and std of bmi grouped by sex  
bmi_mean_sx = insu[['bmi','sex']].groupby('sex').mean()
bmi_median_sx = insu[['bmi','sex']].groupby('sex').median()
bmi_std_sx = insu[['bmi','sex']].groupby('sex').std()

# 4. Mean, median, and std of bmi grouped by smoker type  
bmi_mean_sm = insu[['bmi','smoker']].groupby('smoker').mean()
bmi_median_sm = insu[['bmi','smoker']].groupby('smoker').median()
bmi_std_sm = insu[['bmi','smoker']].groupby('smoker').std()

# 5. Mean, median, and std of bmi grouped by region  
bmi_mean_r = insu[['bmi','region']].groupby('region').mean()
bmi_median_r = insu[['bmi','region']].groupby('region').median()
bmi_std_r = insu[['bmi','region']].groupby('region').std()

# Filtering dataframe to obtain only entries with more than 2 children
insu_ch2 = insu[insu['children']>2]

# 6. Mean, median, and std of bmi for people with more than 2 children 
bmi_mean_c = insu_ch2[['bmi','children']].groupby('children').mean()
bmi_median_c = insu_ch2[['bmi','children']].groupby('children').median()
bmi_std_c = insu_ch2[['bmi','children']].groupby('children').std()

#  Sort Data by "expenses" and obtain the top 20% of entries and the bottom 80%
insu_sort_ex = insu.sort_values(by='expenses')
top_20p_ent = int(0.2*(len(insu))) + 1
bot_80p_ent = int(0.8*(len(insu)))
insu_ex_top_20 = insu_sort_ex.nlargest(top_20p_ent,'expenses')
insu_ex_bot_80 = insu_sort_ex.nsmallest(bot_80p_ent,'expenses')

# Mean and std of bmi for top 20% and bottom 80%
bmi_mean_20 = insu_ex_top_20['bmi'].mean()
bmi_std_20 = insu_ex_top_20['bmi'].std()

bmi_mean_80 = insu_ex_bot_80['bmi'].mean()
bmi_std_80 = insu_ex_bot_80['bmi'].std()


# Mode of smokers and region for 20% and bottom 80%
smoker_mode_20 = insu_ex_top_20['smoker'].mode()
smoker_mode_80 = insu_ex_bot_80['smoker'].mode()

region_mode_20 = insu_ex_top_20['region'].mode()
region_mode_80 = insu_ex_bot_80['region'].mode()

# Create array to save results
Results = np.array([age_mean, age_median, age_std,
                    bmi_mean, bmi_median, bmi_std,
                    bmi_mean_sx, bmi_median_sx, bmi_std_sx,
                    bmi_mean_sm, bmi_median_sm, bmi_std_sm,
                    bmi_mean_r, bmi_median_r, bmi_std_r,
                    bmi_mean_c, bmi_median_c, bmi_std_c,
                    bmi_mean_20, bmi_std_20,
                    bmi_mean_80, bmi_std_80,
                    smoker_mode_20, smoker_mode_80,
                    region_mode_20, region_mode_80])


np.savetxt("HW5_P1_TEAM16.txt",Results,fmt='%s')


    
