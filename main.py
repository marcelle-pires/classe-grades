import logging
import fire
from src.handle_csv import open_csv, write_to_csv
from src.handle_data import calculating_averages, list_students

logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)

def calculate_average(csv_name):
  df = open_csv(f'data/{csv_name}')
  logging.info("calculating average:")
  result = calculating_averages(df)

  csv_result_name = csv_name.replace(".csv", "_result.csv")
  result_path = f'data/result/{csv_result_name}'
  write_to_csv(result, result_path)

def listing_students(csv_name):
  logging.info("List of students")
  df = open_csv(f'data/{csv_name}')

  result = list_students(df)
  print(result)

if __name__ == '__main__':
  fire.Fire()