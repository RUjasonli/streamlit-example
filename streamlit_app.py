import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from math import sqrt

# Creates Calculator Function
def confidence_interval(mean, standard_deviation, sample_size):
    a = mean
    b = standard_deviation
    c = sample_size

    # Returns Lower and Upper Bounds
    return (a - 1.9600 * (b / sqrt(c)), a + 1.9600 * (b / sqrt(c)))

# Streamlit app
def main():
    st.title("Confidence Interval Calculator")

    # Input values
    mean = st.number_input("Mean:", value=0.8)
    std_dev = st.number_input("Standard Deviation:", value=0.05)
    sample_size = st.number_input("Sample Size:", value=30)

    # Calculate confidence interval
    lower_bound, upper_bound = confidence_interval(mean, std_dev, sample_size)

    # Display results
    st.write(f"Lower Bound: {lower_bound:.4f}")
    st.write(f"Upper Bound: {upper_bound:.4f}")

    # Plot normal distribution
    x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 1000)
    y = norm.pdf(x, mean, std_dev)
    
    plt.plot(x, y, label='Normal Distribution')
    plt.fill_between(x, y, where=[(xi >= lower_bound) and (xi <= upper_bound) for xi in x], alpha=0.3, color='orange', label='Confidence Interval')
    
    plt.title('Normal Distribution with Confidence Interval')
    plt.xlabel('Values')
    plt.ylabel('Probability Density')
    plt.legend()

    # Display the plot using Streamlit
    st.pyplot()

if __name__ == "__main__":
    main()
