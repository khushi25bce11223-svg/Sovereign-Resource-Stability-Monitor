import pandas as pd
import matplotlib.pyplot as plt

def calculate_inventory():
    print("--- Sovereign Resource Stability Monitor (SRSM) ---")
    
    # 1. Load Data
    # Assuming a CSV with columns: Resource, Current_Stock, Daily_Usage, Population
    try:
        df = pd.read_csv('data.csv')
    except:
        print("Error: data.csv not found!")
        return

    # 2. Logic: Days of Cover & Burn Rate
    # Formula: Days = Current Stock / Average Daily Usage
    df['Days_of_Cover'] = df['Current_Stock'] / df['Daily_Usage']
    
    # 3. Logic: Panic Trigger (Hoarding Detection)
    # If usage is 30% higher than normal, we flag it
    NORMAL_USAGE = 100 # Example constant
    df['Status'] = "Normal"
    
    for i in range(len(df)):
        if df.loc[i, 'Daily_Usage'] > (NORMAL_USAGE * 1.3):
            df.loc[i, 'Status'] = "PANIC: Hoarding Detected!"
            # Suggesting lower limit
            df.loc[i, 'Recommendation'] = "Reduce Per-Person Limit by 20%"
        elif df.loc[i, 'Days_of_Cover'] < 7:
            df.loc[i, 'Status'] = "CRITICAL: Low Stock"
            df.loc[i, 'Recommendation'] = "Emergency Restock Required"
        else:
            df.loc[i, 'Recommendation'] = "Stable"

    # 4. Show Results in Terminal
    print("\n--- Current Resource Status ---")
    print(df[['Resource', 'Current_Stock', 'Days_of_Cover', 'Status', 'Recommendation']])
    
    # 5. Simple Dashboard (Visualization)
    df.plot(kind='bar', x='Resource', y='Days_of_Cover', color='teal')
    plt.axhline(y=7, color='r', linestyle='--', label='Critical Threshold (7 Days)')
    plt.title('Inventory Dashboard: Days of Cover per Resource')
    plt.ylabel('Days')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    calculate_inventory()