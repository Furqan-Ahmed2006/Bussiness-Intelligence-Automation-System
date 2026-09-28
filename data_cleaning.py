import sqlite3
import pandas as pd

def process_and_ingest_data(file_path_or_buffer, db_path="sales.db"):
    filename = getattr(file_path_or_buffer, 'name', str(file_path_or_buffer)).lower()
    
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        df = pd.read_excel(file_path_or_buffer)
    else:
        df = pd.read_csv(file_path_or_buffer)

    initial_rows = len(df)

    df.columns = df.columns.astype(str).str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')

    df = df.drop_duplicates()

    df['date'] = pd.to_datetime(df['date'],format='mixed', errors='coerce')
    df = df.dropna(subset=['date'])

    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
    df = df[(df['quantity'] > 0) & (df['unit_price'] > 0)]

    df['total_amount'] = df['quantity'] * df['unit_price']
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')

    cleaned_rows = len(df)
    dropped_rows = initial_rows - cleaned_rows

    conn = sqlite3.connect(db_path)
    try:
        existing_ids = pd.read_sql("SELECT transaction_id FROM sales", conn)['transaction_id'].tolist()
        df = df[~df['transaction_id'].isin(existing_ids)]
    except Exception:
        pass 

    if not df.empty:
        df.to_sql("sales", conn, if_exists="append", index=False)
    
    conn.close()

    return {
        "initial_rows": initial_rows,
        "cleaned_rows": cleaned_rows,
        "dropped_rows": dropped_rows,
        "cleaned_df": df
    }