**# README: Running Prolog-Gemini-LangGraph React Agent Notebook in Google Colab**



This README provides a step-by-step guide for new users to run the Jupyter notebook `prolog\_gemini\_langgraph\_react\_agent\_Marktechpost.ipynb` in Google Colab. The notebook demonstrates integrating SWI-Prolog with Google's Gemini AI model using LangGraph for building a reactive agent. 



\## Description

\- \*\*Purpose\*\*: The notebook showcases logical reasoning with Prolog (via PySWIP) combined with AI capabilities from Gemini (via LangChain). It defines a knowledge base for family trees, performs queries, and runs demos for analysis and interaction.

\- \*\*Key Components\*\*:

&nbsp; - Prolog knowledge base for family relationships and math operations.

&nbsp; - LangGraph-based agent for handling queries.

&nbsp; - Interactive sessions and complex reasoning examples.

\- \*\*Requirements\*\*: Basic familiarity with Python and Jupyter notebooks is helpful, but not required.



\## Prerequisites

1\. \*\*Google Account\*\*: You need a Google account to access Google Colab.

2\. \*\*Google Gemini API Key\*\*:

&nbsp;  - Sign up for Google AI Studio at \[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).

&nbsp;  - Generate a free API key for the Gemini model (e.g., "gemini-1.5-flash").

&nbsp;  - Note: The API key is free for limited usage, but check Google's terms for any restrictions.

3\. \*\*Internet Connection\*\*: Colab runs in the cloud, so a stable connection is needed.

4\. \*\*No Local Setup Required\*\*: Everything runs in the browser via Colab—no need to install software on your machine.



\## Step-by-Step Guide to Run the Notebook in Google Colab



\### Step 1: Access Google Colab

