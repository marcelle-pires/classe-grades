from src.handle_data import calculating_averages
from src.handle_data import list_students
import pandas as pd

def test_calculating_averages_correctly():
    df_test = pd.read_csv('test/data/test1.csv')
    df = calculating_averages(df_test)

    assert len(df.index) == 3
    assert len(df.columns) == 6

def test_list_students():
    df_test = pd.read_csv('test/data/test1.csv')
    df = list_students(df_test)

    assert df.iloc[0]['Name'] == 'Test1'
    assert df.iloc[1]['Name'] == 'Test2'
    assert df.iloc[2]['Name'] == 'Test3'
