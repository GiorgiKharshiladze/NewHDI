import pandas as pd

def getRank(series, country):
    df = pd.DataFrame({'country': series.index, 'value': series.values})
    
    df = df.sort_values(by='value', ascending=False).reset_index(drop=True)
    df['rank'] = df.index+1
    df = df.set_index('country')

    return df.loc[country, 'rank']

def getUNDP(file_name):
#     my_undp = {}
    df = pd.read_csv(file_name, index_col="Country")
    df = df.fillna(0)

    country_list = list(df.index)

    for country in country_list:
        my_undp[country] = {}
        for col in df.columns:
#             my_undp[country][int(col)] = getRank(df[col], country)
            df.loc[country, col] = getRank(df[col], country)
    
    return df
            
formated_df = getUNDP('undp.csv')

formated_df.to_csv('undp_formated.csv', encoding='utf-8')
    #         my_undp[country][col] = {}
    #         my_undp[country][col]['value'] = df[col][country]
    #         my_undp[country][col]['rank'] = getRank(df[col], country)