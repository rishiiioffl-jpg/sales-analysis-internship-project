import pandas as pd
def load_data(file_path):
    #Load sales data from a CSV file.
    df = pd.read_csv(file_path)
    return df
def clean_data(df):
    #clean snd prepare the sales data for analysis.
    #remove duplicate rows
    df = df.drop_duplicates()
    #remove rows with missing values
    df=df.dropna()
    #convert date column
    df["Date"]=pd.to_datetime(df["Date"])
    return df
def process_data(file_path):
    #Load and clean the sales data.
    df = load_data(file_path)
    print("Data loaded successfully.")
    print("Original shape:", df.shape)
    df = clean_data(df)
    return df
#Run pipeline 
sales_data=process_data("data/sales_data.csv")
print("\n Processed data: ")
print(sales_data.head())
    


    
