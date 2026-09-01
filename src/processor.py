import csv
import pandas as pd
import openpyxl
from pathlib import Path

class SalesDataProcessor:
    """Sales data main processor"""

    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)

    def load_all_csv(self):
        """Load all of the CSVs"""

        csv_files = list(self.data_dir.glob("*.csv"))
        if not csv_files:
            raise FileNotFoundError("No files!")
        dfs = []

        for file in csv_files:
            dfs.append(pd.read_csv(file))

        df = pd.concat(dfs, ignore_index = True)

        data_frame = df.drop_duplicates()

        data_frame['total_amount'] = data_frame['quantity'] * data_frame['price']
        
        return data_frame
    