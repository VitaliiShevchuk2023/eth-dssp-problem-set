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



def unit_step(k):
    """Unit step function σ[k]."""
    return np.where(k >= 0, 1, 0)

def plot_signals_1():
    k = np.arange(-10, 10, 1)

    # Define the signals based on the problem
    sigma_k = unit_step(k)
    sigma_k_minus_2 = unit_step(k - 2)
    sigma_k_plus_2 = unit_step(k + 2)
    sigma_r_k = unit_step(-k)
    sigma_r_k_minus_2 = unit_step(-k + 2)
    sigma_r_k_plus_2 = unit_step(-k - 2)

    # Create subplots for each signal
    fig, axs = plt.subplots(3, 2, figsize=(10, 8))

    axs[0, 0].stem(k, sigma_k_minus_2)
    axs[0, 0].set_title(r'$\sigma[k - 2]$')

    axs[0, 1].stem(k, sigma_k_plus_2)
    axs[0, 1].set_title(r'$\sigma[k + 2]$')

    axs[1, 0].stem(k, sigma_r_k)
    axs[1, 0].set_title(r'$\sigma_r[k] = \sigma[-k]$')

    axs[1, 1].stem(k, sigma_r_k_minus_2)
    axs[1, 1].set_title(r'$\sigma_r[k - 2] = \sigma[-k + 2]$')

    axs[2, 0].stem(k, sigma_r_k_plus_2)
    axs[2, 0].set_title(r'$\sigma_r[k + 2] = \sigma[-k - 2]$')

    for ax in axs.flat:
        ax.grid(True)
        ax.set_xlabel('k')
        ax.set_ylabel('$\sigma[k]$')

    # Hide the last empty subplot
    axs[2, 1].axis('off')

    plt.tight_layout()
    st.pyplot(plt)


def classify_signals():
    classifications = {
        r'$\sigma[k - 2]$': {'Right-sided': True, 'Left-sided': False, 'Causal': False},
        r'$\sigma[k + 2]$': {'Right-sided': False, 'Left-sided': True, 'Causal': False},
        r'$\sigma_r[k] = \sigma[-k]$': {'Right-sided': False, 'Left-sided': True, 'Causal': False},
        r'$\sigma_r[k - 2] = \sigma[-k + 2]$': {'Right-sided': False, 'Left-sided': True, 'Causal': False},
        r'$\sigma_r[k + 2] = \sigma[-k - 2]$': {'Right-sided': True, 'Left-sided': False, 'Causal': False}
    }

    st.write("### Signal Classification")
    for signal, properties in classifications.items():
        st.write(f"**{signal}**:")
        for prop, value in properties.items():
            status = "Yes" if value else "No"
            st.write(f"- {prop}: {status}")



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


    
    # Problem description
    st.markdown("""
    **Problem 1.2 Operations with the Unit-step Signal**
    
     Let $$ \sigma[k] $$ be the unit-step signal:
    \[
    \sigma[k] = 
    \begin{cases} 
    1 & k \geq 0, \\
    0 & k < 0.
    \end{cases}
    \]

    a) Depict the following signals graphically:
    1. $$ \sigma[k - 2] $$
    2. $$ \sigma[k + 2] $$
    3. $$ \sigma_r[k] = \sigma[-k] $$
    4. $$ \sigma_r[k - 2] = \sigma[-k + 2] $$
    5. $$ \sigma_r[k + 2] = \sigma[-k - 2] $$
    
    b) Which of the signals are right-sided, left-sided, or causal?
    """)

    # Plot the signals
    plot_signals_1()

    classify_signals()
   







if __name__ == "__main__":
    main()
