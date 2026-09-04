import argparse
from src.processor import SalesDataProcessor
from src.metrics import SalesMetrics
from src.reporter import ReportGenerator


def parse_args():
    """Парсинг аргументов командной строки"""
    parser = argparse.ArgumentParser(
        description="Обработка и анализ отчётов по продажам"
    )

    parser.add_argument(
        "--data_dir",
        type=str,
        default="data",
        help="Путь к папке с CSV файлами",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="reports",
        help="Путь для сохранения готовых отчётов",
    )

    return parser.parse_args()


if __name__ == "__main__":
    # 1. Получаем аргументы из терминала
    args = parse_args()

    # 2. Загружаем данные
    reading = SalesDataProcessor(data_dir=args.data_dir)
    df = reading.load_all_csv()

    # 3. Считаем метрики
    metrics = SalesMetrics(df)
    total_revenue = metrics.get_total_revenue()
    sales_by_cat = metrics.get_sales_by_category()
    top_products = metrics.top_products()

    # 4. Сохраняем отчёты
    reports = ReportGenerator(output_dir=args.output_dir)
    reports.save_to_csv(sales_by_cat, "sales_by_category.csv")
    reports.save_to_csv(top_products, "top_products.csv")

    # 5. Вывод результатов в консоль
    print("=== Всего выручки ===")
    print(total_revenue)
    print("\n=== Продажи по категориям ===")
    print(sales_by_cat)
    print("\n=== Топ товаров ===")
    print(top_products)