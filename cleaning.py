import pandas as pd
#read the csv file
df=pd.read_csv("Sample - Superstore.csv")
#Display the first 5 rowss
print(df.head())
#dataset information
print(df.info())
#missing values
print(df.isnull().sum())
#duplicate rows
print("Duplicate rows:",df.duplicated().sum())
#remove duplicate rows
df=df.drop_duplicates()
#fill missing values (if any)
df=df.fillna("Unknown")
#save the cleaned dataset
df.to_csv("Cleaned_Sample - Superstore.csv",index=False)

print("Data cleaned and Saved Successfully!")
import matplotlib.pyplot as plt
#count the number of orders by category
category_count=df["Category"].value_counts()
#create a bar chart
category_count.plot(kind="bar")

plt.title("Orders by category")
plt.xlabel("Category")
plt.ylabel("Number of Orders")
#save the chart
plt.savefig("Category_Chart.png")
#show thw chart
plt.show()
#sales by region
region_sales=df.groupby("Region")["Sales"].sum()
region_sales.plot(kind="pie",autopct="%1.1f%%")
plt.title("Sales by region")
plt.ylabel("")
plt.savefig("Region_Chart.png")
plt.show()
#sales by segment
segment_sales=df.groupby("Segment")["Sales"].sum()
segment_sales.plot(kind="bar")
plt.title("Sales by Segment")
plt.xlabel("Segment")
plt.ylabel("Sales")
plt.savefig("Segment_Chart.png")
plt.show()
