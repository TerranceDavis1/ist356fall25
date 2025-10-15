import pandas as pd 
import streamlit as st 

def clean_currency(value):
    """
    Removes $ and , then converts to float.
    Returns 0.0 if conversion fails.
    """
    try:
        value = str(value).replace('$', '').replace(',', '').strip()
        return float(value)
    except:
        return 0.0

if __name__ == '__main__':
    # Simple tests
    print(clean_currency("$1,234.56"))  # 1234.56
    print(clean_currency("  $89 "))     # 89.0
    print(clean_currency(450))          # 450.0
    print(clean_currency("bad"))        # 0.0
