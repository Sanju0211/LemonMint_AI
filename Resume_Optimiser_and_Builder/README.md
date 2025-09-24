**# Resume Optimizer README**



\## Overview

This project is a Resume Optimizer built with Python, Google Gemini API, and Gradio. It allows you to upload a resume (.md or .txt), paste a job description, optimize the resume for ATS (Applicant Tracking Systems) compatibility, and export it as a PDF.



The notebook (`resumebuilder.ipynb`) runs entirely in Google Collab, a free cloud-based Jupyter notebook environment. No local installation is needed.



\- \*\*Dependencies\*\*: gradio, google-generative Ai, markdown, weasyprint

\- \*\*API Required\*\*: Google Gemini API key (free tier available)



\## Prerequisites

\- A Google account (to access Collab).

\- A Google Gemini API key (free for basic use):

&nbsp; 1. Go to \[Google AI Studio](https://aistudio.google.com/app/apikey).

&nbsp; 2. Sign in with your Google account.

&nbsp; 3. Click "Create API key".

&nbsp; 4. Copy the key.

\- Internet connection.

\- A resume file in `.md` or `.txt` format.

\- A job description text.





\## Step-by-Step Guide to Run in Google Collab.



\### Step 1: Open Google Collab

1\. Go to \[colab.research.google.com](https://colab.research.google.com).

2\. Sign in with your Google account if prompted.

3\. Click \*\*"New notebook"\*\* (or "File" → "New notebook") to create a blank notebook.



\### Step 2: Upload the Notebook File

1\. In the Collab notebook, click the \*\*📁 Files icon\*\* on the left sidebar.

2\. Click \*\*"Upload to session storage"\*\* (folder with arrow icon).

3\. Select your `resumebuilder.ipynb` file from your computer.

4\. Once uploaded, double-click the file in the Files panel to open it in the editor.



\### Step 3: Install Dependencies

1\. In the notebook, find Cell 1 (labeled "# Cell 1: Install Dependencies").

2\. Click the \*\*play button\*\* (▶) next to Cell 1 to run it.

3\. Expected Output: A message like "✅ Dependencies installed!" and some installation logs. This may take 1-2 minutes.



\### Step 4: Configure the Gemini API Key

1\. Run Cell 2 (labeled "# Cell 2: Import Libraries and Setup").

2\. When prompted, paste your Gemini API key (from Prerequisites) and press Enter.

&nbsp;  - If you don't have a key, type `test` to proceed (UI will launch, but optimization won't work).

3\. Expected Output: "🎉 Gemini API configured!" or "⚠️ Using placeholder 'test' key...". If there's an error, check your key and try again.



\### Step 5: Define Processing Functions

1\. Run Cell 3 (labeled "# Cell 3: Define Functions").

2\. Expected Output: "✅ Functions defined successfully!" with a list of functions and key fixes.



\### Step 6: Launch the Gradio UI

1\. Run Cell 4 (labeled "# Cell 4: Create and Launch Gradio UI").

2\. Expected Output: A public URL (e.g., "https://xxx.gradio.live") and "✅ Success! Gradio interface launched!". The URL is valid for ~72 hours.



\### Step 7: Use the Interface

1\. Click the public URL from Cell 4's output to open the UI in a new browser tab.

2\. \*\*Upload Resume\*\*: Click "Upload Your Resume" and select your `.md` or `.txt` file.

3\. \*\*Paste Job Description\*\*: Enter the job posting text in the textbox.

4\. \*\*Optimize\*\*: Click "Optimize My Resume".

5\. Expected: The "Optimized Resume" section shows the tailored resume; "Actionable Suggestions" lists improvements.

6\. \*\*Edit and Export\*\*:

&nbsp;  - Edit in the "Editable Resume" textbox if needed.

&nbsp;  - Click "Export to PDF" – a success message appears with the file path (e.g., `/content/optimized\_resume\_XXXXXX.pdf`).



\### Step 8: Download the PDF

1\. Back in Collab, click the \*\*📁 Files icon\*\* on the left sidebar.

2\. Find the PDF in the `/content/` folder (e.g., `optimized\_resume\_XXXXXX.pdf`).

3\. Right-click the file → "Download".

4\. Expected: The PDF downloads to your computer.



\## Sample Data

\- \*\*Sample Resume (resume\_new.md)\*\*:

&nbsp; ```

&nbsp; # Shaw Talebi  

&nbsp; \*\*Email\*\*: \[shawhintalebi@gmail.com](mailto:shawhintalebi@gmail.com)  

&nbsp; \*\*Homepage\*\*: \[shawhintalebi.com](https://shawhintalebi.com/) | \*\*LinkedIn\*\*: \[shawhintalebi](https://www.linkedin.com/in/shawhintalebi/)  



&nbsp; ---



&nbsp; ## Education  

&nbsp; \*\*The University of Texas at Dallas\*\*  

&nbsp; - PhD, Physics - \*May 2022\*  

&nbsp; - M.S., Physics - \*December 2019\*  

&nbsp; - B.S., Physics - \*May 2017\*  



&nbsp; ## Technical Skills  

&nbsp; - \*\*Programming Languages\*\*: Python, SQL, Julia  

&nbsp; - \*\*Tools\*\*: AWS (SageMaker), Snowflake, GitHub, Tableau  

&nbsp; - \*\*Certifications\*\*: AWS Cloud Practitioner Essentials (AWS), Data Structure \& Algorithms (Udemy), Tableau (Udemy)  



&nbsp; ## Work Experience



&nbsp; ### \*\*Technical Writer \& Data Science Consultant\*\*  

&nbsp; \*\*Shawhin Talebi Ventures LLC\*\* | Plano, Texas \*(December 2020 - Present)\*  

&nbsp; - Developed comprehensive technical documentation for data science projects, including integration guides and API references, ensuring clarity for technical users.  

&nbsp; - Implemented data pipelines leveraging Python and SQL, driving insights and enhancing data quality for decision-making processes.  



&nbsp; ### \*\*Data Scientist\*\*  

&nbsp; \*\*Toyota Financial Services\*\* | Plano, Texas \*(June 2022 - July 2023)\*  

&nbsp; - Enhanced the credit risk model's accuracy for over 70% of accounts, writing model monitoring scripts to prevent future failures.  

&nbsp; - Redeveloped loan originations model, achieving a 50% performance improvement and realizing $2.5 million in value for stakeholders.  



&nbsp; ### \*\*Research Assistant\*\*  

&nbsp; \*\*The University of Texas at Dallas (Department of Physics)\*\* | Richardson, Texas \*(December 2018 - May 2022)\*  

&nbsp; - Authored open-source methodology documentation to improve EEG band discovery, facilitating enhanced data analysis and research reproducibility.  

&nbsp; - Trained and validated machine learning models to estimate particulate matter concentrations, achieving a high fidelity (r² = 0.91) and documenting methodologies for future reference.  



&nbsp; ## Awards and Honors  

&nbsp; - \*\*2021 Friends of BrainHealth Visionary New Scientist Award\*\* — Finalist \*(September 2021)\*  

&nbsp; - \*\*2nd Annual Weeks of Welcome Poster Competition\*\* — 3rd Place Winner \*(August 2019)\*  



&nbsp; ---



&nbsp; ## Publications  



&nbsp; 1. Talebi S., Lary D.J., Wijeratne L. OH., and Lary, T. \*Modeling Autonomic Pupillary Responses from External Stimuli Using Machine Learning\* (2019).  

&nbsp; 2. Talebi, S. et al. \*Data-Driven EEG Band Discovery with Decision Trees\*. Sensors 2022, 22(8), 3048.  



&nbsp; ---



&nbsp; \*\*References and additional information available upon request.\*\*

&nbsp; ```



\- \*\*Sample Job Description\*\*:

&nbsp; ```

&nbsp; Senior Data Scientist - Tech Corp

&nbsp; Plano, TX | Full-time



&nbsp; We are seeking a Senior Data Scientist with 3+ years of experience in machine learning and data engineering. 

&nbsp; Required skills: Python, SQL, AWS (SageMaker), Snowflake, Tableau. 

&nbsp; Responsibilities: Build ML models for credit risk assessment, develop data pipelines, 

&nbsp; create dashboards for stakeholders, and collaborate with cross-functional teams.



&nbsp; Preferred: PhD in quantitative field, publications in ML/data science, experience with 

&nbsp; financial services or automotive industry.

&nbsp; ```



\- \*\*Expected Optimized Resume\*\*: A tailored Markdown version emphasizing matching skills.



\## Troubleshooting

\- \*\*No Output in UI\*\*: Ensure API key is valid (not 'test'). Check Collab output for "Debug" messages or errors.

\- \*\*"Nothing to export!"\*\*: Optimize the resume first; the editable textbox should populate automatically.

\- \*\*Blank PDF\*\*: Ensure the editable textbox has content before exporting.

\- \*\*UI Not Loading\*\*: Use the public URL in a new tab or restart runtime.

\- \*\*API Error\*\*: Check your Gemini key quota; regenerate if needed.

\- \*\*Dependencies Fail\*\*: Re-run Cell 1; if errors, restart runtime.

\- \*\*File Not Found\*\*: PDFs are in `/content/`; refresh the Files panel.



If issues persist, check the Collab output for errors or search the error message on Stack Overflow.



\## Additional Notes

\- \*\*ATS-Friendly Tips\*\*: The optimized resume uses simple Markdown (headings, bullets) to pass ATS scans. Avoid tables or images in the final PDF.

\- \*\*Privacy\*\*: Uploads and processing occur in your Collab session; no data is shared externally except API calls to Gemini.

\- \*\*Limitations\*\*: Free Gemini API has usage quotas; upgrade for heavy use.

\- \*\*Customization\*\*: Edit Cell 3 for different Gemini models or prompt changes.





