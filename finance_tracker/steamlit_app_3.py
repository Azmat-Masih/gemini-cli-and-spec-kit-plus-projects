import streamlit as st
import pandas as pd
import json
from datetime import datetime, date
from pathlib import Path
import plotly.express as px

# --- Constants & Paths ---
CURRENCY = "Rs"
DATA_DIR = Path("finance_tracker/database")
TRANSACTIONS_FILE = DATA_DIR / "transactions.json"
BUDGETS_FILE = DATA_DIR / "budgets.json"
BACKUPS_DIR = DATA_DIR / "backups"

DATA_DIR.mkdir(parents=True, exist_ok=True)
BACKUPS_DIR.mkdir(parents=True, exist_ok=True)

# --- Utility Functions ---
def now_ts():
    return datetime.now().isoformat()

def to_paisa(amount_str: str) -> int:
    try:
        s = str(amount_str).replace(",", "").replace(CURRENCY, "").strip()
        if s == "": return 0
        neg = s.startswith("-")
        if neg: s = s[1:]
        if "." in s:
            rupees, paisa = s.split(".")
            paisa = (paisa + "00")[:2]
            total = int(rupees) * 100 + int(paisa)
        else:
            total = int(s) * 100
        return -total if neg else total
    except:
        return 0

def from_paisa(amount_paisa: int) -> str:
    sign = "-" if amount_paisa < 0 else ""
    a = abs(amount_paisa)
    rupees = a // 100
    paisa = a % 100
    return f"{sign}{rupees}.{paisa:02d}"

# --- Storage Helpers ---
def load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except:
            return default
    return default

def save_json(path: Path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")

# --- Session State ---
if "transactions" not in st.session_state:
    st.session_state.transactions = load_json(TRANSACTIONS_FILE, [])
if "budgets" not in st.session_state:
    st.session_state.budgets = load_json(BUDGETS_FILE, {})

transactions = st.session_state.transactions
budgets = st.session_state.budgets

# --- Transaction Helpers ---
def list_transactions(limit=None, ttype=None, days=None):
    df = pd.DataFrame(st.session_state.transactions)
    if df.empty:
        return df
    df["date"] = pd.to_datetime(df["date"])
    if ttype:
        df = df[df["type"] == ttype]
    if days:
        df = df[df["date"] >= pd.Timestamp.now() - pd.Timedelta(days=days)]
    df = df.sort_values(by="date", ascending=False)
    if limit:
        df = df.head(limit)
    return df

def add_transaction(record):
    st.session_state.transactions.insert(0, record)
    save_json(TRANSACTIONS_FILE, st.session_state.transactions)

# --- Budget Helpers ---
def get_monthly_spent_for_category(category):
    df = list_transactions()
    if df.empty:
        return 0
    now = pd.Timestamp.now()
    df_m = df[
        (df["date"].dt.year == now.year) &
        (df["date"].dt.month == now.month) &
        (df["type"] == "expense") &
        (df["category"] == category)
    ]
    return int(df_m["amount_paisa"].sum())

def set_budget(category, amount_paisa):
    st.session_state.budgets[category] = {"amount": amount_paisa, "updated": now_ts()}
    save_json(BUDGETS_FILE, st.session_state.budgets)

# --- Analytics Helper ---
def calculate_health_score():
    df = list_transactions()
    if df.empty:
        return 50, {}
    now = pd.Timestamp.now()
    month_df = df[
        (df["date"].dt.year == now.year) &
        (df["date"].dt.month == now.month)
    ]
    income = int(month_df[month_df["type"] == "income"]["amount_paisa"].sum())
    expense = int(month_df[month_df["type"] == "expense"]["amount_paisa"].sum())
    savings = max(income - expense, 0)
    savings_rate = (savings / income) if income > 0 else 0
    adherence = sum(
        get_monthly_spent_for_category(c) <= b["amount"]
        for c, b in st.session_state.budgets.items()
    ) / max(1, len(st.session_state.budgets))
    score = int(min(100, savings_rate * 30 + adherence * 40 + (income > 0) * 30))
    return score, {"savings_rate": savings_rate, "adherence": adherence, "income_present": income > 0}

# --- Streamlit Config ---
st.set_page_config(page_title="Finance Tracker", layout="wide", page_icon="💰")

# --- CSS for Modern Dashboard ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.card {
    background-color: var(--card-bg);
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    padding: 24px;
    margin-bottom: 24px;
}

.scrollable-table { overflow-x: auto; }

.metric-label { font-size: 0.9rem; color: var(--muted); }
.metric-value { font-size: 1.6rem; font-weight: 600; margin-top: 4px; }

@media (max-width: 640px) {
    .card { padding: 16px; margin-bottom: 16px; }
    .metric-value { font-size: 1.2rem; }
}

