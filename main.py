from src.processor import SalesDataProcessor

reading = SalesDataProcessor()

df = reading.load_all_csv()

print(df)