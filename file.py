import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt


# Load dataset
df = pd.read_csv("online_retail.csv", encoding='ISO-8859-1')

# 0. Remove missing CustomerID
df = df.dropna(subset=['CustomerID'])

# 1. convert CustomerID to integer
df['CustomerID'] = df['CustomerID'].astype(int)

# 2. Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 3. Remove negative or zero Quantity
df = df[df['Quantity'] > 0]

# 4. Remove zero or negative price
df = df[df['UnitPrice'] > 0]

# 5. Create TotalPrice column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Check cleaned data
print(df.info())
# print(df.head())


# Reference date (latest date in dataset + 1 day)
today_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

# Create RFM table
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (today_date - x.max()).days,  # Recency
    'InvoiceNo': 'count',                                 # Frequency
    'TotalPrice': 'sum'                                   # Monetary
})

# Rename columns
rfm.columns = ['Recency', 'Frequency', 'Monetary']


# Create RFM scores (1–5)

rfm['R_score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1])
rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
rfm['M_score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])

# Convert to string for segmentation
rfm['RFM_Score'] = rfm['R_score'].astype(str) + rfm['F_score'].astype(str)


def segment_customer(row):
    if row['RFM_Score'] in ['55', '54']:
        return 'Champions'
    elif row['RFM_Score'] in ['53', '52']:
        return 'Loyal'
    elif row['RFM_Score'] in ['51']:
        return 'New Customers'
    elif row['RFM_Score'] in ['44', '43']:
        return 'Potential Loyalists'
    elif row['RFM_Score'] in ['33', '32']:
        return 'Needs Attention'
    else:
        return 'At Risk'
    
rfm['Segment'] = rfm.apply(segment_customer, axis=1)
# print(rfm['Segment'].value_counts())

segment_revenue = rfm.groupby('Segment')['Monetary'].sum().sort_values(ascending=False)
print(segment_revenue)

# top_customers = rfm.sort_values(by='Monetary', ascending=False).head(10)
# print(top_customers)

# Save cleaned transactional data
df.to_csv("cleaned_transactions.csv", index=False)

# Save RFM data
rfm = rfm.reset_index()
rfm.to_csv("rfm_customers.csv", index=False)


# # Segment distribution
# rfm['Segment'].value_counts().plot(kind='bar')

# plt.title("Customer Segmentation Distribution")
# plt.xlabel("Segment")
# plt.ylabel("Number of Customers")
# plt.xticks(rotation=45)
# plt.show()