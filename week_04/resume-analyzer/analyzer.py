import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ResumeAnalysis(BaseModel):
    matched_skills: list[str]
    missing_skills: list[str]
    experience_match: str
    suggestions: list[str]
    score: int


def analyze_resume(resume: str, job_description: str):

    system_prompt = """
    You are a resume analyzer.

    Compare the resume with the job description.

    Identify:
    - matched skills
    - missing skills
    - experience match
    - practical suggestions
    - score from 0 to 100

    Do not invent information.
    """

    user_prompt = f"""
    Analyze this resume against this job description.

    RESUME:
    {resume}

    JOB DESCRIPTION:
    {job_description}
    """

    response = client.responses.parse(
        model="gpt-4o-mini",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        text_format=ResumeAnalysis
    )

    return response.output_parsed