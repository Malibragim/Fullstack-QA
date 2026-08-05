
from os import startfile
import pandas as pd

def test_primary_clear_data_in_excel():
 df = pd.read_excel("C:/Users/LENOVO/Downloads/7 academic_performance_dataset_V2.xlsx")
 if df.isna().any().any():
     clean_df = df.dropna()
     clean_df.to_excel(
         "C:/Users/LENOVO/Downloads/7 academic_performance_dataset_V2.xlsx",
         index=False
     )
     startfile("C:/Users/LENOVO/Downloads/7 academic_performance_dataset_V2.xlsx")
 else:
     print("Пропущенные значения в данных отсутствуют.")








