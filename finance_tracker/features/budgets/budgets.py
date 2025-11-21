import os
import questionary
from rich.console import Console
from rich.table import Table
from datetime import datetime
from features.transactions.transactions import _read_transactions, EXPENSE_CATEGORIES

BUDGETS_FILE = "database/budgets.txt"
console = Console()

def set_budget():
    """Sets a budget for a specific category."""
    console.print("[bold blue]\n--- Set Category Budget ---[/bold blue]")

    category = questionary.select(
        "Select category to set budget for:",
        choices=EXPENSE_CATEGORIES,
        instruction="Choose an expense category."
    ).ask()
    if category is None: return

    amount_str = questionary.text(
        "Enter budget amount (e.g., 500.00):",
        validate=lambda text: text.replace('.', '', 1).isdigit() and float(text) > 0,
        instruction="Amount must be a positive number."
    ).ask()
    if amount_str is None: return
    amount_paisa = int(float(amount_str) * 100)

    # Read existing budgets
    budgets = {}
    if os.path.exists(BUDGETS_FILE):
        with open(BUDGETS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    budgets[parts[0]] = int(parts[1]) # category: amount_paisa

    budgets[category] = amount_paisa

    with open(BUDGETS_FILE, "w") as f:
        for cat, amt in budgets.items():
            f.write(f"{cat}|{amt}|{datetime.now().strftime('%Y-%m')}\n") # Save with current month for simplicity
    
    console.print(f"[bold green]Budget for '{category}' set to {(amount_paisa / 100):.2f} successfully![/bold green]")

def view_budgets():
    """Displays all set budgets and their status."""
    console.print("[bold blue]\n--- View Budgets ---[/bold blue]")

    budgets = {}
    if os.path.exists(BUDGETS_FILE):
        with open(BUDGETS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    budgets[parts[0]] = int(parts[1]) # category: amount_paisa

    if not budgets:
        console.print("[yellow]No budgets have been set yet. Use 'Set Budget' to create one.[/yellow]")
        return

    transactions = _read_transactions()
    current_month_expenses_by_category = {category: 0 for category in EXPENSE_CATEGORIES}
    current_month = datetime.now().month
    current_year = datetime.now().year

    for t in transactions:
        if t["type"] == "expense" and t["date"].month == current_month and t["date"].year == current_year:
            if t["category"] in current_month_expenses_by_category:
                current_month_expenses_by_category[t["category"]] += t["amount"]

    table = Table(title="[bold blue]Monthly Budgets Overview[/bold blue]")
    table.add_column("Category", style="cyan", no_wrap=True)
    table.add_column("Budgeted", style="green", justify="right")
    table.add_column("Spent", style="red", justify="right")
    table.add_column("Remaining", style="magenta", justify="right")
    table.add_column("Status", style="white")

    for category, budgeted_amount in budgets.items():
        spent_amount = current_month_expenses_by_category.get(category, 0)
        remaining_amount = budgeted_amount - spent_amount

        budgeted_display = f"{(budgeted_amount / 100):.2f}"
        spent_display = f"{(spent_amount / 100):.2f}"
        remaining_display = f"{(remaining_amount / 100):.2f}"

        status_color = "green" if remaining_amount >= 0 else "red"
        status_text = "Under Budget" if remaining_amount >= 0 else "Over Budget"

        table.add_row(
            category,
            budgeted_display,
            spent_display,
            f"[{status_color}]{remaining_display}[/{status_color}]",
            f"[{status_color}]{status_text}[/{status_color}]"
        )
    console.print(table)
