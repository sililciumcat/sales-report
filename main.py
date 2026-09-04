from src.processor import SalesDataProcessor
from src.metrics import SalesMetrics
from src.reporter import ReportGenerator

# Загрузка данных
reading = SalesDataProcessor()
df = reading.load_all_csv()


# Инициализация метрик с передачей df
metrics = SalesMetrics(df)

# Инициализация создателя репортов
reports = ReportGenerator()

# Расчёт аналитики
total_revenue = metrics.get_total_revenue()
sales_by_cat = metrics.get_sales_by_category()
top_products = metrics.top_products()
reports.save_to_csv(sales_by_cat, "sales_by_category.csv")
reports.save_to_csv(top_products, "top_products.csv")

# Вывод результатов
print("=== Всего выручки ===")
print(total_revenue)
print("\n=== Продажи по категориям ===")
print(sales_by_cat)
print("\n=== Топ товаров ===")
print(top_products)
