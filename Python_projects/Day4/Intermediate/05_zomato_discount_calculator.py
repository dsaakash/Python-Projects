"""
Intermediate Project 5: Zomato Discount Calculator
Demonstrates Logical and Comparison Operators.
Clean Code Principles: Magic strings/numbers extracted, clean conditional logic.
"""

def get_discount_amount(order_total, promo_code):
    """
    Determines the discount amount based on promo codes and logical conditions.
    """
    PROMO_WELCOME50 = "WELCOME50"  # 50% off up to $100
    PROMO_FLAT200 = "FLAT200"      # Flat $200 off on orders above $500
    
    if promo_code == PROMO_WELCOME50:
        discount = order_total * 0.50
        # Logical / comparison operator to cap discount
        if discount > 100.0:
            return 100.0
        return discount
        
    elif promo_code == PROMO_FLAT200:
        if order_total >= 500.0:
            return 200.0
        else:
            print(f"Code {PROMO_FLAT200} is only valid on orders of $500 or more.")
            return 0.0
            
    else:
        print("Invalid or expired promo code.")
        return 0.0

def run_zomato_calculator():
    print("--- Zomato Discount Calculator ---")
    
    try:
        order_total = float(input("Enter your total order amount: $"))
        
        if order_total <= 0:
            print("Order amount must be greater than zero.")
            return
            
        apply_promo = input("Do you have a promo code? (yes/no): ").strip().lower()
        
        discount_amount = 0.0
        
        if apply_promo == 'yes':
            print("Available Codes: WELCOME50, FLAT200")
            promo_code = input("Enter promo code: ").strip().upper()
            discount_amount = get_discount_amount(order_total, promo_code)
            
        final_amount = order_total - discount_amount
        
        print("\\n--- Bill Breakdown ---")
        print(f"Order Total: ${order_total:.2f}")
        if discount_amount > 0:
            print(f"Discount Applied: -${discount_amount:.2f}")
        print(f"Amount Payable: ${final_amount:.2f}")

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")

if __name__ == "__main__":
    run_zomato_calculator()
