import csv
from pathlib import Path
import openpyxl
import pandas as pd


class SalesDataProcessor:
    """Sales data main processor"""

    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)

    def load_all_csv(self):
        """Load all of the CSVs"""

        csv_files = list(self.data_dir.glob("*.csv"))
        if not csv_files:
            raise FileNotFoundError(f"В директории '{self.data_dir}' не найдено ни одного CSV файла.")

        required_columns = {"price", "quantity", "category", "product"}
        dfs = []

        for file in csv_files:
            df = pd.read_csv(file)

            # Проверяем, все ли нужные колонки на месте
            if not required_columns.issubset(df.columns):
                missing = required_columns - set(df.columns)
                raise ValueError(
                    f"В файле {file.name} не хватает колонок: {missing}"
                )

            dfs.append(df)

        df = pd.concat(dfs, ignore_index=True)
        data_frame = df.drop_duplicates()
        data_frame["total_amount"] = (
            data_frame["quantity"] * data_frame["price"]
        )

        return data_frame