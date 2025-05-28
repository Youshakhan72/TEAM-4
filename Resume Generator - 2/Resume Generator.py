name = input("Name: ")
title = input("Job Title: ")
skills = input("Skills (comma-separated): ").split(",")
experience = input("Previous Experience: ")

resume = f"""
=== {name.upper()} ===
Job Title: {title}

Skills:
{chr(10).join('- ' + s.strip() for s in skills)}

Experience:
{experience}
"""

with open("resume.txt", "w") as f:
    f.write(resume)

print("Resume saved to resume.txt")