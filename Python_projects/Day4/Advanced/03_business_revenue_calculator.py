"""
Advanced Project 3: Business Revenue Calculator
Demonstrates Arithmetic, Assignment, and Comparison Operators.
Clean Code Principles: Clear aggregate functions.
"""

def calculate_tier_revenue(users, price_per_user):
    return users * price_per_user

def run_revenue_calculator():
    print("--- SaaS Business Revenue Calculator ---")
    
    # Tier pricing structure
    TIER_BASIC_PRICE = 10.0
    TIER_PRO_PRICE = 30.0
    TIER_ENTERPRISE_PRICE = 100.0
    
    try:
        basic_users = int(input(f"Enter number of Basic tier users (${TIER_BASIC_PRICE}/mo): "))
        pro_users = int(input(f"Enter number of Pro tier users (${TIER_PRO_PRICE}/mo): "))
        ent_users = int(input(f"Enter number of Enterprise tier users (${TIER_ENTERPRISE_PRICE}/mo): "))
        
        if basic_users < 0 or pro_users < 0 or ent_users < 0:
            print("User counts cannot be negative.")
            return

        rev_basic = calculate_tier_revenue(basic_users, TIER_BASIC_PRICE)
        rev_pro = calculate_tier_revenue(pro_users, TIER_PRO_PRICE)
        rev_ent = calculate_tier_revenue(ent_users, TIER_ENTERPRISE_PRICE)
        
        total_monthly_revenue = rev_basic + rev_pro + rev_ent
        total_annual_revenue = total_monthly_revenue * 12
        
        print("\\n--- Revenue Summary ---")
        print(f"Basic Tier Revenue: ${rev_basic:.2f}/mo")
        print(f"Pro Tier Revenue: ${rev_pro:.2f}/mo")
        print(f"Enterprise Tier Revenue: ${rev_ent:.2f}/mo")
        print("-----------------------")
        print(f"Total Monthly Recurring Revenue (MRR): ${total_monthly_revenue:.2f}")
        print(f"Total Annual Recurring Revenue (ARR): ${total_annual_revenue:.2f}")
        
        # Target check
        MRR_TARGET = 10000.0
        if total_monthly_revenue >= MRR_TARGET:
            print(f"\\nCongratulations! You have hit your monthly target of ${MRR_TARGET}.")
        else:
            shortfall = MRR_TARGET - total_monthly_revenue
            print(f"\\nYou are ${shortfall:.2f} away from your monthly target of ${MRR_TARGET}.")

    except ValueError:
        print("Invalid input. Please enter whole numbers.")

if __name__ == "__main__":
    run_revenue_calculator()
