# Magic Data Cleanup
import pandas as pd
import numpy as np # used for np.where

def getUNDP(file_name):
    my_df = pd.read_csv(file_name, index_col="Country")
    my_df = my_df.fillna(0)
    
    for column in my_df:
        df = pd.DataFrame({'country': my_df[column].index, 'value': my_df[column].values})
        df = df.sort_values(by='value', ascending=False).reset_index(drop=True)
#         df['rank'] = df.index+1
        df['rank'] = np.where(df['value'], df.index+1, None)
        df = df.set_index('country')
        my_df[column] = df['rank']
        
    return my_df
            
formated_df = getUNDP('undp.csv')
formated_df.to_csv('undp_formated.csv', encoding='utf-8')
    #         my_undp[country][col] = {}
    #         my_undp[country][col]['value'] = df[col][country]
    #         my_undp[country][col]['rank'] = getRank(df[col], country)

