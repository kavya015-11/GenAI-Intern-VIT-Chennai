import matplotlib.pyplot as plt
import os
import uuid

def generate_bar_chart(columns, data, title="Bar Chart"):
    x = [row[0] for row in data]
    y = [row[1] for row in data]

    plt.figure(figsize=(10, 6))
    plt.bar(x, y, color="skyblue")
    plt.xlabel(columns[0])
    plt.ylabel(columns[1])
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()

    os.makedirs("charts", exist_ok=True)
    filename = f"chart_{uuid.uuid4().hex}.png"
    filepath = os.path.join("charts", filename)
    plt.savefig(filepath)
    plt.close()
    return filepath

def generate_pie_chart(columns, data, title="Pie Chart"):
    labels = []
    sizes = []

    for row in data:
        label, size = row[0], row[1]
        if size > 0:
            labels.append(label)
            sizes.append(size)

    if not sizes:
        return None  # No valid values to show

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title(title)
    plt.tight_layout()

    os.makedirs("charts", exist_ok=True)
    filename = f"pie_{uuid.uuid4().hex}.png"
    filepath = os.path.join("charts", filename)
    plt.savefig(filepath)
    plt.close()
    return filepath
