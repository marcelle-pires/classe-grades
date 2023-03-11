from src.handle_csv import open_csv
from src.handle_csv import write_to_csv
import os

def test_open_csv():
    df = open_csv('test/data/test1.csv')

    assert len(df.index) == 3
    assert len(df.columns) == 5

def test_write_to_csv():
    df = open_csv('test/data/test1.csv')
    path_result = 'test/data/test1_result.csv'
    write_to_csv(df, path_result)

    fileExist = os.path.exists(path_result)
    assert fileExist == True

    df_result = open_csv('test/data/test1_result.csv')
    
    assert len(df_result.index) == 3
    assert len(df_result.columns) == 6

    os.remove('test/data/test1_result.csv')
