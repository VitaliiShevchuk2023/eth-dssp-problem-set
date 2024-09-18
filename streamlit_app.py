import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

def analyze_properties(a):
    # Determine properties of the signal
    right_sided = True  # Always true
    left_sided = False  # Always false
    abs_summable = abs(a) < 1
    square_summable = abs(a) < 1
    bounded = abs(a) <= 1

    return {
        'Right-sided': right_sided,
        'Left-sided': left_sided,
        'Absolutely Summable': abs_summable,
        'Square Summable': square_summable,
        'Bounded': bounded
    }

def plot_signal(a, properties):
    # Set font for supporting special characters
    rcParams['font.family'] = 'DejaVu Sans'

    # Signal parameters
    k = np.arange(0, 20)
    f_k = a ** k

    # Generate the plot title based on properties
    title_parts = []
    if properties['Right-sided']:
        title_parts.append('Right-sided')
    if properties['Left-sided']:
        title_parts.append('Left-sided')
    if properties['Absolutely Summable']:
        title_parts.append('Absolutely Summable')
    if properties['Square Summable']:
        title_parts.append('Square Summable')
    if properties['Bounded']:
        title_parts.append('Bounded')
    
    #title = f'Signal for $a = {a}$: ' + ', '.join(title_parts)
    title = f'Signal for $a = {a}$' 


    # Visualization
    plt.figure(figsize=(10, 6))
    plt.stem(k, f_k)
    plt.title(title)
    plt.xlabel('$k$')
    plt.ylabel('$f[k]$')
    plt.grid(True)
    plt.tight_layout()

    # Display the plot
    st.pyplot(plt)

def main():
    st.title('Discrete-time and Statistical Signal Processing')

    # header
    st.header("Problem set 1")

    # Problem statement with LaTeX
    st.markdown("""
    **Problem 1.1 Signals**

    Let $$f[k] = 0 $$ for $$ k < 0 $$ and $$ f[k] = a^k $$ for $$ k \geq 0 $$. For which values of $$ a \in \mathbb{C} $$ is $$ f[\cdot] $$:

    a) Right-sided? \\
    b) Left-sided? \\
    c) Absolutely summable? \\
    d) Square summable? \\
    e) Bounded?
    """)

    # Input for parameter a
    a = st.number_input('Enter the value of $a$', value=0.5, step=0.1, format="%.1f")

    # Analyze properties
    properties = analyze_properties(a)

    # Display the signal plot
    plot_signal(a, properties)

if __name__ == "__main__":
    main()
