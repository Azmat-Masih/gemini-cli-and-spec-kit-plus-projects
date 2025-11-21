import questionary
from rich.console import Console
from rich.table import Table
from datetime import datetime
from collections import defaultdict
from features.transactions.transactions import _read_transactions, EXPENSE_CATEGORIES

console = Console()

def monthly_summary():
    """Displays a summary of income, expenses, and net for the current month."""
    console.print("[bold blue]\n--- Monthly Summary ---[/bold blue]")

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
    
    net_savings = current_month_income - current_month_expenses

    console.print(f"Total Income (this month): [bold green]{(current_month_income / 100):.2f}[/bold green]")
    console.print(f"Total Expenses (this month): [bold red]{(current_month_expenses / 100):.2f}[/bold red]")
    
    net_color = "green" if net_savings >= 0 else "red"
    console.print(f"Net Savings/Loss (this month): [bold {net_color}]{(net_savings / 100):.2f}[/bold {net_color}]")

def category_wise_spending():
    """Displays a breakdown of spending by category for the current month."""
    console.print("[bold blue]\n--- Category-wise Spending ---[/bold blue]")

    transactions = _read_transactions()
    category_spending = defaultdict(int)
    current_month = datetime.now().month
    current_year = datetime.now().year

    for t in transactions:
        if t["type"] == "expense" and t["date"].month == current_month and t["date"].year == current_year:
            category_spending[t["category"]] += t["amount"]
    
    if not category_spending:
        console.print("[yellow]No expenses recorded for the current month to display category-wise spending.[/yellow]")
        return

    table = Table(title="[bold blue]Category-wise Spending (Current Month)[/bold blue]")
    table.add_column("Category", style="cyan", no_wrap=True)
    table.add_column("Amount Spent", style="red", justify="right")

    for category, amount in category_spending.items():
        table.add_row(
            category,
            f"{(amount / 100):.2f}"
        )
    console.print(table)
