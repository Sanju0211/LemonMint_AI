import gradio as gr
import pandas as pd
import numpy as np
import re
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter

def load_data():
    """Load and clean the job data"""
    try:
        df = pd.read_csv('data/job_data.csv')
        return df
    except Exception as e:
        raise Exception(f"Error loading data: {e}")

def standardize_salary(salary_text):
    """Parse salary text and convert to standardized annual min/max values"""
    if pd.isna(salary_text) or salary_text == '':
        return None, None
    
    salary_text = str(salary_text).replace('$', '').replace(',', '').strip()
    
    range_patterns = [
        r'(\d+(?:\.\d+)?)\s*[-–]\s*(\d+(?:\.\d+)?)',  # Standard ranges
        r'(\d+(?:\.\d+)?)\s*to\s*(\d+(?:\.\d+)?)',    # "X to Y" format
    ]
    
    for pattern in range_patterns:
        match = re.search(pattern, salary_text)
        if match:
            min_val = float(match.group(1))
            max_val = float(match.group(2))
            if any(word in salary_text.lower() for word in ['hour', 'hr', '/hour']):
                min_val *= 2080  # 40 hours * 52 weeks
                max_val *= 2080
            elif any(word in salary_text.lower() for word in ['month', '/month', 'monthly']):
                min_val *= 12
                max_val *= 12
            return min_val, max_val
    
    single_match = re.search(r'(\d+(?:\.\d+)?)', salary_text)
    if single_match:
        val = float(single_match.group(1))
        if any(word in salary_text.lower() for word in ['hour', 'hr', '/hour']):
            val *= 2080
        elif any(word in salary_text.lower() for word in ['month', '/month', 'monthly']):
            val *= 12
        return val, val
    
    return None, None

def extract_ai_skills(job_description):
    """Extract AI/ML skills from job descriptions"""
    if pd.isna(job_description):
        return []
    
    skills_patterns = {
        'Python': r'\bpython\b',
        'PyTorch': r'\bpytorch\b',
        'TensorFlow': r'\btensorflow\b',
        'Machine Learning': r'\bmachine learning\b|\bml\b',
        'Deep Learning': r'\bdeep learning\b',
        'LLM': r'\bllm\b|\blarge language model\b',
        'NLP': r'\bnlp\b|\bnatural language processing\b',
        'Computer Vision': r'\bcomputer vision\b|\bcv\b',
        'AI': r'\bartificial intelligence\b|\bai\b',
        'Neural Networks': r'\bneural network\b',
        'Data Science': r'\bdata science\b',
        'Kubernetes': r'\bkubernetes\b',
        'Docker': r'\bdocker\b',
        'AWS': r'\baws\b|\bamazon web services\b',
        'GCP': r'\bgcp\b|\bgoogle cloud\b',
        'Azure': r'\bazure\b',
        'Transformers': r'\btransformer\b',
        'BERT': r'\bbert\b',
        'GPT': r'\bgpt\b',
        'LangChain': r'\blangchain\b',
        'Vector Database': r'\bvector database\b|\bpinecone\b|\bweaviate\b',
        'MLOps': r'\bmlops\b',
        'Reinforcement Learning': r'\breinforcement learning\b|\brl\b',
        'Scikit-learn': r'\bscikit-learn\b|\bsklearn\b',
        'Pandas': r'\bpandas\b',
        'NumPy': r'\bnumpy\b',
        'SQL': r'\bsql\b',
        'R': r'\b r \b|\br,|\br\.',
        'Java': r'\bjava\b',
        'C++': r'\bc\+\+\b',
        'Go': r'\bgolang\b|\bgo\b',
        'Rust': r'\brust\b',
        'React': r'\breact\b',
        'Node.js': r'\bnode\.js\b|\bnodejs\b',
        'TypeScript': r'\btypescript\b',
        'JavaScript': r'\bjavascript\b'
    }
    
    found_skills = []
    job_desc_lower = job_description.lower()
    for skill, pattern in skills_patterns.items():
        if re.search(pattern, job_desc_lower, re.IGNORECASE):
            found_skills.append(skill)
    return found_skills

def process_data(df):
    """Process the raw data for analysis"""
    salary_data = df['Salary Range:'].apply(standardize_salary)
    df['salary_min'] = [x[0] for x in salary_data]
    df['salary_max'] = [x[1] for x in salary_data]
    df['salary_avg'] = df[['salary_min', 'salary_max']].mean(axis=1)
    df['skills'] = df['Job Description'].apply(extract_ai_skills)
    df_with_salary = df.dropna(subset=['salary_min', 'salary_max'])
    return df, df_with_salary

def create_dashboard():
    """Create Gradio dashboard"""
    try:
        df = load_data()
        df_processed, df_with_salary = process_data(df)
    except Exception as e:
        return f"Error loading data: {e}", None, None, None, None
    
    # Key Statistics
    total_jobs = len(df_processed)
    median_salary = f"${df_with_salary['salary_avg'].median():,.0f}" if len(df_with_salary) > 0 else "N/A"
    mean_salary = f"${df_with_salary['salary_avg'].mean():,.0f}" if len(df_with_salary) > 0 else "N/A"
    jobs_with_salary = len(df_with_salary)
    stats = f"""
    **Total Jobs**: {total_jobs}  
    **Median Salary**: {median_salary}  
    **Mean Salary**: {mean_salary}  
    **Jobs with Salary Data**: {jobs_with_salary}
    """
    
    # Skills Chart
    all_skills = []
    for skills_list in df_processed['skills']:
        all_skills.extend(skills_list)
    skills_plot = None
    if all_skills:
        skills_counter = Counter(all_skills)
        top_skills = skills_counter.most_common(15)
        if top_skills:
            skills_df = pd.DataFrame(top_skills, columns=['Skill', 'Count'])
            skills_plot = px.bar(
                skills_df, 
                x='Count', y='Skill', orientation='h',
                title="Most Mentioned Skills in Job Descriptions",
                color='Count', color_continuous_scale='viridis'
            ).update_layout(height=500, yaxis={'categoryorder': 'total ascending'})
    
    # Salary by Skills Chart
    salary_skills_plot = None
    if all_skills and len(df_with_salary) > 0:
        skill_salaries = {}
        for skill in [s[0] for s in Counter(all_skills).most_common(10)]:
            jobs_with_skill = df_with_salary[df_with_salary['skills'].apply(lambda x: skill in x)]
            if len(jobs_with_skill) > 0:
                skill_salaries[skill] = jobs_with_skill['salary_avg'].mean()
        if skill_salaries:
            skills_salary_df = pd.DataFrame(list(skill_salaries.items()), columns=['Skill', 'Average Salary']).sort_values('Average Salary', ascending=True)
            salary_skills_plot = px.bar(
                skills_salary_df, x='Average Salary', y='Skill', orientation='h',
                title="Average Salary by Skill", color='Average Salary', color_continuous_scale='plasma'
            ).update_layout(height=400, xaxis_title="Average Annual Salary ($)", yaxis={'categoryorder': 'total ascending'}).update_traces(texttemplate='$%{x:,.0f}', textposition='outside')
    
    # Salary Distribution (Histogram and Box Plot)
    salary_dist_plot = None
    if len(df_with_salary) > 0:
        fig_hist = px.histogram(
            df_with_salary, x='salary_avg', nbins=20,
            title="Salary Distribution", labels={'salary_avg': 'Average Salary ($)', 'count': 'Number of Jobs'}
        ).update_layout(xaxis_title="Annual Salary ($)", yaxis_title="Number of Jobs")
        fig_box = px.box(
            df_with_salary, y='salary_avg',
            title="Salary Range Distribution", labels={'salary_avg': 'Annual Salary ($)'}
        ).update_layout(yaxis_title="Annual Salary ($)")
        salary_dist_plot = [fig_hist, fig_box]
    
    # Job Details Table
    display_df = df_processed[['Job Title', 'salary_min', 'salary_max', 'salary_avg', 'skills']].copy()
    display_df['salary_min'] = display_df['salary_min'].apply(lambda x: f"${x:,.0f}" if pd.notna(x) else "N/A")
    display_df['salary_max'] = display_df['salary_max'].apply(lambda x: f"${x:,.0f}" if pd.notna(x) else "N/A")
    display_df['salary_avg'] = display_df['salary_avg'].apply(lambda x: f"${x:,.0f}" if pd.notna(x) else "N/A")
    display_df['skills'] = display_df['skills'].apply(lambda x: ', '.join(x[:5]) + ('...' if len(x) > 5 else ''))
    display_df.columns = ['Job Title', 'Min Salary', 'Max Salary', 'Avg Salary', 'Top Skills']
    
    # Insights
    insights = []
    if len(df_with_salary) > 0:
        highest_paying = df_with_salary.loc[df_with_salary['salary_avg'].idxmax()]
        lowest_paying = df_with_salary.loc[df_with_salary['salary_avg'].idxmin()]
        insights.append(f"**Highest paying role**: {highest_paying['Job Title']} (${highest_paying['salary_avg']:,.0f})")
        insights.append(f"**Lowest paying role**: {lowest_paying['Job Title']} (${lowest_paying['salary_avg']:,.0f})")
        if all_skills:
            most_common_skill = Counter(all_skills).most_common(1)[0]
            insights.append(f"**Most in-demand skill**: {most_common_skill[0]} (mentioned in {most_common_skill[1]} jobs)")
        salary_range = df_with_salary['salary_avg'].max() - df_with_salary['salary_avg'].min()
        insights.append(f"**Salary range span**: ${salary_range:,.0f}")
    insights_text = "\n".join(insights)
    
    return stats, skills_plot, salary_skills_plot, salary_dist_plot, display_df, insights_text

def gradio_interface():
    with gr.Blocks(title="AI Job Market Dashboard") as demo:
        gr.Markdown("# 🤖 AI Job Market Dashboard")
        gr.Markdown("Analysis of AI and Machine Learning job opportunities")
        
        stats, skills_plot, salary_skills_plot, salary_dist_plots, display_df, insights = create_dashboard()
        
        gr.Markdown("## 📊 Key Statistics")
        gr.Markdown(stats)
        
        gr.Markdown("## 💼 Top AI Skills in Demand")
        if skills_plot:
            gr.Plot(skills_plot)
        else:
            gr.Markdown("No skills data extracted.")
        
        gr.Markdown("## 💰 Average Salary by Top Skills")
        if salary_skills_plot:
            gr.Plot(salary_skills_plot)
        else:
            gr.Markdown("No salary data for skills.")
        
        gr.Markdown("## 📈 Salary Distribution")
        if salary_dist_plots:
            with gr.Row():
                gr.Plot(salary_dist_plots[0])
                gr.Plot(salary_dist_plots[1])
        else:
            gr.Markdown("No salary data available.")
        
        gr.Markdown("## 📋 Job Details")
        gr.DataFrame(display_df)
        
        gr.Markdown("## 🔍 Key Insights")
        gr.Markdown(insights)
    
    return demo

if __name__ == "__main__":
    gradio_interface().launch(share=True)