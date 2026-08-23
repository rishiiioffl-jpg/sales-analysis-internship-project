from flask import Flask, jsonify
import pandas as pd 
app=Flask(__name__)
#Load sales data
sales_data=pd.read_csv("data/sales_data.csv")
@app.route("/sales",methods=["GET"])
def get_sales():
    return jsonify(sales_data.to_dict(orient="records"))
@app.route("/sales/summary",methods=["GET"])
def get_summary():
    total_revenue=sales_data["Revenue"].sum()
    total_quantity=sales_data["Quantity"].sum()
    return jsonify({"total_revenue":total_revenue,"total_quantity":total_quantity})
@app.route("/sales/products",methods=["GET"])
def get_products():
    product_sales=sales_data.groupby("Product")["Revenue"].sum()
    return jsonify(product_sales.to_dict())
if __name__=="__main__":
    app.run(debug=True)