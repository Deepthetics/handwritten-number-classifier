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

  #print(len(df.index))
  #print(len(df.columns))
  #print(df.shape)
  for i in range(len(df.index)):
    for j in range(len(df.columns)):
      if df.iloc[i, j] > 127:
        df.iat[i, j] = 255
        print(i)
      else:
        df.iat[i, j] = 0
        print(i)

  return df
