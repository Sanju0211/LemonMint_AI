# AI Job Market Analysis

![AI Job Market Banner](https://via.placeholder.com/800x200/00BFFF/FFFFFF?text=AI+Job+Market+Analysis) <!-- Replace with actual banner if desired -->

## Overview

This project provides an end-to-end solution for analyzing AI job listings. It includes a web scraper to collect job data from [AIJobs.ai](https://aijobs.ai) and an interactive dashboard to visualize job trends, salaries, and in-demand skills. The scraper generates a CSV file (`job_data.csv`), which the dashboard uses to display insights like salary distributions, top skills, and job details. The dashboard is built with [Gradio](https://gradio.app) for easy access in Google Colab, making it beginner-friendly and cloud-based.

### Project Goals
- **Scrape AI Jobs**: Extract job titles, descriptions, and salaries from AIJobs.ai.
- **Analyze Trends**: Visualize key metrics (e.g., salary ranges, skill demands).
- **Interactive Dashboard**: Explore data with charts and tables.
- **Accessible Setup**: Run everything in Google Colab without local dependencies.

### Key Technologies
- **Python**: Core programming language (3.10+ compatible).
- **Libraries**: `pandas`, `requests`, `beautifulsoup4`, `gradio`, `plotly`, `numpy`.
- **Platform**: Google Colab for cloud-based execution.
- **Data Source**: [AIJobs.ai](https://aijobs.ai/united-states) or sample CSV.

## Repository Structure

| File/Folder | Description |
|-------------|-------------|
| `ai-job-scraper.ipynb` | Jupyter Notebook to scrape job data from AIJobs.ai and save to `data/job_data.csv`. |
| `ai-job-dashboard-gradio.py` | Gradio dashboard to visualize job data (stats, charts, tables). |
| `generate_sample_job_data.py` | Script to create a sample `job_data.csv` with 20 AI job entries. |
| `data/ai_job_data.csv` | Sample CSV with real job data (fallback if scraper fails). |
| `data/` | Folder to store output CSV (`job_data.csv`). |

## Prerequisites

- **Google Account**: For accessing [Google Colab](https://colab.research.google.com/).
- **Internet Connection**: For scraping and running Colab.
- **Optional**: Basic Python knowledge for troubleshooting.
- **No Local Setup Needed**: Everything runs in Colab’s cloud environment.

## Step-by-Step Execution in Google Colab

### Step 1: Clone or Download the Repository
1. **Access the Repo**:
   - Clone: `git clone https://github.com/Sanju0211/AI_Job_Market_Analysis.git` (requires Git in Colab).
   - OR Download: Visit [github.com/Sanju0211/AI_Job_Market_Analysis](https://github.com/Sanju0211/AI_Job_Market_Analysis), click **Code > Download ZIP**, and extract.
2. **Open Colab**:
   - Go to [colab.research.google.com](https://colab.research.google.com/).
   - Create a new notebook: **File > New notebook**.
   - Rename it to `AI_Job_Analysis.ipynb`.

### Step 2: Upload Project Files
1. In Colab, click the **Files** icon (left sidebar, folder symbol).
2. Upload all files:
   - `ai-job-scraper.ipynb`
   - `ai-job-dashboard-gradio.py`
   - `generate_sample_job_data.py`
   - `data/ai_job_data.csv`
3. Create a `data/` folder: Run in a cell:
   ```
   !mkdir data
   ```
4. Move `ai_job_data.csv` to `data/`:
   ```
   !mv ai_job_data.csv data/
   ```
   Your structure should be:
   ```
   - ai-job-scraper.ipynb
   - ai-job-dashboard-gradio.py
   - generate_sample_job_data.py
   - data/
     - ai_job_data.csv
   ```

### Step 3: Install Dependencies
Run this in a Colab cell to install required libraries:
```python
!pip install pandas requests beautifulsoup4 gradio plotly numpy --quiet
```
- **Time**: ~1 minute.
- **Note**: `--quiet` reduces output; remove for debugging.

### Step 4: Scrape Job Data
1. **Open Scraper Notebook**:
   - Double-click `ai-job-scraper.ipynb` in Colab’s Files panel.
2. **Run All Cells**:
   - Click **Runtime > Run all** (or Ctrl+F9).
   - **What it does**:
     - Scrapes job listings from [AIJobs.ai/united-states](https://aijobs.ai/united-states).
     - Extracts job titles, descriptions, salaries.
     - Saves to `data/job_data.csv`.
   - **Output**: Displays job data; check `df.head(10)` for ~26 jobs.
3. **Verify**:
   - Refresh Files panel; open `data/job_data.csv`.
   - Columns: `Job Title`, `Job Description`, `Salary Range:`.
4. **If Scraping Fails** (e.g., HTTP 403/429, site changes):
   - Use the sample data (Step 5) or debug:
     - Check site HTML for updated selectors (e.g., `.post-main-title2`, `.salery h2`).
     - Add delays: Insert `import time; time.sleep(1)` before `requests.get`.

**Time**: ~1–2 minutes.

### Step 5: Use Sample Data (Fallback or for More Entries)
If the scraper fails or you want richer data:
1. Run `generate_sample_job_data.py` in a cell:
   ```python
   !python generate_sample_job_data.py
   ```
   - Creates `data/job_data.csv` with 20 diverse AI jobs (titles, descriptions with skills like Python/TensorFlow, salaries $85,000–$220,000).
2. **Verify**: Check `data/job_data.csv` in Files (20 rows).
3. **Optional: Merge with Real Data**:
   To combine sample data with `ai_job_data.csv`:
   ```python
   import pandas as pd
   real_df = pd.read_csv('data/ai_job_data.csv')
   real_df = real_df[['job_title', 'job_description', 'salary_min']].rename(
       columns={'job_title': 'Job Title', 'job_description': 'Job Description', 'salary_min': 'Salary Range:'}
   )
   real_df['Salary Range:'] = real_df['Salary Range:'].apply(lambda x: f"${x:,.0f} - ${x:,.0f}")
   sample_df = pd.read_csv('data/job_data.csv')
   combined_df = pd.concat([sample_df, real_df[['Job Title', 'Job Description', 'Salary Range:']]], ignore_index=True)
   combined_df.to_csv('data/job_data.csv', index=False)
   print("Combined job_data.csv created")
   ```

### Step 6: Run the Gradio Dashboard
1. **Run the Dashboard**:
   In a Colab cell:
   ```python
   !python ai-job-dashboard-gradio.py
   ```
   - **What it does**:
     - Loads `data/job_data.csv`.
     - Displays stats (total jobs, median/mean salary).
     - Shows charts: skills bar, salary-by-skill, salary distribution (histogram, box plot).
     - Lists jobs in a table with titles, salaries, and skills.
     - Provides insights (e.g., highest/lowest paying roles).
   - **Output**: A public URL (e.g., `https://*.gradio.app`) appears. Click to view.
2. **Interact**:
   - Explore visualizations in the browser.
   - **Time**: ~10–30 seconds to start.
3. **If URL Fails**:
   - Retry or use `share=False` in `ai-job-dashboard-gradio.py` (edit last line to `.launch(share=False)` for local view).

### Step 7: Save and Cleanup
- **Save Data**: Download `data/job_data.csv` (right-click in Files > Download).
- **Stop Dashboard**: Stop the cell or run `!pkill python` to terminate.
- **Colab Timeout**: Sessions reset after ~20 minutes inactivity. Re-upload files if needed.

## Troubleshooting

- **Scraper Errors**:
  - **HTTP 403/429**: Add `time.sleep(1)` in `ai-job-scraper.ipynb` or use sample data.
  - **Selector Issues**: Inspect [AIJobs.ai](https://aijobs.ai) HTML; update `.post-main-title2` or `.salery h2`.
  - **No Data**: Run `generate_sample_job_data.py`.
- **Dashboard Errors**:
  - **File Not Found**: Ensure `data/job_data.csv` exists.
  - **Empty Charts**: Verify CSV has valid `Salary Range:` (e.g., "$100,000 - $200,000").
  - **Gradio URL Fails**: Retry or use `share=False`.
- **Dependencies**: If errors, reinstall: `!pip install --force-reinstall pandas gradio`.
- **More Data**: Edit `generate_sample_job_data.py` to add entries or scrape more pages in `ai-job-scraper.ipynb`:
  ```python
  job_links = []
  for page in range(1, 10):
      url = f"https://aijobs.ai/united-states?page={page}"
      res = requests.get(url)
      soup = BeautifulSoup(res.text, "html.parser")
      a_tags = soup.select('a[href*="/job/"]')
      job_links.extend(urljoin(url, tag.get("href")) for tag in a_tags)
  ```

## Contributing

1. Fork the repo.
2. Create a branch: `git checkout -b feature/add-filter`.
3. Commit: `git commit -m 'Add salary filter to dashboard'`.
4. Push: `git push origin feature/add-filter`.
5. Open a Pull Request.

Ideas: Add dashboard filters (e.g., salary slider), expand scraper to other job boards, or enhance visualizations.

## License

MIT License - See [LICENSE](LICENSE) for details.

## Contact

- **Author**: Sanju0211
- **GitHub**: [Sanju0211/AI_Job_Market_Analysis](https://github.com/Sanju0211/AI_Job_Market_Analysis)
- **Issues**: Report bugs or suggest features via GitHub Issues.
- **Email**: [your.email@example.com](mailto:your.email@example.com) (replace with your contact).

Happy analyzing! 🚀 Explore the AI job market with ease.

*Last Updated: September 26, 2025*