import pandas as pd
import numpy as np

def clean_data(location,method="drop"):
# assigning the NA values for default values
    missingvalues=["NA","N/A","na","n/a"]
    df_raw = pd.read_csv(location,na_values=missingvalues,header=None, skiprows=1)
#   print the raw data after defaulting the na values
    print ('****RAW dataset****')
    print (df_raw)
#  converting all the data to float and cleaning any non numeric values
    df_raw=df_raw.replace('[^0-9]','',regex=True).astype(float)
#   print the data with only numeric values 
    print ('****Removing the non numeric characters****')
    print (df_raw)
# method called in if loop for drop or avg
    
    if method=="drop":
        df_method=df_raw.dropna(how='any')
        print("****Printing the values after filtering the NA****")
    elif method=="avg":
        df_method=df_raw.fillna(df_raw.mean())
        print("****Printing the values after filling the NA values with average of the column************")
    df_method=df_method.reset_index(drop=True)
    print (df_method)
    stds = 1.0
    lenloc=len(df_method.columns)
    print ('****Total Number of columns present in dataset:****')
    print (lenloc)
    if lenloc==1:
        df_method.columns=['Y']
        df_outliers=df_method
        print('****univariant********')
    elif lenloc==2:
        df_method.columns=['Y','X1']
        outliers = df_method[['X1']].transform(lambda group: (group - group.mean()).abs().div(group.std())) > stds  
        df_outliers=df_method[outliers.any(axis=1)]
        print('****One dependant valriable****')
    elif lenloc==3:
        df_method.columns=['Y','X1','X2']
        outliers = df_method[['X1','X2']].transform(lambda group: (group - group.mean()).abs().div(group.std())) > stds  
        df_outliers=df_method[outliers.any(axis=1)]
        print('****Two dependant valriable****')
    elif lenloc==4:
        df_method.columns=['Y','X1','X2','X3']
        outliers = df_method[['X1','X2','X3']].transform(lambda group: (group - group.mean()).abs().div(group.std())) > stds  
        df_outliers=df_method[outliers.any(axis=1)]
        print('****Three dependant valriable****')
    else:
        print('****Number of columns greater than three in data set****')
    #df_clean=df_outliers.merge(df_method,how='right', on=['Y','X1','X2'])
    #df_clean = df_method[df_outliers.X1 == False]
    df_clean=pd.concat([df_method,df_outliers]).drop_duplicates(keep=False)
    print ('****raw dataset********')
    print (df_method)
    print ('****outliers****')
    print (df_outliers)
    print ('****clean****')
    print (df_clean)
    return df_clean,df_outliers
