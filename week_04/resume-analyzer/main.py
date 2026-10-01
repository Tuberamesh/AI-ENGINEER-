from analyzer import analyze_resume


resume = """
Python
SQL
Pandas
Power BI
3 data analytics projects
"""

job_description = """
Looking for a Data Analyst with Python, SQL, Pandas,
AWS and Docker experience.
"""


result = analyze_resume(resume, job_description)

print("Matched Skills:", result.matched_skills)
print("Missing Skills:", result.missing_skills)
print("Experience Match:", result.experience_match)
print("Suggestions:", result.suggestions)
print("Score:", result.score)