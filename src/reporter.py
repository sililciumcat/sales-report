import os


class ReportGenerator:
    """Report Generator"""

    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def save_to_csv(self, data, filename="report.csv"):
        filepath = os.path.join(self.output_dir, filename)
        data.to_csv(filepath)
        print(f"The report saved: {filepath}")

    def save_summary(self, total_revenue, sales_by_cat, top_products, filename="summary.txt"):
        """Формирование и сохранение текстовой сводки"""
        filepath = os.path.join(self.output_dir, filename)
        
        top_product_name = top_products.index[0] if not top_products.empty else "N/A"
        top_product_qty = top_products.iloc[0] if not top_products.empty else 0
        
        top_cat_name = sales_by_cat.index[0] if not sales_by_cat.empty else "N/A"
        top_cat_revenue = sales_by_cat.iloc[0] if not sales_by_cat.empty else 0

        summary_content = (
            "========================================\n"
            "         ИТОГОВЫЙ СВОДНЫЙ ОТЧЕТ          \n"
            "========================================\n\n"
            f"Общая выручка: ${total_revenue:,.2f}\n\n"
            "--- Лидер продаж по количеству ---\n"
            f"Товар: {top_product_name} ({top_product_qty} шт.)\n\n"
            "--- Топовая категория по выручке ---\n"
            f"Категория: {top_cat_name} (${top_cat_revenue:,.2f})\n\n"
            "========================================\n"
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(summary_content)

        print(f"The summary report saved: {filepath}")