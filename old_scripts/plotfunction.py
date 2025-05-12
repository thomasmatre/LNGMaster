import matplotlib.pyplot as plt
import pandas as pd

def plot_spot_rates(data, start_date=None, end_date=None):
    """
    Plot actual and predicted LNG spot rates over a custom period.

    Parameters:
    - data: DataFrame with 'Actual Spot Rate' and 'Predicted Spot Rate'
    - start_date: (str) e.g., '2022-01-01'
    - end_date: (str) e.g., '2024-12-01'
    """

    # Filter by date if provided
    plot_df = data.copy()
    if start_date:
        plot_df = plot_df[plot_df.index >= pd.to_datetime(start_date)]
    if end_date:
        plot_df = plot_df[plot_df.index <= pd.to_datetime(end_date)]

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(plot_df.index, plot_df['LNG 174K CBM (2-stroke dual fuel) Spot Rate (avg., $/day)'],
             label='Actual Spot Rate', marker='o', markersize=4)
    plt.plot(plot_df.index, plot_df['Predicted Spot Rate'],
             label='Forecasted Spot Rate', linestyle='--', marker='x', color='red')
    plt.title(f"LNG Spot Charter Rate Forecast\n({start_date or 'Start'} to {end_date or 'End'})")
    plt.xlabel("Date")
    plt.ylabel("Spot Rate ($/day)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()