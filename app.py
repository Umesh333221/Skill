import streamlit as st

# Define job skills requirements (example data)
job_skills = {
    "Software Engineer": ["Python", "JavaScript", "SQL", "Git", "Problem Solving"],
    "Data Scientist": ["Python", "R", "Statistics", "Machine Learning", "SQL"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Node.js"],
    "Product Manager": ["Communication", "Analytics", "Project Management", "User Research"],
    "UX Designer": ["Design Thinking", "Prototyping", "User Research", "Figma", "Adobe XD"]
}

# Available skills for user to select
all_skills = set()
for skills in job_skills.values():
    all_skills.update(skills)
all_skills = sorted(list(all_skills))

st.title("Career Guidance & Skill Gap Analyzer")

st.header("Enter Your Skills")
user_skills = st.multiselect("Select the skills you have:", all_skills)

st.header("Select Desired Job")
desired_job = st.selectbox("Choose a job to analyze:", list(job_skills.keys()))

if st.button("Analyze"):
    if not user_skills:
        st.error("Please select at least one skill.")
    elif not desired_job:
        st.error("Please select a desired job.")
    else:
        required_skills = set(job_skills[desired_job])
        user_skills_set = set(user_skills)
        
        matching_skills = user_skills_set & required_skills
        missing_skills = required_skills - user_skills_set
        
        st.subheader("Skill Gap Analysis")
        st.write(f"**Matching Skills:** {', '.join(matching_skills) if matching_skills else 'None'}")
        st.write(f"**Missing Skills:** {', '.join(missing_skills) if missing_skills else 'None'}")
        
        match_percentage = len(matching_skills) / len(required_skills) * 100 if required_skills else 0
        st.write(f"**Match Percentage:** {match_percentage:.1f}%")
        
        if missing_skills:
            st.info("Consider learning the missing skills to pursue this career.")
        else:
            st.success("You have all the required skills for this job!")
        
        st.subheader("Career Recommendations")
        recommendations = []
        for job, req_skills in job_skills.items():
            if job != desired_job:
                req_set = set(req_skills)
                match = len(user_skills_set & req_set) / len(req_set) * 100 if req_set else 0
                recommendations.append((job, match))
        
        recommendations.sort(key=lambda x: x[1], reverse=True)
        for job, match in recommendations[:3]:
            st.write(f"- {job}: {match:.1f}% skill match")