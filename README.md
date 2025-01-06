## **AI Sales Insights Dashboard**

A simple AI-powered dashboard to provide actionable sales insights for e-commerce businesses.

This project demonstrates how to analyze sales data and visualize trends using Python. It provides actionable insights for e-commerce businesses through:
- A script that generates a **monthly sales trend plot**.
- A summary of **top products by sales**.
- **CSV export** of summarized monthly sales data for reporting purposes.

---

### **Features**
1. **Monthly Sales Trend**  
   - Visualize sales performance over time with a line plot.  
   - Labels on data points display exact sales values for clarity.

2. **Top Products Summary**  
   - Displays a ranked list of top-performing products based on sales amount.

3. **CSV Export**  
   - Generates a CSV file containing a summary of monthly sales for easy reporting.

---

### **How to Run**

#### **1. Clone the Repository**
```bash
git clone https://github.com/elijahjlv/AI-Sales-Insights-Dashboard.git
cd AI-Sales-Insights-Dashboard
```

#### **2. Install Dependencies**
Ensure you have Python 3.6+ installed. Then, install the required libraries using:
```bash
pip install -r requirements.txt
```

#### **3. Run the Script**
To execute the analysis and generate the output:
```bash
python src/app.py
```

#### **4. View the Outputs**
- **Sales Trend Plot**: Saved as `data/sales_trend.png`.  
- **Monthly Sales Summary**: Saved as `data/monthly_sales_summary.csv`.  
- **Top Products**: Printed in the terminal.

---

### **Alternate Ways to Run**

#### **Using a Virtual Environment**
1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python src/app.py
   ```

#### **Using Docker (Optional)**
1. Build the Docker image:
   ```bash
   docker build -t ai-sales-insights .
   ```
2. Run the container:
   ```bash
   docker run -v $(pwd)/data:/app/data ai-sales-insights
   ```

---

### **Example Dataset**
Here’s a preview of the input dataset (`data/sales_data.csv`):
```csv
date,product_id,product_name,sales_amount,customer_id
2025-01-01,101,Product A,200,1
2025-01-02,102,Product B,150,2
2025-02-01,101,Product A,300,3
2025-02-15,103,Product C,400,4
2025-03-05,104,Product D,450,5
```

---

### **Project Structure**
```
AI-Sales-Insights-Dashboard/
├── data/
│   ├── sales_data.csv               # Input data
│   ├── sales_trend.png              # Generated sales trend plot
│   ├── monthly_sales_summary.csv    # Exported sales summary
├── src/
│   ├── app.py                       # Main Python script
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies
```

---

### **Requirements**
- Python 3.6+
- Libraries: `pandas`, `matplotlib`

---

### **License**
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

### **Contributing**
Contributions are welcome! Feel free to fork this repository, submit issues, or create pull requests.

---

### **Contact**
For questions or feedback, please reach out:
- **Name**: Elijah Johnson  
- **GitHub**: [elijahjlv](https://github.com/elijahjlv)

