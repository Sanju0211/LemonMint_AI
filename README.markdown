# SQLdb_with_smolAgents

This repository contains a Python project that integrates a PostgreSQL database (using the Chinook sample database) with the `smolagents` library to create an agent-based SQL query system. The project allows an agent to execute SQL queries on the `chinook` database and retrieve results, leveraging the `CodeAgent` and model classes from `smolagents`.

## Overview

The project uses a Jupyter notebook (`sql_db.ipynb`) to demonstrate how to:

- Connect to a PostgreSQL database.
- Set up a `smolagents` CodeAgent to run SQL queries.
- Retrieve and display results (e.g., distinct genres from the `genre` table).

## Prerequisites

- **Operating System:** Ubuntu (tested on WSL2).
- **Python:** Version 3.10 or later.
- **PostgreSQL:** Version 14 or later.

## Installation

### 1. Set Up the Virtual Environment

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

Install the required Python packages using pip. Create a `requirements.txt` file with the following content and run:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:

```
smolagents==1.21.3
psycopg2-binary
sqlalchemy
litellm
jupyter
huggingface-hub>=0.31.2
jinja2>=3.1.4
pillow>=10.0.1
python-dotenv
requests>=2.32.3
rich>=13.9.4
tqdm>=4.42.1
hf-xet>=1.1.3
filelock
fsspec>=2023.5.0
```

### 3. Install and Configure PostgreSQL

- Install PostgreSQL on Ubuntu:

  ```bash
  sudo apt update
  sudo apt install postgresql postgresql-contrib
  ```
- Start and enable the PostgreSQL service:

  ```bash
  sudo service postgresql start
  sudo systemctl enable postgresql
  ```
- Set a password for the `postgres` user:

  ```bash
  sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'password';"
  ```
- Adjust authentication in `/etc/postgresql/14/main/pg_hba.conf`:
  - Change `local all postgres peer` to `local all postgres md5`.
  - Change `local all all peer` to `local all all md5`.
  - Restart PostgreSQL:

    ```bash
    sudo service postgresql restart
    ```

### 4. Set Up the Chinook Database

- Create the `chinook` database:

  ```bash
  sudo -u postgres createdb chinook
  ```
- Download and import the Chinook sample data:

  ```bash
  wget https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql
  psql -U postgres -d chinook -f Chinook_PostgreSql.sql -W
  ```
  - Enter `password` when prompted.

## Usage

1. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

2. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

   - Open `sql_db.ipynb` in your browser.

3. Run the notebook cells:

   - Ensure the `db_uri` is set to:

     ```
     db_uri = "postgresql+psycopg2://postgres:password@localhost:5432/chinook"
     ```
   - Execute cells to connect to the database and run the agent (e.g., `agent.run("List distinct genres?")`).

## Project Structure

- `sql_db.ipynb`: Main Jupyter notebook with database connection and agent logic.
- `venv/`: Virtual environment directory.
- `Chinook_PostgreSql.sql`: SQL script for Chinook database setup.
- `requirements.txt`: List of Python dependencies.

## Troubleshooting

- **Connection Errors:** Ensure PostgreSQL is running (`sudo service postgresql status`) and the `pg_hba.conf` changes are applied.
- **ModuleNotFoundError:** Verify all dependencies are installed via `pip list`.
- **Import Errors:** Check `smolagents` version and available imports with `python -c "import smolagents; print(dir(smolagents))"`.

## Contributing

Fork the repository, create a branch, and submit a pull request. Ensure changes are tested with the Chinook database setup.

## License

\[Specify license, e.g., MIT\] - Add a `LICENSE` file if applicable.