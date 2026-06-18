
# ============================================
#  Project 12: Resume Summary Generator
#  Topics Used: print(), input()
# ============================================

print("=" * 55)
print("        RESUME SUMMARY GENERATOR")
print("=" * 55)
print("Answer the questions to generate your Resume Summary!")
print("=" * 55)

name = input("\nEnter your full name: ")
experience = input("Years of experience (or 'Fresher'): ")
degree = input("Enter your highest qualification: ")
specialization = input("Enter specialization/major: ")
college = input("Enter college/university: ")
top_skill1 = input("Enter your top skill #1: ")
top_skill2 = input("Enter your top skill #2: ")
top_skill3 = input("Enter your top skill #3: ")
achievement = input("Enter one major achievement: ")
goal = input("Enter your career goal: ")
email = input("Enter your email: ")
phone = input("Enter your phone: ")

print()
print("=" * 55)
print("         📄 RESUME SUMMARY 📄")
print("=" * 55)
print(f"""
{name.upper()}
{email} | {phone}
{'─' * 50}

PROFESSIONAL SUMMARY
{'─' * 50}
A highly motivated {experience} professional with a 
{degree} in {specialization} from {college}. 
Proficient in {top_skill1}, {top_skill2}, and {top_skill3}.
Recognized for {achievement}.
Seeking to {goal} and contribute effectively 
to a dynamic organization.

KEY SKILLS
{'─' * 50}
✦ {top_skill1}
✦ {top_skill2}
✦ {top_skill3}
""")
print("=" * 55)
print("   📌 Your Resume Summary is Ready! 📌")
print("=" * 55)
