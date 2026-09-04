from src.processor import SalesDataProcessor
from src.metrics import SalesMetrics

# 1. Загрузка данных
reading = SalesDataProcessor()
df = reading.load_all_csv()

# 2. Инициализация метрик с передачей df
metrics = SalesMetrics(df)

# 3. Расчёт аналитики
total_revenue = metrics.get_total_revenue()
sales_by_cat = metrics.get_sales_by_category()
top_products = metrics.top_products()

# 4. Вывод результатов
print("=== Всего выручки ===")
print(total_revenue)
print("\n=== Продажи по категориям ===")
print(sales_by_cat)
print("\n=== Топ товаров ===")
print(top_products)