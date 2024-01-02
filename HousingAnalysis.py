'''
HousingAnalysis.py:
* Uses HouseData.txt to calculate a correlation matrix and eigen values to use for regression analysis
    and principal component analysis.
I) Open HouseData.txt and cleans unwanted syntax.
II) Centers all columns means to zero and t score standardizes all variables to handle unequal scale of variables.
    *Calculates and appends covariance and correlation to covariance and correlation matrices.
    *Handles naN by using least common N in calculations.
III) corr_pVal_matrix; new matrix with (r,pValue) for data cells
IV) Eigen Values of correlation matrix with dependent variable (Price) dropped.
* The corr_pVal_matrix and eigenvalues can be used to access the price regression model and perform prinicipal component analysis
    by analysing colinearity and eigenvalues.
'''
import pandas as pd
import matplotlib.pyplot as plt
import math as math
import statistics as stat
import numpy as np
from scipy import stats
import researchpy as rp
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy.stats import t
#I)
with open('C:/Users/rowec/OneDrive/Desktop/HouseData.txt', encoding="utf-8") as f:
    raw_data = pd.read_csv(f)
    pd.set_option('display.max_columns', None, "display.precision", 10)
    raw_data.columns = raw_data.columns.str.replace(' ', '')
    raw_data.columns = raw_data.columns.str.replace("'", '')
    raw_data.columns = raw_data.columns.str.replace("[", '')
    raw_data.columns = raw_data.columns.str.replace("]", '')
    raw_data = raw_data.drop(['Address', 'County', 'Pool'], axis=1)
    #II)
    num_cols = len(raw_data.keys())
    col_names = list(raw_data.keys())
    covariance_matrix = {}
    correlation_matrix = {}
    temp_col_array = []
    for i in range(0, num_cols):
        cov_list = []
        corr_list = []
        temp_col = raw_data[col_names[i]].dropna()
        temp_avg = sum(temp_col) / len(temp_col)
        temp_col = [x - temp_avg for x in temp_col]
        temp_list = []
        stdev = stat.stdev(temp_col, 0)
        for x in temp_col:
            t_score = x / stdev
            temp_list.append(t_score)
        temp_col_array.append(temp_list)
    temp_standardized_df = pd.DataFrame(temp_col_array)
    temp_standardized_df = temp_standardized_df.transpose()
    deg_free_list = []
    for i in range(0, num_cols):
        cov_list = []
        corr_list = []
        for j in range(0, num_cols):
            temp_col_1 = temp_standardized_df[i].dropna()
            n1 = len(temp_col_1)
            temp_col_2 = temp_standardized_df[j].dropna()
            n2 = len(temp_col_2)
            if (n1 <= n2):
                temp_col_1 = temp_col_1[0:n1]
                temp_col_2 = temp_col_2[0:n1]
                covariance = temp_col_1.cov(temp_col_2) / n1
                correlation = temp_col_1.corr(temp_col_2)
                deg_free_list.append(n1 - 2)
            else:
                temp_col_1 = temp_col_1[0:n2]
                temp_col_2 = temp_col_2[0:n2]
                covariance = temp_col_1.cov(temp_col_2) / n2
                correlation = temp_col_1.corr(temp_col_2)
                deg_free_list.append(n2 - 2)
            cov_list.append(covariance)
            corr_list.append(correlation)
        covariance_matrix[col_names[i]] = cov_list
        correlation_matrix[col_names[i]] = corr_list
    covariance_matrix = pd.DataFrame(covariance_matrix)
    correlation_matrix = pd.DataFrame(correlation_matrix)
    #III)
    corr_pVal_matrix = pd.DataFrame(columns=correlation_matrix.columns)
    corr_matrix_colnames = corr_pVal_matrix.keys().to_list()
    counter = 0
    temp_array = []
    temp_cell = ()
    for col in correlation_matrix:
        temp_list = []
        for r in (correlation_matrix[col]):
            deg_free = deg_free_list[counter]
            t_score = (r * math.sqrt(deg_free) / (0.000001 + math.sqrt(1 - r ** 2))) #add note about fisher transformation of r to z for p value calculations of r
            r = round(r, 4)
            p_val = t.sf(t_score, deg_free);
            p_val = round(p_val, 4)
            temp_cell = (r, p_val)
            temp_cell = (temp_cell)
            temp_list.append(temp_cell)
            counter += 1
        corr_pVal_matrix[col] = temp_list
    corr_pVal_matrix.index = corr_pVal_matrix.columns
    print(corr_pVal_matrix.to_string())
    #IV)
    independent_variables_correlation_matrix = correlation_matrix.drop(columns='Price')
    independent_variables_correlation_matrix = independent_variables_correlation_matrix.iloc[1:, :]
    independent_variables_correlation_matrix = pd.DataFrame(independent_variables_correlation_matrix)
    evalue, evect = np.linalg.eig(independent_variables_correlation_matrix)
    eigen_values = []
    for element in range(0, len(evalue)):
        eig_val = evalue[element]
        eig_val = round(eig_val, 4)
        eig_val = str(eig_val)
        eig_name = independent_variables_correlation_matrix.columns[element]
        eigen = eig_val, eig_name
        eigen = " ".join(eigen)
        eigen_values.append(eigen)
    print(eigen_values)







