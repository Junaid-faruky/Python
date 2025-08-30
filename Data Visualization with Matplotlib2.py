# Create various types of plots and charts
import matplotlib.pyplot as plt
import numpy as np

def create_dashboard():
    # Sample data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    categories = ['A', 'B', 'C', 'D']
    values = [23, 45, 56, 78]
    
    # Create subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # Line plot
    ax1.plot(x, y1, label='sin(x)', color='blue')
    ax1.plot(x, y2, label='cos(x)', color='red')
    ax1.set_title('Trigonometric Functions')
    ax1.legend()
    ax1.grid(True)
    
    # Bar chart
    ax2.bar(categories, values, color=['red', 'green', 'blue', 'orange'])
    ax2.set_title('Category Values')
    ax2.set_ylabel('Values')
    
    # Scatter plot
    x_scatter = np.random.rand(50) * 10
    y_scatter = np.random.rand(50) * 10
    ax3.scatter(x_scatter, y_scatter, alpha=0.6, color='purple')
    ax3.set_title('Random Scatter Plot')
    ax3.set_xlabel('X values')
    ax3.set_ylabel('Y values')
    
    # Pie chart
    ax4.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
    ax4.set_title('Distribution Pie Chart')
    
    plt.tight_layout()
    plt.show()

# Generate the dashboard
create_dashboard()
