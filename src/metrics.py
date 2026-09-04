import argparse
import pandas as pd

class SalesMetrics:
    """class of Sales Metrics"""
    
    def __init__(self, df):
        self.df = df

    def get_total_revenue(self):
        """Getting total revenue"""

        return self.df["total_amount"].sum()

    def get_sales_by_category(self):
        """total revanue of the category"""

        return self.df.groupby("category")["total_amount"].sum()

    def top_products(self, n=5):
        return (
            self.df.groupby("product")["quantity"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )
