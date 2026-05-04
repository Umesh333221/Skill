# Career Guidance & Skill Gap Analyzer

A simple web application built with Streamlit to help users analyze their skills against job requirements and get career recommendations.

## Features

- Skill gap analysis: Compare your skills to those required for a specific job
- Career recommendations: Get suggestions for other careers based on your skill set
- User-friendly interface: Select skills and jobs from predefined lists

## Installation

1. Ensure you have Python installed (version 3.7 or higher).
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   streamlit run app.py
   ```
2. Open your web browser and go to the URL displayed (usually http://localhost:8501).
3. Select your skills from the list.
4. Choose a desired job to analyze.
5. Click "Analyze" to see the results.

## How it works

The application uses predefined skill requirements for various jobs. It compares your selected skills against these requirements to identify matches and gaps. Career recommendations are based on the percentage of matching skills for other job roles.