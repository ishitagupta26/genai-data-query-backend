GenAI Data Query Backend

This is a mini backend project I built for a GenAI analytics tool assignment. The idea is to let users type natural language queries like “Show total sales” and the system should give back mock insights like it's an AI.

It’s built using Django + Django REST Framework, and deployed live on Render.

Live Project Link

[https://genai-data-query-backend.onrender.com/query/](https://genai-data-query-backend.onrender.com/query/)

Tech Used
- Python 3
- Django 5
- Django REST Framework (DRF)
- SQLite (mock DB)
- Hosted on Render

What This Does
- Accepts natural language queries
- Converts them to mock SQL
- Returns dummy data as if it came from a database
- Has 3 working APIs:
  - `/query` - responds with mock SQL + data
  - `/explain` - explains what the query means
  - `/validate` - checks if the query makes sense

Authentication
All endpoints are protected using Basic Authentication.
Make sure to login using the Django admin credentials you create.  
To create one, run this in your terminal:
```bash
python manage.py createsuperuser
```
You can then log in at `/admin` and use those credentials in Postman or the browser.

How to Run Locally
```bash
git clone https://github.com/ishitagupta26/genai-data-query-backend.git
cd genai-data-query-backend
python -m venv venv
source venv/bin/activate     # Or use venv\Scripts\activate for Windows
pip install -r requirements.txt
python manage.py runserver
```

 API Endpoints
 
`POST /query/`
This one takes a natural language query and responds with some fake SQL and dummy data.
Request:
```json
{
  "query": "Show total sales"
}
```

Response:
```json
{
  "data": [
    {
      "date": "2024-01-01",
      "sales": 1000
    }
  ],
  "sql": "SELECT * FROM sales_data;"
}
```

`POST /explain/`
Just explains what the query is about.
Request:
```json
{
  "query": "List all customers"
}
```

Response:
```json
{
  "explanation": "This query is asking about: 'List all customers'"
}
```

`POST /validate/`
Checks if the query has known keywords (like sales, revenue, customer).
Request:
```json
{
  "query": "Get customer list"
}
```

Response:
```json
{
  "valid": true
}
```

Sample Keywords That Work
To trigger mock responses, try queries containing:

- `sales`
- `revenue`
- `customer`
Everything else just returns a dummy response.

Postman Collection
I’ve added a Postman collection file too that has all 3 API calls already set up.
File: `genai_query_engine.postman_collection.json`  
You can import this in Postman and test easily.

Ishita Gupta  
GitHub: [@ishitagupta26](https://github.com/ishitagupta26)
linkedIn: https://www.linkedin.com/in/ishita-gupta-9a5724226/
Thanks for checking it out!
