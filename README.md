# 📊 InsightFlow-AI

> **Ask a question. Get a dashboard. No SQL. No BI tools. Just insights.**

InsightFlow-AI is a conversational AI data analytics tool that converts **natural language questions into interactive dashboards** - automatically generating SQL queries, charts, and business insights from any uploaded CSV dataset.

Upload your data → Ask a question → Instantly get visual analytics.

Built for hackathons and rapid data exploration using **Google Gemini, Streamlit, Pandas, SQLite, and Plotly.**

---

# 🎬 Demo

Example interaction:

```
User:
Show total views by category

System:
→ Generates SQL
→ Executes query on dataset
→ Chooses best chart type
→ Builds dashboard
→ Generates AI insights
```

Follow-up queries work conversationally:

```
User: Show views by category
User: Only for 2024

System resolves to:
Show views by category for 2024
```

No manual filtering required.

---

# ✨ Features

|           Feature            |                   Description                     |
|------------------------------|---------------------------------------------------|
| 💬 Natural language queries  | Ask questions about your dataset in plain English |
| 🤖 AI-generated SQL          | Gemini converts questions into SQLite queries     |
| 📊 Smart chart selection     | Automatically chooses bar, line, pie, or scatter  |
| ⚡ Interactive Plotly charts | Zoom, hover, inspect, export                      |
| 🧠 AI business insights      | Gemini generates 3–5 bullet insights from results |
| 🔄 Conversational follow-ups | Context-aware query rewriting                     |
| 📁 Upload any CSV            | Works with arbitrary datasets                     |
| 💡 Dynamic example queries   | AI suggests relevant questions for each dataset   |
| 🧠 Schema-aware reasoning    | Automatically extracts numeric/categorical columns|

---

# 🏗 Architecture

```
User Query
     │
     ▼
┌──────────────────────┐
│ Followup Resolver    │
│ followup_resolver.py │
│ (Gemini)             │
└──────────┬───────────┘
           │ Standalone query
           ▼
┌──────────────────────┐
│ SQL Generator        │
│ sql_generator.py     │
│ (Gemini)             │
└──────────┬───────────┘
           │ SQL Query
           ▼
┌──────────────────────┐
│ Query Executor       │
│ query_executor.py    │
│ SQLite + Pandas      │
└──────────┬───────────┘
           │ DataFrame
           ▼
┌──────────────────────┐
│ Chart Selector       │
│ chart_selector.py    │
│ (Gemini reasoning)   │
└──────────┬───────────┘
           │ Chart type
           ▼
┌──────────────────────┐
│ Chart Renderer       │
│ chart_renderer.py    │
│ Plotly builder       │
└──────────┬───────────┘
           │
           ├─────────────► AI Insights Generator
           │               insights_generator.py
           │               (Gemini)
           ▼
      Streamlit UI
```

---

# 📁 Project Structure

```
InsightFlow-AI/
│
├── backend/
│   ├── gemini_client.py
│   ├── sql_generator.py
│   ├── query_executor.py
│   ├── chart_selector.py
│   ├── chart_renderer.py
│   ├── insights_generator.py
│   ├── followup_resolver.py
│   └── example_generator.py
│
├── frontend/
│   ├── app.py
│   └── style.css
│
├── utils/
│   ├── schema_loader.py
│   └── css_loader.py
│
├── prompts/
│   ├── sql_prompt.txt
│   ├── chart_prompt.txt
│   ├── insight_prompt.txt
│   ├── followup_prompt.txt
│   └── examples_prompt.txt
│
├── requirements.txt
├── .env
└── README.md
```

---

# 🚀 Getting Started

## Prerequisites

- Python **3.10+**
- Google **Gemini API key**

Get your key here:

https://aistudio.google.com/app/api-keys

---

## Installation

```bash
git clone https://github.com/openvaibhav/InsightFlow-AI.git

cd InsightFlow-AI

python -m venv venv
# Bash:
source venv/bin/activate
# Fish:
source venv/bin/activate.fish
# Windows:
# venv\Scripts\activate

pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## Run the app

```
streamlit run frontend/app.py
```

Then open:

```
http://localhost:8501
```

---

# 🧪 Usage

1️⃣ Upload a CSV dataset  
2️⃣ Ask a question about the data  
3️⃣ The system automatically:

- Generates SQL
- Runs query
- Picks chart
- Renders dashboard
- Produces insights

4️⃣ Ask follow-up questions conversationally

---

# 💡 Example Queries

Works for many datasets.

Examples:

```
Show total views by category
Which category has the highest engagement
Top 10 videos by views
Compare views and likes
Show monthly views trend
Which region has the highest revenue
Show average rating by product category
Compare revenue and profit
```

Dynamic examples are generated based on detected:

- numeric columns
- categorical columns
- date columns

---

# 🧠 Key Components

### Schema Loader

Automatically extracts:

- column names
- data types
- numeric columns
- categorical columns

Used to guide LLM SQL generation.

---

### SQL Generator

Gemini converts natural language into **SQLite-compatible SQL queries**.

Safety features:

- prevents write operations
- enforces schema usage
- validates query output

---

### Query Executor

Runs SQL against a **temporary in-memory SQLite database** built from the uploaded DataFrame.

---

### Chart Selector

AI decides which visualization fits the result:

|     Data Pattern    |  Chart  |
|---------------------|---------|
| Category vs value   | Bar     |
| Time series         | Line    |
| Parts of whole      | Pie     |
| Numeric correlation | Scatter |

---

### Insights Generator

Gemini analyzes result tables and produces concise business insights.

Example:

```
• Gaming category generates the highest total views
• Engagement peaks during June and July
• Sentiment scores show strong positive correlation with likes
```

---

# 🛠 Tech Stack

|      Layer      |     Technology     |
|-----------------|--------------------|
| UI              | Streamlit          |
| LLM             | Google Gemini      |
| Charts          | Plotly             |
| Data processing | Pandas             |
| Query engine    | SQLite (in-memory) |
| Environment     | Python 3.10+       |

---

# 📦 Requirements

```
streamlit
pandas
plotly
google-generativeai
python-dotenv
numpy
statsmodels
pyarrow
```

---

# ⚠ Known Limitations

- SQL generation depends on schema clarity
- Very large datasets (>500k rows) may slow execution
- Gemini rate limits apply on free tier
- Some ambiguous queries may generate suboptimal charts

---

# 🚀 Future Improvements

Potential upgrades:

- Multi-dataset joins
- Dashboard export
- Chart editing
- LLM self-correction loops
- SQL execution sandboxing
- Live database connections

---

# 🤝 Contributing

Pull requests welcome.

Steps:

```
1. Fork repo
2. Create branch
3. Implement feature
4. Submit PR
```

---

# 📄 License

MIT License

---

# 🧑‍💻 Author

Built for hackathon with questionable sleep and too much caffeine ☕.

---

<div align="center">

**InsightFlow-AI**

Ask your data anything.

</div>