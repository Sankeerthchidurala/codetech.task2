import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import datetime

# Step 1: Generate sample data
def get_sample_data():
    data = {
        'Date': pd.date_range(start='2025-06-01', periods=7),
        'Sales': [1500, 1600, 1700, 1800, 2200, 2100, 2500]
    }
    df = pd.DataFrame(data)
    return df

# Step 2: Create a chart and save it
def create_chart(df):
    plt.figure(figsize=(6, 4))
    plt.plot(df['Date'], df['Sales'], marker='o', color='blue')
    plt.title('Weekly Sales Report')
    plt.xlabel('Date')
    plt.ylabel('Sales (in ₹)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("sales_chart.png")
    plt.close()

# Step 3: Generate PDF report
def generate_pdf(df):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Weekly Sales Report", ln=True, align='C')
    
    # Date
    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, f"Generated on: {datetime.date.today()}", ln=True, align='C')
    
    pdf.ln(10)

    # Table Header
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(40, 10, "Date", 1)
    pdf.cell(50, 10, "Sales (₹)", 1)
    pdf.ln()

    # Table Rows
    pdf.set_font("Arial", '', 12)
    for index, row in df.iterrows():
        pdf.cell(40, 10, row['Date'].strftime("%Y-%m-%d"), 1)
        pdf.cell(50, 10, str(row['Sales']), 1)
        pdf.ln()

    # Insert chart image
    pdf.ln(10)
    pdf.image("sales_chart.png", x=30, w=150)
    
    # Save PDF
    pdf.output("Weekly_Sales_Report.pdf")
    print("✅ Report generated: Weekly_Sales_Report.pdf")

# Run the app
if __name__ == "__main__":
    data = get_sample_data()
    create_chart(data)
    generate_pdf(data)
