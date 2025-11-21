import os
import questionary
from rich.console import Console
from rich.table import Table
from datetime import datetime

TRANSACTIONS_FILE = "database/transactions.txt"
console = Console()

EXPENSE_CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Health", "Other"]

INCOME_SOURCES = ["Salary", "Freelance", "Business", "Investment", "Gift", "Other"]

def add_expense():
    """Adds an expense transaction."""
    console.print("[bold red]\n--- Add New Expense ---[/bold red]")

    amount_str = questionary.text(
        "Enter amount (e.g., 12.50):",
        validate=lambda text: text.replace('.', '', 1).isdigit() and float(text) > 0,
        instruction="Amount must be a positive number."
    ).ask()
    if amount_str is None: return
    amount_paisa = int(float(amount_str) * 100)

    category = questionary.select(
        "Select category for this expense:",
        choices=EXPENSE_CATEGORIES
    ).ask()
    if category is None: return

    description = questionary.text(
        "Enter a brief description (e.g., 'Lunch with John'):"
    ).ask()
    if description is None: return

    date_str = questionary.text(
        "Enter date (YYYY-MM-DD, default today):",
        default=datetime.now().strftime("%Y-%m-%d"),
        instruction="Press Enter for today's date."
    ).ask()
    if date_str is None: return
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        console.print("[bold red]Invalid date format. Please use YYYY-MM-DD. Using today's date.[/bold red]")
        date_str = datetime.now().strftime("%Y-%m-%d")

    with open(TRANSACTIONS_FILE, "a") as f:
        f.write(f"{date_str}|expense|{amount_paisa}|{category}|{description}\n")
    console.print("[bold green]Expense added successfully![/bold green]")

def add_income():
    """Adds an income transaction."""
    console.print("[bold green]\n--- Add New Income ---[/bold green]")

    amount_str = questionary.text(
        "Enter amount (e.g., 100.00):",
        validate=lambda text: text.replace('.', '', 1).isdigit() and float(text) > 0,
        instruction="Amount must be a positive number."
    ).ask()
    if amount_str is None: return
    amount_paisa = int(float(amount_str) * 100)

    source = questionary.select(
        "Select source of this income:",
        choices=INCOME_SOURCES
    ).ask()
    if source is None: return

    description = questionary.text(
        "Enter a brief description (e.g., 'Freelance project payment'):"
    ).ask()
    if description is None: return

    date_str = questionary.text(
        "Enter date (YYYY-MM-DD, default today):",
        default=datetime.now().strftime("%Y-%m-%d"),
        instruction="Press Enter for today's date."
    ).ask()
    if date_str is None: return
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        console.print("[bold red]Invalid date format. Please use YYYY-MM-DD. Using today's date.[/bold red]")
        date_str = datetime.now().strftime("%Y-%m-%d")

    with open(TRANSACTIONS_FILE, "a") as f:
        f.write(f"{date_str}|income|{amount_paisa}|{source}|{description}\n")
    console.print("[bold green]Income added successfully![/bold green]")

def _read_transactions():
    transactions = []
    if not os.path.exists(TRANSACTIONS_FILE):
        return transactions
    with open(TRANSACTIONS_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 5:
                transactions.append({
                    "date": datetime.strptime(parts[0], "%Y-%m-%d"),
                    "type": parts[1],
                    "amount": int(parts[2]),
                    "category": parts[3],
                    "description": parts[4]
                })
    return transactions

def list_transactions():
    """Lists all transactions."""
    console.print("[bold blue]\n--- All Transactions ---[/bold blue]")

    transactions = _read_transactions()
    transactions.sort(key=lambda x: x["date"], reverse=True)

    # Filtering options
    filter_choice = questionary.select(
        "Filter transactions:",
        choices=["All", "Last 7 days", "Expenses only", "Income only"]
    ).ask()
    if filter_choice is None: return

    filtered_transactions = []
    today = datetime.now().date()

    for t in transactions:
        include = True
        if filter_choice == "Last 7 days":
            if (today - t["date"].date()).days > 7:
                include = False
        elif filter_choice == "Expenses only":
            if t["type"] != "expense":
                include = False
        elif filter_choice == "Income only":
            if t["type"] != "income":
                include = False
        
        if include:
            filtered_transactions.append(t)

    if not filtered_transactions:
        console.print("[yellow]No transactions match the selected filter.[/yellow]")
        return

    table = Table(title="[bold blue]Transactions Overview[/bold blue]")
    table.add_column("Date", style="cyan", no_wrap=True)
    table.add_column("Type", style="magenta")
    table.add_column("Category/Source", style="blue")
    table.add_column("Description", style="white")
    table.add_column("Amount", style="green", justify="right")

    for t in filtered_transactions:
        amount_display = f"{(t['amount'] / 100):.2f}"
        color = "red" if t["type"] == "expense" else "green"
        table.add_row(
            t["date"].strftime("%Y-%m-%d"),
            t["type"].capitalize(),
            t["category"],
            t["description"],
            f"[{color}]{amount_display}[/{color}]"
        )
    console.print(table)

def balance_command():
    """Displays current balance."""
    console.print("[bold magenta]\n--- Current Balance ---[/bold magenta]")

    transactions = _read_transactions()
    
    current_month_income = 0
    current_month_expenses = 0
    current_month = datetime.now().month
    current_year = datetime.now().year

    for t in transactions:
        if t["date"].month == current_month and t["date"].year == current_year:
            if t["type"] == "income":
                current_month_income += t["amount"]
            elif t["type"] == "expense":
                current_month_expenses += t["amount"]
    
    current_balance = current_month_income - current_month_expenses

    console.print(f"Total Income (this month): [bold green]{(current_month_income / 100):.2f}[/bold green]")
    console.print(f"Total Expenses (this month): [bold red]{(current_month_expenses / 100):.2f}[/bold red]")
    
    balance_color = "green" if current_balance >= 0 else "red"
    console.print(f"Current Balance: [bold {balance_color}]{(current_balance / 100):.2f}[/bold {balance_color}]")
