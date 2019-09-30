def df_summary(df):
  df_U = df.nunique()
  df_M = df.isnull().sum()
  df_I = df.dtypes
  df_Summary = df.describe(include = 'all').transpose()
  df_U = df_U.to_frame().reset_index()
  df_M = df_M.to_frame().reset_index()
  df_I = df_I.to_frame().reset_index()
  df_Summary = df_Summary.reset_index()
  df_U = df_U.rename(columns= {0: 'Unique Data'})
  df_M = df_M.rename(columns= {0: 'Missing Data'})
  df_I = df_I.rename(columns= {0: 'Data Types'})
  #output = pd.merge(pd.merge(df_M,df_U,on='index'),df_I,on='index')
  output = pd.merge(pd.merge(pd.merge(df_M,df_U,on='index'),df_I,on='index'),df_Summary,on = 'index')
  return output;
