import pandas as pd

def parse_stock_data(file)-> list[str]:
    """
    Parses stock data from an Excel file and returns it as a list of isins.

    Args:
        file (xlsx): The path to the Excel file containing stock data.
    
    """
    df = pd.read_excel(file)
    isins = df['ISIN'].tolist()
    return isins
