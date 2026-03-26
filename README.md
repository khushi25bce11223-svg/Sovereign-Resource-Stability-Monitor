# Sovereign Resource Stability Monitor (SRSM)

### Project Overview
This project is an automated tool for government officials to monitor essential resources like Wheat and LPG. It calculates how many days of stock are left and detects unusual spikes in consumption (hoarding).

### How to Run
1. **Clone the repo:**
   `git clone https://github.com/your-username/SRSM.git`
2. **Install requirements:**
   `pip install pandas matplotlib`
3. **Run the program:**
   `python main.py`

### Mathematical Formulas Used
* **Days of Cover:** Total Stock / Daily Consumption.
* **Panic Trigger:** If (Current Usage > Normal Usage * 1.3), trigger hoarding alert.
