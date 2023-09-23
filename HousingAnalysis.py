import pandas as pd
with open('C:/Users/Chris/Desktop/test.txt', encoding="utf-8") as f:
    # creating a data frame
    df = pd.read_csv(f)
    #print(df)
    pd.set_option('display.max_columns', None, "display.precision", 10)
    df.columns = df.columns.str.replace(' ','')
    df.columns = df.columns.str.replace("'",'')
    df.columns = df.columns.str.replace("[", '')
    df.columns = df.columns.str.replace("]", '')

    # Convert the dictionary into DataFrame
    # df = pd.DataFrame(data)

    # removed categoricals and it handles differences in N by not handling it and leaving it to you...
    df = df.drop(['Address', 'County', 'Pool'], axis=1)
    Cov_XX_fun = df['Price'].cov(df['Price'])

    print(df.count())
    '''
Price        250
Beds         250
Baths        250
Garage       184
Sqft         239
Lot_Sqft     125
Stories      207
YearBuilt    144
dtype: int64
#when calculating covariance use least N denominator and ignore unpaired samples and report sample
    #   size difference in sample size effect on accuracy of model
    
    '''

    #print(Cov_XX_fun)
    #print(Cov_XX_fun/df['Price'].count())
    #variance is fine cuz respective Ns but covariance maybe limit to limiting N for measurments with it for reduced
    #   significance but increased accruacy...better than just using avg N between them or something.

    '''
    Cause 1: Sample size imbalance
One possible cause of heterogeneity of covariance matrices is that the sample sizes of the groups are very different. 
For example, if you have 10 observations in one group and 100 in another, the smaller group may have more variability 
and less stability in its covariance matrix than the larger group. This can lead to unequal error terms and biased 
estimates of the group differences. To avoid this problem, you should try to balance the sample sizes of the groups as 
much as possible, or use a robust method of MANOVA that can handle unequal sample sizes, such as the Box's M test or 
the Pillai's trace criterion.
    '''

    '''

    # Convert the dictionary into DataFrame
    #df = pd.DataFrame(data)

    # Remove column name 'A'
    df = df.drop(['Address','County','Pool'], axis=1)
    Cov_XX_fun = df['Price'].cov(df['Price'])
    print(Cov_XX_fun)
    print(df['Price'].var())
    a = df['Price'].var() / df['Price'].count() -1
    print(a)
    print(df['Price'].count())
    print(len(df['Price']))
    

    #df = pd.DataFrame([(1, 2), (0, 3), (2, 0), (1, 1)],
                      #columns=['dogs', 'cats'])
    #print(df.cov())
    cov_matrix = df.cov()
    print(cov_matrix.to_string())
    #N changes ....
    cov_matrix = df.cov()/
    print(cov_matrix.to_string())
    #for x in df['Price']:
        #df['Price'] = df['Price'] - df['Price'].mean()
    #print(df.to_string())

    #for col in df.columns:
        #print(df[col]) #prints column
    #print(df.to_string()) #displays all rows
    #print(df.describe())
    '''
    '''
    print(df['Price'].mean())
    print(df['Price'].cov(df['Price']))
    print(sum(df['Price']))
    print(df['Price'].mean()*df['Price'].count())
    
    '''
    '''!!!
    the sum of a list of numbers is equal to the avg times the number.
    therefore, sum(df['Price'] == df['Price'].mean()*df['Price'].count()
    '''
    #print( sum(df['Price']) - df['Price'].mean()*df['Price'].count()   )
    #print(cov(df['Price'],df['Price']))
    #print((sum(df['Price'])-(df['Price'].mean()))**2)/(df['Price'.count()-1))
    #print(df.count())


    #print(type((df['Price'])))
    '''
    numerical_data = {'Price': [df['Price']],'Beds': [df['Beds']],
                      'Baths': [df['Baths']],'Garage': [df['Garage']],
                      'Sqft': [df['Sqft']], 'Stories': [df['Stories']],
                      'YearBuilt': [df['YearBuilt']]
            }
    
    dft = pd.DataFrame(numerical_data)

    #print(dft.to_string())
    cov_matrix = dft.cov()
    #print(cov_matrix)

    #df = pd.DataFrame(data)

    #print(df)
'''
#now use data for ML methods for portfolio
'''
Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s 
distribution, excluding NaN values. Therefore, NaN are already skipped over in calculations for description().
'''

#Covariance and Correlation Matrix
'''

import numpy as np
 
 
# x represents the total sale in
# dollars
x = [215, 325, 185, 332, 406, 522, 412,
     614, 544, 421, 445, 408],
 
# y represents the temperature on
# each day of sale
y = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1,
     19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
 
# create correlation matrix
matrix = np.corrcoef(x, y)
 
# print matrix
print(matrix)
'''
#Ordinary Least Squares (OLS) & Regression
'''
#Estimates the coefficients of a linear regression model by minimizing the sum of the squared differences between the 
    observed values of the dependent variable and the predicted values from the model.
#ELEMENTS OF A MULTIPLE REGRESSION EQUATION
    Y=a + b1X1 + b2X2 + b3X3
    Y is the value of the Dependent variable (Y), what is being predicted or explained
    a (Alpha) is the Constant or intercept
    b1 is the Slope (Beta coefficient) for X1
    X1 First independent variable that is explaining the variance in Y
    s.e.b1 standard error of coefficient b1
    R2 The proportion of the variance in the values of the dependent variable (Y) explained by all the independent variables (Xs) in the equation together; sometimes this is reported as adjusted R2, when a correction has been made to reflect the number of variables in the equation.
    F Whether the equation as a whole is statistically significant in explaining Y
    https://home.csulb.edu/~msaintg/ppa696/696regmx.htm
'''

'''
The Pandas .iterrows() function can be used to iterate over rows of the DataFram. It returns a tuple-based object, 
and each tuple consists of the index and the data of each row from the data frame. The .iterrows() method does not 
maintain data types.
'''


'''

# Import pandas package
import pandas as pd
  
# create a dictionary with five fields each
data = {
    'A': ['A1', 'A2', 'A3', 'A4', 'A5'],
    'B': ['B1', 'B2', 'B3', 'B4', 'B5'],
    'C': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'D': ['D1', 'D2', 'D3', 'D4', 'D5'],
    'E': ['E1', 'E2', 'E3', 'E4', 'E5']}
  
# Convert the dictionary into DataFrame
df = pd.DataFrame(data)
  
# Remove column name 'A'
df.drop(['A'], axis=1)
'''