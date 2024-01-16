# sql2json-recursive
The program creates a json file of your mysql database using a recursive algorithm

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