:root { --card-bg: #ffffff; --muted: #6b7280; --bg: #f8fafc; --text-color: #111827; }
.dark-mode { --card-bg: #1f2937; --muted: #9ca3af; --bg: #111827; --text-color: #f3f4f6; }

.stApp { background-color: var(--bg); color: var(--text-color); }
</style>
""", unsafe_allow_html=True)

# --- Dark Mode Toggle ---
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

col1, col2 = st.columns([3, 1])
with col1:
    st.title("Finance Tracker")
with col2:
    st.session_state.dark_mode = st.checkbox("Dark Mode", value=st.session_state.dark_mode)

if st.session_state.dark_mode:
    st.markdown("<script>document.querySelector('body').classList.add('dark-mode')</script>", unsafe_allow_html=True)

# --- Sidebar Navigation ---
page = st.sidebar.selectbox("Navigate", ["Dashboard", "Transactions", "Budgets", "Analytics", "Data & Export"])

# ------------------ DASHBOARD ------------------
if page == "Dashboard":
    df_month = list_transactions()
    now = pd.Timestamp.now()
    if not df_month.empty:
        df_month = df_month[(df_month["date"].dt.year == now.year) & (df_month["date"].dt.month == now.month)]
        income = int(df_month[df_month["type"] == "income"]["amount_paisa"].sum())
        expense = int(df_month[df_month["type"] == "expense"]["amount_paisa"].sum())
    else:
        income = expense = 0
    balance = income - expense
    score, _ = calculate_health_score()

    # KPI Cards Container
    with st.container():
        k1, k2, k3, k4 = st.columns(4, gap="large")
        for col, label, value in zip([k1, k2, k3, k4],
                                     ["Income (This Month)", "Expenses (This Month)", "Balance", "Health Score"],
                                     [income, expense, balance, score]):
            display_val = f"{CURRENCY} {from_paisa(value)}" if label != "Health Score" else f"{value}/100"
            col.markdown(f"<div class='metric-label'>{label}</div><div class='metric-value'>{display_val}</div>", unsafe_allow_html=True)

    # Charts Container
    with st.container():
        df_all = list_transactions()
        if not df_all.empty:
            df_all["date"] = pd.to_datetime(df_all["date"])
            col_chart1, col_chart2 = st.columns(2, gap="large")
            with col_chart1:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                cat_group = df_month[df_month["type"]=="expense"].groupby("category")["amount_paisa"].sum()
                if not cat_group.empty:
                    fig = px.pie(values=cat_group.values, names=cat_group.index, hole=0.4, title="Expense Breakdown")
                    st.plotly_chart(fig, use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

            with col_chart2:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                fig = px.line(df_all.sort_values("date"), x="date", y="amount_paisa", color="type", markers=True, title="Transaction History")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)

    # Recent Transactions Container
    with st.container():
        st.markdown("<div class='card scrollable-table'>", unsafe_allow_html=True)
        st.subheader("Recent Transactions")
        df_recent = list_transactions(limit=10)
        if df_recent.empty:
            st.info("No transactions yet.")
        else:
            df_recent["Amount"] = df_recent["amount_paisa"].apply(lambda x: f"{CURRENCY} {from_paisa(x)}")
            st.dataframe(df_recent[["date","type","category","description","Amount"]], use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ------------------ TRANSACTIONS ------------------
elif page == "Transactions":
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.header("Transactions")

        tab1, tab2 = st.tabs(["Add", "List & Filter"])
        with tab1:
            with st.form("add_txn"):
                txn_type = st.selectbox("Type", ["expense", "income"])
                amount = st.text_input("Amount (e.g. 1250 or 12.50)")
                category = st.selectbox(
                    "Category",
                    ["Food","Transport","Shopping","Bills","Entertainment","Health","Other"] if txn_type=="expense" else
                    ["Salary","Freelance","Business","Investment","Gift","Other"]
                )
                description = st.text_input("Description")
                txn_date = st.date_input("Date", date.today())
                submitted = st.form_submit_button("Add Transaction")
                if submitted:
                    paisa = to_paisa(amount)
                    if paisa==0: st.error("Enter a valid amount")
                    else:
                        add_transaction({
                            "id": int(datetime.now().timestamp()*1000),
                            "date": txn_date.isoformat(),
                            "type": txn_type,
                            "category": category,
                            "description": description,
                            "amount_paisa": paisa,
                            "created": now_ts()
                        })
                        st.success("Transaction added")

        with tab2:
            st.subheader("Filter & Search")
            search = st.text_input("Search by description or category")
            filter_opt = st.selectbox("Filter", ["All","Expenses","Income","Last 7 days","Last 30 days"])
            if filter_opt=="All": df = list_transactions()
            elif filter_opt=="Expenses": df = list_transactions(ttype="expense")
            elif filter_opt=="Income": df = list_transactions(ttype="income")
            elif filter_opt=="Last 7 days": df=list_transactions(days=7)
            else: df=list_transactions(days=30)

            if not df.empty:
                df["Amount"] = df["amount_paisa"].apply(lambda x: f"{CURRENCY} {from_paisa(x)}")
                if search:
                    df = df[df["description"].str.contains(search, case=False, na=False) |
                            df["category"].str.contains(search, case=False, na=False)]
                st.dataframe(df[["date","type","category","description","Amount"]], use_container_width=True)
            else:
                st.info("No transactions found")

        st.markdown("</div>", unsafe_allow_html=True)

# ------------------ BUDGETS ------------------
elif page=="Budgets":
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.header("Budgets")

        with st.form("set_budget"):
            cat = st.selectbox("Category", ["Food","Transport","Shopping","Bills","Entertainment","Health"])
            amt = st.text_input("Monthly budget amount")
            if st.form_submit_button("Set Budget"):
                set_budget(cat,to_paisa(amt))
                st.success(f"Budget set for {cat}")

        st.subheader("Budget Overview")
        if not budgets:
            st.info("No budgets set yet.")
        else:
            rows=[]
            for c,b in budgets.items():
                spent=get_monthly_spent_for_category(c)
                remaining=b["amount"]-spent
                util=int(min(100,(spent/b['amount']*100 if b["amount"]>0 else 0)))
                rows.append({"Category":c,"Budget":f"{CURRENCY} {from_paisa(b['amount'])}","Spent":f"{CURRENCY} {from_paisa(spent)}","Remaining":f"{CURRENCY} {from_paisa(remaining)}","Utilisation (%)":f"{util}%"})
            st.table(pd.DataFrame(rows))
        st.markdown("</div>", unsafe_allow_html=True)

# ------------------ ANALYTICS ------------------
elif page=="Analytics":
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.header("Analytics & Insights")

        df_all = list_transactions()
        if df_all.empty:
            st.info("No data yet")
        else:
            df_all["date"]=pd.to_datetime(df_all["date"])
            now=pd.Timestamp.now()
            df_month=df_all[(df_all["date"].dt.year==now.year) & (df_all["date"].dt.month==now.month)]

            # Spending by Category
            st.subheader("Spending by Category (This Month)")
            cat_group=df_month[df_month["type"]=="expense"].groupby("category")["amount_paisa"].sum()
            if not cat_group.empty:
                fig_cat = px.pie(values=cat_group.values, names=cat_group.index, hole=0.4)
                st.plotly_chart(fig_cat, use_container_width=True)

            # Transactions over time
            st.subheader("All Transactions Over Time")
            fig_tr = px.line(df_all.sort_values("date"), x="date", y="amount_paisa", color="type", markers=True)
            st.plotly_chart(fig_tr, use_container_width=True)

            # Metrics
            income=int(df_month[df_month["type"]=="income"]["amount_paisa"].sum())
            expense=int(df_month[df_month["type"]=="expense"]["amount_paisa"].sum())
            burn_rate = expense/max(1,now.day)
            c1,c2,c3 = st.columns(3)
            c1.metric("Income (This Month)", f"{CURRENCY} {from_paisa(income)}")
            c2.metric("Expense (This Month)", f"{CURRENCY} {from_paisa(expense)}")
            c3.metric("Avg Daily Spend", f"{CURRENCY} {from_paisa(int(burn_rate))}")

            score,_=calculate_health_score()
            st.subheader("Financial Health Score")
            st.metric("Score", f"{score}/100")

        st.markdown("</div>", unsafe_allow_html=True)

# ------------------ DATA & EXPORT ------------------
elif page=="Data & Export":
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.header("Data & Export")

        if st.button("Create Backup"):
            ts=datetime.now().strftime("%Y%m%d%H%M%S")
            backup={"transactions":transactions,"budgets":budgets,"created":now_ts()}
            save_json(BACKUPS_DIR/f"backup_{ts}.json", backup)
            st.success(f"Backup created: backup_{ts}.json")

        df=pd.DataFrame(transactions)
        if not df.empty:
            df["Amount"]=df["amount_paisa"].apply(lambda x: from_paisa(int(x)))
            st.download_button("Download CSV", data=df.to_csv(index=False), file_name="transactions.csv", mime="text/csv")
            st.download_button("Download JSON", data=json.dumps(transactions, indent=2), file_name="transactions.json", mime="application/json")
        else:
            st.info("No transactions to export")

        st.markdown("</div>", unsafe_allow_html=True)

# ------------------ SAVE STATE ------------------
save_json(TRANSACTIONS_FILE, transactions)
save_json(BUDGETS_FILE, budgets)

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("Built with ❤️ by Azmat Masih. Data stored locally in database/ folder.")
