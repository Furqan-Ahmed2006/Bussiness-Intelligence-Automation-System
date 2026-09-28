import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def generate_sales_forecast(df, forecast_days=30):
    """
    Generates a trend-based sales forecast for the next N days.
    """
    df_daily = df.groupby('date')['total_amount'].sum().reset_index()
    df_daily['date'] = pd.to_datetime(df_daily['date'])
    df_daily = df_daily.sort_values('date')

    if len(df_daily) < 5:
        return None

    df_daily['day_num'] = (df_daily['date'] - df_daily['date'].min()).dt.days

    X = df_daily[['day_num']]
    y = df_daily['total_amount']

    model = LinearRegression()
    model.fit(X, y)

    last_day_num = df_daily['day_num'].max()
    future_days = np.arange(last_day_num + 1, last_day_num + forecast_days + 1).reshape(-1, 1)

    future_dates = [df_daily['date'].max() + pd.Timedelta(days=int(i)) for i in range(1, forecast_days + 1)]
    future_df = pd.DataFrame(future_days, columns=['day_num'])
    future_preds = model.predict(future_df)
    future_preds = np.maximum(future_preds, 0) 

    forecast_df = pd.DataFrame({
        'date': future_dates,
        'predicted_sales': future_preds
    })

    return forecast_df