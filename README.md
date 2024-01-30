# sql2json-recursive
Specifically designed to transform complex SQL queries into detailed, branched JSON structures. This is particularly useful in scenarios where modern databases, despite their capabilities to generate JSON from SQL directly, fall short in creating intricately branched JSON data. Our tool excels in situations requiring a deep dive into master data, seamlessly branching out across various tables and systems to fetch and organize branch-specific data.

## Getting Started

create virtual Enviroment and install requirements.txt

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Aaditya57/sql2json-recursive.git
   cd sql2json-recusive
   ```
2. **Activate Virtual Enviroment**
    Create a local enviroment to install the packages to run code:
    ```
    python -m venv venv
    ```
    Activate it (for Windows):
    ```
    .\venv\Scripts\activate
    ```
    Activate it (for Mac):
    ```
    source venv/bin/activate
    ```
    Finally, install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. **Configuration**
    You will need to update the .env file with the information of your SQL server, an example one is provided.
    Next you will have to go to queries.yml and write in the queries for the desired tables you want to insert, an example one is provided
    Finally, run generatejson.py
    ```
    python ./generatejson.py
    ```
## Authors

* **Aaditya Ghosalkar** - Student of University of Virginia (https://github.com/Aaditya57)
I am a 3rd year student studying CS at UVA

