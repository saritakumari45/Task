📌 Task Project
📝 Overview
Task is a Python-based project designed to fetch research papers from PubMed using a query-based search.
It utilizes Poetry for dependency management and follows a clean modular structure.

🚀 Features
✅ Fetches research papers from PubMed
✅ Uses Poetry for package and environment management
✅ Modular and scalable code structure
✅ Simple CLI usage

📂 Project Structure

  📂 Task/
  ├── 📜 fetch_papers.py  # Script to fetch research papers
  ├── 📜 main.py          # Main entry point
  ├── 📜 pyproject.toml   # Poetry configuration
  ├── 📜 poetry.lock      # Lock file for dependencies
  ├── 📂 pubmed/          # Directory for fetched papers
  └── 📜 README.md        # Project documentation
  ⚙️ Installation
  
1️⃣ Clone the Repository

  git clone https://github.com/saritakumari45/Task.git
  cd Task
2️⃣ Install Poetry (if not installed)
   Check if Poetry is installed:
  
  poetry --version
  If not, install it:

 curl -sSL https://install.python-poetry.org | python3 -
3️⃣ Install Dependencies
  poetry install

4️⃣ Activate the Virtual Environment
  poetry shell
  
📌 Usage
  Run the script to fetch papers using a query:

python fetch_papers.py "machine learning"
This will retrieve research papers related to Machine Learning from PubMed.

🛠️ Technologies Used
Python 3.12 🐍
Poetry 📦
PubMed API 🔍
🛡️ License
This project is licensed under the MIT License.
