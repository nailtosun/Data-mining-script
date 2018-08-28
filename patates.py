import pandas as pd
def list_to_dataframe(list_name):
    for i in range (len(list_name)):
        df = pd.DataFrame()
        df.append(list_name[i])
    return pd
deneme = [1,2,3]
y = list_to_dataframe(deneme)
deneme[0]
df1 = pd.DataFrame()
type(df1)
df1.append(deneme[0])
