📊 Customer Lifetime Value (CLV) & RFM Segmentation Dashboard

🔍 Project Overview
This project analyzes transactional customer data to identify high-value customers, segment user behavior, and detect churn risk using **RFM (Recency, Frequency, Monetary) analysis**. The output is visualized through an interactive JavaScript dashboard and supported by exploratory analysis in Power BI.

🎯 Objectives

* Segment customers based on purchasing behavior using RFM scoring
* Identify high-value customers (Champions) contributing maximum revenue
* Detect At-Risk customers with declining engagement
* Analyze revenue distribution and behavioral patterns across segments
* Enable business-focused decision-making through interactive dashboards

🛠️ Tools Used

* Python (Pandas) – data cleaning, transformation, and RFM computation
* JavaScript + Chart.js – interactive dashboard visualization
* Power BI – trend analysis and exploratory insights
* SQL (conceptual) – data structuring approach

📊 Key Insights

* **Champions (~14% of customers)** contribute nearly **half of total revenue**, making them the most valuable segment
* **At Risk customers (~61%)** represent the largest segment and a major retention opportunity
* Customer value distribution is highly skewed — a small group drives most revenue
* High-frequency, recent buyers show significantly higher lifetime value
* Retention strategies offer higher ROI compared to new customer acquisition

📈 Dashboard Features

* KPI overview (total customers, revenue, segment share)
* Revenue by segment (bar chart visualization)
* Customer distribution (donut chart)
* Segment-level metrics (recency, frequency, monetary trends)
* Interactive filtering of **top customers by segment**
* Highlighting of high-value and high-risk customer groups

🚀 Business Impact
This analysis enables businesses to:

* Prioritize **high-value customers (Champions)** for loyalty programs
* Design **win-back campaigns** for At Risk customers
* Optimize marketing spend toward retention rather than acquisition
* Identify top revenue-driving customers for personalized engagement

📁 Project Structure

* rfm_customers.csv → cleaned datasets (RFM outputs)
* file.py → Python scripts for preprocessing and segmentation
* rfm_customer_dashboard.html → JavaScript-based interactive dashboard
* dashboard.pbix → exploratory analysis and trend visuals

📌 Conclusion
The analysis demonstrates that a small segment of customers drives a disproportionate share of revenue, while a large portion of the customer base is at risk of churn. By combining RFM segmentation with interactive visualization, the project provides actionable insights for improving retention and maximizing customer lifetime value.
