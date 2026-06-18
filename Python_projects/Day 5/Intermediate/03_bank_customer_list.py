"""
Intermediate Project 3: Bank Customer List
Concepts: Nested Lists, looping, list comprehension filtering.
"""

def run_bank_system():
    # Data: [Account Number, Name, Balance, Account Type]
    customers = [
        [1001, "Alice Smith", 5000.0, "Savings"],
        [1002, "Bob Jones", 1500.0, "Checking"],
        [1003, "Charlie Davis", 25000.0, "Savings"],
        [1004, "Diana Prince", 800.0, "Checking"],
        [1005, "Evan Wright", 12000.0, "Savings"]
    ]
    
    print("--- Bank Customer Database ---")
    
    print(f"\\n{'Acc #':<8} | {'Name':<15} | {'Balance':<10} | {'Type':<10}")
    print("-" * 50)
    for cust in customers:
        print(f"{cust[0]:<8} | {cust[1]:<15} | ${cust[2]:<9.2f} | {cust[3]:<10}")
        
    print("\\n--- Analytics ---")
    
    # 1. Using list comprehension to get all balances
    balances = [cust[2] for cust in customers]
    total_deposits = sum(balances)
    print(f"Total Bank Deposits: ${total_deposits:.2f}")
    
    # 2. Filtering using list comprehension (VIP customers > $10,000)
    vip_customers = [cust for cust in customers if cust[2] > 10000.0]
    
    print("\\nVIP Customers (Balance > $10,000):")
    for vip in vip_customers:
        print(f"- {vip[1]} (Balance: ${vip[2]:.2f})")
        
    # 3. Filtering by string match
    savings_accounts = [cust for cust in customers if cust[3] == "Savings"]
    print(f"\\nNumber of Savings Accounts: {len(savings_accounts)}")

if __name__ == "__main__":
    run_bank_system()
