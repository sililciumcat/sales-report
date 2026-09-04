import os
class ReportGenerator:
    """Report Generator"""

    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def save_to_csv(self, data, filename="report.csv"):
        filepath = os.path.join(self.output_dir, filename)
        data.to_csv(filepath)
        print(f'The report saved: {filepath}')