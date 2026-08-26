# 🛒 E-Commerce Sales Analysis Project

An end-to-end E-Commerce Sales Analysis project built using Python, Pandas, FastAPI, and Streamlit. The project processes sales data, performs statistical and business analysis, provides sales forecasting and product recommendations, and presents the results through an interactive web dashboard.

---

## 🚀 Live Demo

ry the deployed E-commerce sales Dashboard

[👉 Open the E-Commerce Sales Dashboard](  https://rishiiioffl-jpg-sales-analysis-internship--streamlit-app-qwtevq.streamlit.app/ )

## 🔌 API Endpoints

The project provides a FastAPI backend with the following endpoints:

| Endpoint | Description |
|---|---|
| `/` | Check API status |
| `/sales` | Get all sales records |
| `/sales/total` | Get total revenue |
| `/sales/average` | Get average sale |
| `/sales/highest` | Get highest sale |
| `/sales/lowest` | Get lowest sale |
| `/sales/quantity` | Get total quantity sold |
| `/sales/products` | Get product-wise sales |
| `/sales/categories` | Get category-wise sales |
| `/sales/best-product` | Get best-selling product |
| `/sales/best-day` | Get best sales day |
| `/sales/daily` | Get daily sales |
| `/sales/monthly` | Get monthly sales |
| `/sales/summary` | Get complete sales summary |


## 🏗️ Project Architecture

The project follows a simple data-analysis and API-driven dashboard architecture:

```text
Sales CSV Data
      ↓
Data Processing
      ↓
Sales Analysis
      ↓
FastAPI Backend
      ↓
Streamlit Dashboard
      ↓
Interactive Sales Insights

Main Components
Data Processing — Cleans and validates the sales dataset.
Sales Analysis — Calculates revenue, quantities, product performance, and sales trends.
FastAPI — Provides REST API endpoints for accessing sales analysis results.
Streamlit — Provides the interactive frontend dashboard.
Testing — Validates data processing and application functionality.
Deployment — FastAPI backend is deployed in production and the Streamlit dashboard is hosted online.


### 🔗 FastAPI Backend

[👉 Open the Sales Analysis API](https://sales-analysis-api-deef.onrender.com)

---

## 📌 Project Overview

The E-Commerce Sales Analysis project is designed to transform raw sales data into useful business insights.

The system performs data loading, cleaning, validation, sales calculations, product and category analysis, trend analysis, forecasting, recommendations, performance testing, and visualization.

The project also provides a REST API using FastAPI and an interactive dashboard using Streamlit.

---

## 🎯 Project Objectives

- Load and process e-commerce sales data.
- Clean and validate the dataset.
- Calculate total sales and revenue.
- Analyze product-wise sales.
- Analyze category-wise sales.
- Analyze daily and monthly sales trends.
- Identify the best-selling products.
- Identify the highest and lowest sales.
- Provide sales forecasting.
- Generate product recommendations.
- Test performance on large datasets.
- Provide a REST API for sales analysis.
- Build an interactive sales dashboard.
- Deploy the API and dashboard online.

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **FastAPI**
- **Streamlit**
- **Uvicorn**
- **Git**
- **GitHub**
- **Render**
- **Streamlit Community Cloud**

---

## ✨ Key Features

### 📊 Sales Analysis

- Total revenue calculation
- Average sale calculation
- Highest sale identification
- Lowest sale identification
- Total quantity sold
- Product-wise sales
- Category-wise sales
- Daily sales
- Monthly sales
- Best-selling product
- Best sales day

### 🔮 Advanced Features

- Sales forecasting
- Product recommendation
- Sales trend analysis
- Business insights

### ⚡ Performance Testing

The sales analysis pipeline was tested using a larger dataset created from the original dataset.

Performance testing was performed to evaluate how efficiently the pipeline handles larger amounts of sales data.

### 🌐 REST API

The project provides FastAPI endpoints for accessing sales information programmatically.

### 📈 Interactive Dashboard

The Streamlit dashboard displays:

- Total revenue
- Average sale
- Quantity sold
- Best-selling product
- Highest sale
- Lowest sale
- Best sales day
- Product revenue
- Category sales
- Sales visualizations
- Key business insights

---

## 🏗️ Project Architecture

```text
                Sales Dataset
                     │
                     ▼
              Data Processing
                     │
                     ▼
             Sales Analysis
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Forecasting  Analysis  Recommendations
          │          │          │
          └──────────┼──────────┘
                     ▼
                  FastAPI
                     │
                     ▼
                 Streamlit
                  Dashboard
                     │
                     ▼
                Business Insights
```

---

## 📁 Project Structure

```text
sales-analysis-internship-project/
│
├── data/
│   └── sales_data.csv
│
├── api.py
├── sales_analysis.py
├── data_processing.py
├── advanced_features.py
├── performance_test.py
├── optimised_sales_analysis.py
├── dashboard_utils.py
├── visualisation.py
├── sales_logger.py
├── user_testing.py
├── streamlit_app.py
│
├── requirements.txt
├── documentation.md
├── README.md
├── .gitignore
│
├── category_sales_ui.png
├── monthly_sales.png
├── product_sales_ui.png
├── product_wise_sales.png
├── product_wise_sales_improved.png
├── quantity_by_product.png
└── sales_forecast.png
```

---

## 🔄 Data Processing Pipeline

The project follows these main data processing steps:

### 1. Data Loading

The sales dataset is loaded from a CSV file using Pandas.

### 2. Data Cleaning

The dataset is cleaned by:

- Removing duplicate records.
- Handling missing values.
- Converting dates into the correct format.
- Converting numeric columns into appropriate data types.

### 3. Sales Calculation

Total sales are calculated using:

```text
Total Sales = Quantity × Price
```

### 4. Data Analysis

The processed data is grouped and analyzed by:

- Product
- Category
- Date
- Month

### 5. Visualization

Sales results are presented through charts and the Streamlit dashboard.

### 6. API Integration

The processed data and analysis results are exposed through FastAPI endpoints.

### 7. Dashboard

The Streamlit frontend connects to the deployed API and displays the results interactively.

---

## 🌐 FastAPI Endpoints

The backend provides several endpoints.

| Endpoint | Description |
|---|---|
| `/` | API status |
| `/sales` | Get all sales records |
| `/sales/total` | Get total revenue |
| `/sales/average` | Get average sale |
| `/sales/highest` | Get highest sale |
| `/sales/lowest` | Get lowest sale |
| `/sales/quantity` | Get total quantity sold |
| `/sales/products` | Product-wise sales |
| `/sales/categories` | Category-wise sales |
| `/sales/best-product` | Best-selling product |
| `/sales/best-day` | Best sales day |
| `/sales/daily` | Daily sales |
| `/sales/monthly` | Monthly sales |
| `/sales/summary` | Complete sales summary |

---

## 🔗 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
https://sales-analysis-api-deef.onrender.com/docs
```

### ReDoc

```text
https://sales-analysis-api-deef.onrender.com/redoc
```

---

## 📊 Dashboard

The Streamlit dashboard connects directly to the deployed FastAPI backend.

The dashboard provides a simple interface for viewing sales metrics and business insights.

### Main Dashboard Metrics

- 💰 Total Revenue
- 📊 Average Sale
- 📦 Quantity Sold
- 🏆 Best Product
- 📈 Highest Sale
- 📉 Lowest Sale
- 📅 Best Sales Day
- 💵 Best Product Revenue

---

## 🔮 Sales Forecasting

The project includes sales forecasting functionality to analyze historical sales patterns and estimate future sales trends.

Forecasting can help identify:

- Expected future sales
- Sales trends
- Potential growth
- Periods of increased or decreased demand

---

## 🛍️ Product Recommendation

The recommendation feature uses sales information to identify products that may be recommended based on their sales performance.

This can help businesses understand which products are performing well and may deserve greater attention.

---

## ⚡ Performance Testing

Performance testing was performed on the sales analysis pipeline.

A larger dataset was generated by replicating the original dataset and running the complete analysis pipeline against it.

Example performance results:

```text
Performance Test Results

Run 1: 0.0310 seconds
Run 2: 0.0283 seconds
Run 3: 0.0297 seconds
```

Additional optimized testing was also performed after improving the implementation:

```text
Optimized Performance Test Results

Run 1: 0.1413 seconds
Run 2: 0.1515 seconds
Run 3: 0.1182 seconds
```

The testing process helped evaluate the behavior of the analysis pipeline when working with larger datasets.

---

## 🧪 Testing

The project includes testing for:

- Data validation
- Sales calculations
- Pipeline execution
- Performance
- Dashboard functionality
- API functionality
- User experience

---

## 📝 Logging

Logging functionality was added to record important sales analysis and application events.

The logging system helps with:

- Tracking application activity
- Identifying errors
- Debugging
- Monitoring analysis operations

---

## 💻 Running the Project Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/rishiioffl-jpg/sales-analysis-internship-project.git
```

### Step 2: Enter the project directory

```bash
cd sales-analysis-internship-project
```

### Step 3: Create a virtual environment

```bash
python -m venv .venv
```

### Step 4: Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running FastAPI

Start the FastAPI backend using:

```bash
uvicorn api:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Running Streamlit

Start the Streamlit dashboard using:

```bash
streamlit run streamlit_app.py
```

The dashboard will open in your browser.

---

## ☁️ Deployment

### Backend

The FastAPI backend is deployed using **Render**.

```text
https://sales-analysis-api-deef.onrender.com
```

### Frontend

The Streamlit dashboard is deployed using **Streamlit Community Cloud**.

```text
PASTE_YOUR_STREAMLIT_URL_HERE
```

---

## 🔐 Environment Configuration

The Streamlit application uses the deployed FastAPI URL to communicate with the backend.

Example:

```python
API_URL = "https://sales-analysis-api-deef.onrender.com"
```

For local development, the API URL can be changed to:

```python
API_URL = "http://127.0.0.1:8000"
```

---

## 📈 Project Workflow

```text
1. Collect Sales Data
        ↓
2. Load CSV Dataset
        ↓
3. Clean & Validate Data
        ↓
4. Calculate Total Sales
        ↓
5. Analyze Products & Categories
        ↓
6. Analyze Daily & Monthly Trends
        ↓
7. Perform Forecasting
        ↓
8. Generate Recommendations
        ↓
9. Test Performance
        ↓
10. Expose Results Through FastAPI
        ↓
11. Connect Streamlit Dashboard
        ↓
12. Deploy API
        ↓
13. Deploy Dashboard
```

---

## 🎓 Internship Learning Outcomes

Through this project, the following skills were practiced:

- Python programming
- Data manipulation with Pandas
- Numerical computing with NumPy
- Data visualization
- Data cleaning
- Feature engineering
- Sales trend analysis
- Performance optimization
- REST API development
- FastAPI
- Streamlit
- Testing and debugging
- Logging
- Git and GitHub
- Cloud deployment
- Project documentation

---

## 📌 Future Improvements

Possible future improvements include:

- User authentication
- Database integration
- Advanced machine learning forecasting
- More advanced recommendation algorithms
- Interactive filtering
- Real-time sales data
- Automated reports
- Improved dashboard visualizations
- Role-based access
- Cloud database integration

---

## 👨‍💻 Author

**Rishiketh**

Computer Science & Engineering – Artificial Intelligence & Machine Learning

---

## 📜 License

This project was created for educational and internship purposes.

---

## ⭐ Acknowledgement

This project was developed as part of an internship/project-based learning program focused on Python, data analysis, API development, visualization, testing, and deployment.