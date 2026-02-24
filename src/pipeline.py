import pandas as pd
from connection.create_data_set import create_dataframe
import reports.create_report as report


def run_pipeline():
    
    df_customers = create_dataframe("customers")
    df_orders = create_dataframe("orders")
    df_products = create_dataframe("products")
    df_payments = create_dataframe("payments")
    
    df_customers.columns = ["customer_id","full_name","email","phone","birth_date","city","created_at"]
    df_orders.columns = ["order_id","customer_id","order_date","total_amount","status"]
    df_payments.columns = ["payment_id","order_id","payment_method","paid_amount","paid_at"]
    df_products.columns = ["product_id","product_name","category","price"]
    
    
    report.generate_excel_report(df_customers, output_path="customers_data_quality_report.xlsx")
    report.generate_pdf_report(df_customers, output_path="customers_data_quality_report.pdf")   
    
    
    
    
    
if __name__ == "__main__":
    run_pipeline()