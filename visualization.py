"""Summary statistics and trend plotting for BMI history."""
import pandas as pd
import matplotlib.pyplot as plt


def show_summary(df: pd.DataFrame) -> None:
    """Print average/min/max BMI, plus a rolling average once there's enough data."""
    if df.empty:
        print("No history yet for this user.\n")
        return

    print(f"\nAverage BMI: {df['bmi'].mean():.2f}")
    print(f"Min BMI: {df['bmi'].min():.2f}")
    print(f"Max BMI: {df['bmi'].max():.2f}")

    if len(df) >= 3:
        rolling_avg = df["bmi"].rolling(3).mean().iloc[-1]
        print(f"Rolling average (last 3 entries): {rolling_avg:.2f}")
    print()


def plot_history(df: pd.DataFrame, name: str) -> None:
    """Plot BMI over time for a user. Requires at least 2 entries.

    A fresh figure is created (and closed) on every call so that viewing
    the graph more than once in the same session doesn't overlay points
    from the previous plot onto the same axes.
    """
    if len(df) < 2:
        print("\nNeed at least 2 entries to plot a trend.\n")
        return

    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    plt.figure()
    plt.plot(df["timestamp"], df["bmi"], marker="o")
    plt.title(f"BMI trend - {name}")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()
    plt.close()
