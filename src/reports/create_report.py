import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def _build_quality_dataframe(df: pd.DataFrame) -> tuple:

    total_rows = len(df)

    missing_values = df.isnull().sum()
    missing_percent = (missing_values / total_rows) * 100
    data_types = df.dtypes.astype(str)

    duplicated_count = df.duplicated().sum()
    duplicated_percent = (duplicated_count / total_rows) * 100

    summary_df = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": missing_values.values,
        "Missing Values (%)": missing_percent.values.round(2),
        "Data Type": data_types.values
    })

    return summary_df, total_rows, duplicated_count, duplicated_percent


# 
def generate_excel_report(df: pd.DataFrame, output_path: str = "data_quality_report.xlsx"):
    summary_df, total_rows, duplicated_count, duplicated_percent = _build_quality_dataframe(df)

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        summary_df.to_excel(writer, sheet_name="Data Quality", index=False)

        metrics_df = pd.DataFrame({
            "Metric": [
                "Total Rows",
                "Duplicated Rows",
                "Duplicated Rows (%)"
            ],
            "Value": [
                total_rows,
                duplicated_count,
                round(duplicated_percent, 2)
            ]
        })

        metrics_df.to_excel(writer, sheet_name="General Metrics", index=False)

    print(f"Excel report generated at: {output_path}")



def generate_pdf_report(df: pd.DataFrame, output_path: str = "data_quality_report.pdf"):
    summary_df, total_rows, duplicated_count, duplicated_percent = _build_quality_dataframe(df)

    doc = SimpleDocTemplate(output_path)
    elements = []

    styles = getSampleStyleSheet()

    elements.append(Paragraph("Report Data Quality", styles["Heading1"]))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"Total of rows: {total_rows}", styles["Normal"]))
    elements.append(Paragraph(
        f"Duplicated rows: {duplicated_count} ({duplicated_percent:.2f}%)",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 0.3 * inch))

    table_data = [summary_df.columns.tolist()] + summary_df.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    elements.append(table)

    doc.build(elements)

    print(f"PDF report generated at: {output_path}")