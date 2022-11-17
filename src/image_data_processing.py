import pandas as pd


def extract(df):
  """Purkaa MNIST-datasta kuvat ja niitä vastaavat luokat erilleen.

  Args:
    df: pandas.DataFrame-luokan olio.

  Returns:
    dataframe: pandas.Dataframe-luokan olio
  """

  images = df.iloc[:,1:]
  labels = df.iloc[:,0]
  return (images, labels)

def to_binary(df):
  """Muuntaa MNIST-datan sisältämät harmaaväriskaalaiset kuvat binääreiksi mustavalkoisiksi kuviksi.

  Args:
    df: pandas.DataFrame-luokan olio, joka sisältää harmaaväriskaalaiset kuvat.

  Returns:
    dataframe: pandas.Dataframe-luokan olio, joka sisältää binäärit mustavalkoiset kuvat.
  """

  row_count = len(df.index)
  column_count = len(df.columns)
  
  for i in range(row_count):
    for j in range(column_count):
      if df.iloc[i, j] > 127:
        df.iat[i, j] = 1
        print(f'Row: {i}')
      else:
        df.iat[i, j] = 0
        print(f'Row: {i}')

  return df
