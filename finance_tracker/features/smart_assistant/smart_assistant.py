import questionary
from rich.console import Console
from rich.table import Table
from datetime import datetime
from collections import defaultdict
from features.transactions.transactions import _read_transactions, EXPENSE_CATEGORIES
from features.budgets.budgets import BUDGETS_FILE

console = Console()

def spending_analysis():
    """Analyzes spending patterns and identifies top spending categories."""
    console.print("[bold blue]\n--- Spending Analysis ---[/bold blue]")

    transactions = _read_transactions()
    current_month_spending = defaultdict(int)
    current_month = datetime.now().month
    current_year = datetime.now().year

    for t in transactions:
        if t["type"] == "expense" and t["date"].month == current_month and t["date"].year == current_year:
            current_month_spending[t["category"]] += t["amount"]
    
    if not current_month_spending:
        console.print("[yellow]No expenses recorded for the current month to perform spending analysis.[/yellow]")
        return

    console.print("\n[bold underline]Top Spending Categories (Current Month):[/bold underline]")
    sorted_spending = sorted(current_month_spending.items(), key=lambda item: item[1], reverse=True)

    table = Table(title="[bold blue]Spending by Category[/bold blue]")
    table.add_column("Category", style="cyan")
    table.add_column("Amount Spent", style="red", justify="right")

    for category, amount in sorted_spending:
        table.add_row(category, f"{(amount / 100):.2f}")
    console.print(table)

    # Identify potentially high spending
    console.print("\n[bold underline]Insights:[/bold underline]")
    total_spent = sum(current_month_spending.values())
    if total_spent > 0:
        for category, amount in sorted_spending:
            percentage = (amount / total_spent) * 100
            if percentage > 30: # Arbitrary threshold for "high" spending
                console.print(f"- [yellow]You spent {percentage:.2f}% of your total expenses on '{category}' this month. Consider reviewing this category.[/yellow]")
    else:
        console.print("- [green]Your spending is well-distributed this month.[/green]")

def savings_suggestions():
    """Provides suggestions for saving money based on spending habits."""
    console.print("[bold blue]\n--- Savings Suggestions ---[/bold blue]")

    transactions = _read_transactions()
    current_month_spending = defaultdict(int)
    current_month = datetime.now().month
    current_year = datetime.now().year

    for t in transactions:
        if t["type"] == "expense" and t["date"].month == current_month and t["date"].year == current_year:
            current_month_spending[t["category"]] += t["amount"]
    
    if not current_month_spending:
        console.print("[yellow]No expenses recorded for the current month to provide savings suggestions.[/yellow]")
        return

    console.print("\n[bold underline]Here are some savings suggestions based on your spending:[/bold underline]")
    suggestions_made = False

    for category, amount in current_month_spending.items():
        if category == "Food" and amount > 50000: # > $500
            console.print("- [green]You spent a significant amount on 'Food' this month. Consider packing lunch twice a week or cooking more at home to save.[/green]")
            suggestions_made = True
        elif category == "Entertainment" and amount > 30000: # > $300
            console.print("- [green]Your 'Entertainment' spending is quite high. Look for free local events or consider a 'no-spend' weekend.[/green]")
            suggestions_made = True
        elif category == "Shopping" and amount > 40000: # > $400
            console.print("- [green]High 'Shopping' expenses detected. Try to differentiate between needs and wants before making a purchase.[/green]")
            suggestions_made = True
    
    if not suggestions_made:
        console.print("[green]Your spending seems balanced this month. Keep up the good work![/green]")

import os

def budget_optimization():
    """Suggests adjustments to budgets based on actual spending patterns."""
    console.print("[bold blue]\n--- Budget Optimization ---[/bold blue]")

    budgets = {}
    if os.path.exists(BUDGETS_FILE):
        with open(BUDGETS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    budgets[parts[0]] = int(parts[1]) # category: amount_paisa

    if not budgets:
        console.print("[yellow]No budgets set yet to provide optimization suggestions. Use 'Set Budget' to create one.[/yellow]")
        return

    transactions = _read_transactions()
    current_month_expenses_by_category = defaultdict(int)
    current_month = datetime.now().month
    current_year = datetime.now().year

    for t in transactions:
        if t["type"] == "expense" and t["date"].month == current_month and t["date"].year == current_year:
            current_month_expenses_by_category[t["category"]] += t["amount"]
    
    console.print("\n[bold underline]Budget Optimization Suggestions:[/bold underline]")
    suggestions_made = False

    for category, budgeted_amount in budgets.items():
        spent_amount = current_month_expenses_by_category.get(category, 0)
        
        if budgeted_amount > 0 and spent_amount < budgeted_amount * 0.7: # Consistently underspending (e.g., less than 70%)
            console.print(f"- [green]Your '{category}' budget of {(budgeted_amount / 100):.2f} is consistently underspent (spent {(spent_amount / 100):.2f}). Consider reallocating {(budgeted_amount - spent_amount) / 100:.2f} to another category or savings.[/green]")
            suggestions_made = True
        elif budgeted_amount > 0 and spent_amount > budgeted_amount * 1.1: # Consistently overspending (e.g., more than 110%)
            console.print(f"- [red]You are overspending in your '{category}' budget (budgeted {(budgeted_amount / 100):.2f}, spent {(spent_amount / 100):.2f}). Consider increasing this budget or finding ways to reduce spending in this category.[/red]")
            suggestions_made = True
    
    if not suggestions_made:
        console.print("[green]Your budgets seem well-aligned with your spending this month. Great job![/green]")

def financial_tips():
    """Offers general financial advice."""
    console.print("[bold blue]\n--- Financial Tips ---[/bold blue]")

    tips = [
        "Create a budget and stick to it. Knowing where your money goes is the first step to financial control.",
        "Build an emergency fund. Aim for 3-6 months of living expenses in a separate, easily accessible account.",
        "Pay off high-interest debt first. This can save you a significant amount of money in the long run.",
        "Invest in yourself through education or skills development to increase your earning potential.",
        "Review your subscriptions regularly and cancel any that you don't frequently use.",
        "Automate your savings. Set up automatic transfers to your savings account each payday.",
        "Track your spending. This helps you identify areas where you can cut back.",
        "Set clear financial goals, whether it's saving for a down payment, retirement, or a vacation."
    ]

    console.print("\n[bold underline]Here are some general financial tips:[/bold underline]")
    for i, tip in enumerate(tips):
        console.print(f"[green]{i+1}. {tip}[/green]")
