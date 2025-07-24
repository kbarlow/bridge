# 🌉 Bridge DSL

Bridge is a simple, human-readable language designed to express business logic and data questions — without writing SQL. It's an abstraction layer that translates intent into structured queries using a configurable domain vocabulary.

---

## 📦 Project Structure

```
bridge/
├── bridge_dsl/
│   ├── parser.py          ← Parses Bridge DSL into structured logic (AST)
│   ├── compiler.py        ← Compiles AST + config into SQL
│   ├── config.py          ← Loads bridgeconfig.yml mappings
├── examples/
│   └── customer_churn.bridge
├── bridgeconfig.yml       ← Maps user-friendly terms to SQL expressions
├── run.py                 ← Entry point for executing Bridge DSL
├── README.md              ← You're here
├── MANIFESTO.md           ← The vision
```

---

## 🧠 How It Works

Bridge is a simple, human-friendly language for expressing analytical intent. You write in a near-English format, and the system converts that into optimized SQL — with no need to remember column names or join logic.

Here’s how that process works:

### 🔄 In Practice

Let’s say you write this in Bridge DSL:

```bridge
SHOW net_deposits BY region
```

The system does the following under the hood:

1. **Parsing** (`parser.py`)
   - Converts the DSL into a structured representation:
     ```json
     {
       "command": "show",
       "metric": "net_deposits",
       "group_by": "region"
     }
     ```

2. **Config Mapping** (`config.py` + `bridgeconfig.yml`)
   - Loads your domain-specific meanings:
     ```yaml
     fields:
       net_deposits: "SUM(amount)"
       region: "region"
     tables:
       transactions: "transactions"
     ```

3. **Compilation** (`compiler.py`)
   - Uses both of the above to build SQL:
     ```sql
     SELECT region, SUM(amount) AS net_deposits
     FROM transactions
     GROUP BY region;
     ```

---

### 🧩 Core Components (With Analogies)

| Component | File | What It Does | Analogy |
|----------|------|---------------|---------|
| 🧠 **Parser** | `parser.py` | Turns Bridge text into structured meaning (AST) | Like a **language interpreter** listening to your sentence |
| 🗺️ **Config Loader** | `config.py` | Reads your dictionary of business terms → SQL mappings | Like a **recipe book** with ingredient translations |
| 🛠️ **Compiler** | `compiler.py` | Uses the AST + config to build SQL queries | Like a **chef** who cooks the final dish using the recipe |
| 📘 **Config File** | `bridgeconfig.yml` | Defines what each term means in SQL | Like a **translator cheat sheet** between human and database |
| 📝 **Bridge Scripts** | `examples/*.bridge` | Where you write your DSL commands | Like a **script or playbook** for what you want the system to do |
| ▶️ **Runner** | `run.py` | Orchestrates everything: parse → map → compile → output | Like pressing **play** to run your command |

---

> 🧪 Example Use Case:  
> A business user writes `SHOW net_deposits BY region`.  
> The system interprets it, looks up what that means, and delivers the SQL — no coding required.

---

## 🚀 Next Steps

- Add support for `DEFINE` expressions
- Implement `WHERE` and `FILTER TO`
- Introduce templated output backends (SQL, Python, etc.)
- Allow AI agents to generate Bridge DSL from natural questions
---

## 🧬 Language Evolution

Bridge is designed to grow with its users — both human and machine. Its simplicity is intentional, but it’s also meant to be extensible. One key feature currently in progress is:

### 🔤 `DEFINE` Expressions

Bridge allows the definition of reusable business logic with natural semantics:

```bridge
DEFINE good_customer AS: tenure > 24 AND avg_balance > 5000

SHOW net_deposits BY region
WHERE customer_type = good_customer
```

This:
- Encapsulates domain logic in a readable form
- Makes queries more understandable for analysts
- Enables reuse across multiple queries
- Encourages a shared vocabulary between teams and tools

---

## 🤝 Human + Machine Collaboration

Bridge isn’t just about simplifying queries — it’s about aligning intent across disciplines.

- **Analysts** define reusable terms and business logic
- **Engineers** map those terms to SQL or Spark
- **AI Agents** can generate Bridge DSL from natural questions
- **Systems** compile and execute those commands safely

The vision is to create a **living interface** where meaning, data, and execution are co-created — with Bridge acting as a shared dialect.
