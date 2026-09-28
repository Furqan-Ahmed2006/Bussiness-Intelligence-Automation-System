import pandas as pd
import numpy as np

def generate_dirty_batch(filename, is_excel=False):
    np.random.seed(42 if 'batch_1' in filename else 101)
    
    dates = ['2026-09-01', '2026/09/02', '03-09-2026', None, '2026-09-05', 'INVALID_DATE']
    categories = {'Electronics': ['Laptop', 'Headphones'], 'Apparel': ['Shirt', 'Jeans'], 'Home': ['Lamp', 'Chair']}
    
    data = []
    for i in range(18): 
        cat = np.random.choice(list(categories.keys()))
        prod = np.random.choice(categories[cat])
        
        data.append({
            'Transaction ID': f"TXN-{2000+i}",
            'Date': np.random.choice(dates),
            'Customer ID': f"CUST-{np.random.randint(100, 110)}",
            'Category': cat,
            'Product': prod,
            'Quantity': np.random.choice([1, 2, -5, 3, None]), 
            'Unit Price': np.random.choice([50.0, 150.0, -20.0, 300.0, 0.0]) 
        })
    
    data.append(data[0].copy())
    data.append(data[1].copy())
    
    df = pd.DataFrame(data)
    
    if is_excel:
        df.to_excel(filename, index=False)
    else:
        df.to_csv(filename, index=False)
    print(f"Generated 20 unclean test records at: {filename}")

if __name__ == "__main__":
    generate_dirty_batch("sales_batch_1_dirty.csv", is_excel=False)
    generate_dirty_batch("sales_batch_2_dirty.xlsx", is_excel=True)