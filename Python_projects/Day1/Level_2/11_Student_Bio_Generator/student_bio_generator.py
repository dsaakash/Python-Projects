
# ============================================
#  Project 11: Student Bio Generator
#  Topics Used: print(), input()
# ============================================

print("=" * 50)
print("        STUDENT BIO GENERATOR")
print("=" * 50)
print("Fill in the details to generate your Student Bio!")
print("=" * 50)

name = input("\nEnter your full name: ")
rollno = input("Enter your roll number: ")
course = input("Enter your course name: ")
year = input("Enter your current year (1st/2nd/etc): ")
college = input("Enter your college name: ")
city = input("Enter your city: ")
skills = input("Enter your skills (comma separated): ")
languages = input("Enter languages you know: ")
email = input("Enter your email ID: ")
phone = input("Enter your phone number: ")
linkedin = input("Enter your LinkedIn profile (or 'NA'): ")

print()
print("=" * 50)
print("        📋 STUDENT BIO CARD 📋")
print("=" * 50)
print(f"""
Hi! I am {name}, a {year} year student pursuing 
{course} from {college}, {city}.

Roll Number : {rollno}
Skills      : {skills}
Languages   : {languages}

📧 Email    : {email}
📞 Phone    : {phone}
🔗 LinkedIn : {linkedin}
""")
print("=" * 50)
print("   ✨ Future Leader in the Making! ✨")
print("=" * 50)