\- Open your web browser and go to \[https://colab.research.google.com/](https://colab.research.google.com/).

\- Sign in with your Google account if prompted.



\### Step 2: Upload or Open the Notebook

\- In Colab, click \*\*File > Open notebook\*\*.

\- Select the \*\*Upload\*\* tab.

\- Drag and drop the `prolog\_gemini\_langgraph\_react\_agent\_Marktechpost.ipynb` file or click \*\*Browse\*\* to select it from your computer.

\- Once uploaded, the notebook will open in the Colab editor.



\### Step 3: Set Up the Runtime

\- Colab provides a free GPU/CPU runtime, but this notebook doesn't require heavy computation, so the default is fine.

\- (Optional) To ensure a clean environment: Click \*\*Runtime > Restart runtime\*\* (or Ctrl+M .) to reset the session.



\### Step 4: Install Dependencies

\- The first cell installs SWI-Prolog and Python packages. Run it by:

&nbsp; - Clicking the play button (▶) next to the cell, or

&nbsp; - Selecting the cell and pressing \*\*Shift + Enter\*\*.

\- Code in the cell:

&nbsp; ```

&nbsp; !apt-get install swi-prolog -y

&nbsp; !pip install pyswip langchain-google-genai langgraph langchain-core

&nbsp; ```

\- This may take 1-2 minutes. You'll see output logs in the cell below the code.

\- If you encounter permission issues, Colab might prompt you to confirm running as root—approve it.



\### Step 5: Set Your Google Gemini API Key

\- In the third cell (or wherever `GOOGLE\_API\_KEY` is defined), replace `"YOUR\_GEMINI\_API\_KEY\_HERE"` with your actual API key.

\- Example:

&nbsp; ```

&nbsp; GOOGLE\_API\_KEY = "your\_actual\_api\_key\_here"

&nbsp; os.environ\["GOOGLE\_API\_KEY"] = GOOGLE\_API\_KEY



&nbsp; llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

&nbsp; ```

\- Run this cell (Shift + Enter).

\- \*\*Security Note\*\*: Never share your notebook with the API key visible. Use Colab's "Share" feature carefully or revoke the key if needed.



\### Step 6: Run the Remaining Cells

\- Proceed cell by cell:

&nbsp; - Cell 4: Defines the `AdvancedPrologInterface` class and loads the Prolog knowledge base (family facts, rules, etc.).

&nbsp; - Cell 5: Initializes the Prolog interface and defines tools (`family\_relationships`, `mathematical\_operations`, `advanced\_queries`).

&nbsp; - Cell 6: Binds tools to the agent and defines demo functions (`run\_family\_analysis`, `demonstrate\_complex\_reasoning`, `interactive\_prolog\_session`).

&nbsp; - Cell 7: Defines the `main` function, direct query tests, and math capabilities demo.

\- Run each cell sequentially. If a cell depends on previous ones (e.g., variables like `prolog\_interface`), ensure prior cells have run successfully.

\- The last cell runs `main()` and `show\_mathematical\_capabilities()`, producing outputs like family analyses and factorial calculations.



\### Step 7: Interact with the Notebook

\- After running all cells, you can explore:

&nbsp; - \*\*Direct Queries\*\*: Outputs family relationships and math results.

&nbsp; - \*\*Family Analysis\*\*: Runs predefined queries (e.g., "Who are John and Mary's children?").

&nbsp; - \*\*Complex Reasoning\*\*: Analyzes the full family tree in one go.

&nbsp; - \*\*Mathematical Demos\*\*: Computes factorials.

\- (Optional) Modify the knowledge base in Cell 4 by adding your own Prolog rules (e.g., more family members) and re-run.



\### Step 8: Save Your Work

\- Click \*\*File > Save a copy in Drive\*\* to save the notebook to your Google Drive.

\- Download the notebook: \*\*File > Download > Download .ipynb\*\*.



\## Expected Output

\- Installation logs from the first cell.

\- Prolog query results in JSON format (e.g., family members, factorials).

\- Agent responses to queries, like:

&nbsp; - "John and Mary's children are alice and bob."

&nbsp; - "The factorial of 6 is 720."

\- If everything works, you'll see a completion message: "Tutorial completed successfully!" with key achievements.



\## Troubleshooting

\- \*\*API Key Error\*\*: If you see "Invalid API Key," double-check your key in AI Studio. Regenerate if needed.

\- \*\*Prolog Installation Issues\*\*: If `!apt-get install swi-prolog` fails, restart the runtime and try again. Colab sometimes has transient errors.

\- \*\*Module Not Found\*\*: Re-run the pip install cell if libraries like `pyswip` or `langchain` are missing.

\- \*\*Query Failures\*\*: Prolog queries are case-sensitive and must match the knowledge base (e.g., names like "john" are lowercase).

\- \*\*Runtime Disconnect\*\*: Colab sessions timeout after ~20 minutes of inactivity. Reconnect via \*\*Runtime > Reconnect\*\*.

\- \*\*Errors in Outputs\*\*: The notebook handles errors gracefully (e.g., "No solutions found" or "Operation not supported"). If stuck, check the console for details.

\- \*\*Gemini Model Limits\*\*: If queries fail due to rate limits, wait a few minutes or reduce query complexity.

\- \*\*Need Help?\*\*: Search for error messages on Stack Overflow or Google Colab forums. For Prolog-specific issues, refer to SWI-Prolog docs: \[https://www.swi-prolog.org/](https://www.swi-prolog.org/).



\## Additional Tips for New Users

\- \*\*Colab Shortcuts\*\*:

&nbsp; - Add a new cell: Ctrl + M, B (below) or A (above).

&nbsp; - Run all cells: \*\*Runtime > Run all\*\*.

&nbsp; - Clear outputs: \*\*Edit > Clear all outputs\*\*.

\- \*\*Extend the Notebook\*\*: Add your own Prolog facts (e.g., `parent(your\_name, spouse, child)`) to the `\_load\_knowledge\_base` method and experiment.

\- \*\*Performance\*\*: For larger knowledge bases, Colab's free tier is sufficient, but upgrade to Colab Pro for more resources if needed.

\- \*\*Date Note\*\*: This guide is based on the notebook as of September 25, 2025. Library versions may change—update pip installs if deprecated.





