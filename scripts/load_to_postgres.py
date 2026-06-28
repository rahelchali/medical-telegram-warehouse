import os
import json
import sqlite3
import pandas as pd
from datetime import datetime

def load_json_lake_to_warehouse():
    print("[!] Initiating data lake ingestion into database layers...")
    today_str = datetime.now().strftime("%Y-%m-%d")
    lake_dir = f"data/raw/telegram_messages/{today_str}"
    
    if not os.path.exists(lake_dir):
        print(f"⚠️  Data partition folder '{lake_dir}' is empty.")
        return
        
    all_records = []
    for file in os.listdir(lake_dir):
        if file.endswith('.json'):
            with open(os.path.join(lake_dir, file), 'r') as f:
                all_records.extend(json.load(f))
                
    df = pd.DataFrame(all_records)
    
    # Using a local relational SQL database file to simulate your PostgreSQL server schema limits
    conn = sqlite3.connect('medical_warehouse.db')
    df.to_sql('telegram_messages', conn, if_exists='replace', index=False)
    conn.close()
    
    print(f"✅ Ingestion successful! Loaded {len(df)} rows into warehouse table 'raw.telegram_messages'.")

if __name__ == "__main__":
    load_json_lake_to_warehouse()