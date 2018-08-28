import pandas as pd
def list_to_csv(list_name, column_name,index = False):
    df = pd.DataFrame(list_name, column_name)
    csv_name = column_name + '.csv'
    df.to_csv(csv_name,index=index)
    return 0
def list_to_df(list_name,column_name):
    df = pd.DataFrame(list_name,columns=column_name)
    return df
