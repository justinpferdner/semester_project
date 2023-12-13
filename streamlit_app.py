import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

st.title('Dashboard: Analyzing Home Prices in Utah')

homes = pd.read_csv('homes.csv')
homes['Price_per_sqft'] = homes['Price'] / homes['Sqft']
homes = homes.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'])
homes['ZipCode'] = homes['ZipCode'].astype(str)


def distribution_of_home_prices(homes):
    plt.figure(figsize=(10, 6))
    sns.histplot(homes['Price'], bins=30, kde=True)
    plt.title('Distribution of Home Prices')
    plt.xlabel('Price ($)')
    plt.ylabel('Frequency')
    st.pyplot()

def scatter_plot_price_vs_square_footage_by_county(homes):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=homes, x='Sqft', y='Price', hue='County', palette="Set2", alpha=0.7)
    plt.title('Scatter Plot of Price vs. Square Footage by County')
    plt.xlabel('Square Footage')
    plt.ylabel('Home Price ($)')
    plt.legend(title='County')
    st.pyplot()

def boxplot_of_home_prices_by_county(homes):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=homes, x='County', y='Price', palette="Set2")
    plt.title('Boxplot of Home Prices (by County)')
    plt.xlabel('County')
    plt.ylabel('Home Price ($)')
    st.pyplot()

def correlation_heatmap(homes):
    selected_columns = ['Price', 'Bedrooms', 'Bathrooms', 'Sqft']
    correlation_matrix = homes[selected_columns].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Correlation Heatmap')
    st.pyplot()

def average_price_per_square_foot_in_different_cities(homes):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='City', y='Price_per_sqft', data=homes)
    plt.title('Average Price per Square Foot in Different Cities')
    plt.xlabel('City')
    plt.ylabel('Average Price per Square Foot ($)')
    plt.xticks(rotation=90)
    st.pyplot()

def box_plot_of_home_prices_based_on_number_of_bedrooms(homes):
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Bedrooms', y='Price', data=homes)
    plt.title('Box Plot of Home Prices Based on Number of Bedrooms')
    plt.xlabel('Number of Bedrooms')
    plt.ylabel('Price ($)')
    st.pyplot()

def median_home_price_in_each_city(homes):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='City', y='Price', data=homes, estimator=np.median)
    plt.title('Median Home Price in Each City')
    plt.xlabel('City')
    plt.ylabel('Median Home Price ($)')
    plt.xticks(rotation=90)
    st.pyplot()

# Streamlit App

def main():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Sidebar filters
    st.sidebar.header("Filters")

    # Price slider
    price_slider = st.sidebar.slider("Filter by Price", min_value=float(homes['Price'].min()), max_value=float(homes['Price'].max()), value=(float(homes['Price'].min()), float(homes['Price'].max())))

    # County filter
    selected_county = st.sidebar.selectbox("Filter by County", ['All'] + homes['County'].unique().tolist())
    filtered_homes = homes.copy()

    if selected_county != 'All':
        filtered_homes = filtered_homes[filtered_homes['County'] == selected_county]

    # City filter
    selected_city = st.sidebar.selectbox("Filter by City", ['All'] + homes['City'].dropna().unique().tolist())
    if selected_city != 'All':
        filtered_homes = filtered_homes[filtered_homes['City'] == selected_city]

    # Bedrooms slider
    bedrooms_slider = st.sidebar.slider("Filter by Number of Bedrooms", min_value=int(homes['Bedrooms'].min()), max_value=int(homes['Bedrooms'].max()), value=(int(homes['Bedrooms'].min()), int(homes['Bedrooms'].max())))

    # Bathrooms slider
    bathrooms_slider = st.sidebar.slider("Filter by Number of Bathrooms", min_value=int(homes['Bathrooms'].min()), max_value=int(homes['Bathrooms'].max()), value=(int(homes['Bathrooms'].min()), int(homes['Bathrooms'].max())))

    # Apply filters
    filtered_homes = filtered_homes[(filtered_homes['Price'] >= price_slider[0]) & (filtered_homes['Price'] <= price_slider[1])]
    filtered_homes = filtered_homes[(filtered_homes['Bedrooms'] >= bedrooms_slider[0]) & (filtered_homes['Bedrooms'] <= bedrooms_slider[1])]
    filtered_homes = filtered_homes[(filtered_homes['Bathrooms'] >= bathrooms_slider[0]) & (filtered_homes['Bathrooms'] <= bathrooms_slider[1])]

    # Display filtered data
    st.subheader("Filtered Data")
    st.write(filtered_homes)

    # Display plots
    st.subheader('Distribution of Home Prices')
    distribution_of_home_prices(filtered_homes)

    st.subheader('Scatter Plot of Price vs. Square Footage by County')
    scatter_plot_price_vs_square_footage_by_county(filtered_homes)

    st.subheader('Boxplot of Home Prices by County')
    boxplot_of_home_prices_by_county(filtered_homes)

    st.subheader('Correlation Heatmap for Quantitative Variables')
    correlation_heatmap(filtered_homes)

    st.subheader('Average Price per Square Foot')
    average_price_per_square_foot_in_different_cities(filtered_homes)

    st.subheader('Box Plot of Home Prices Based on Number of Bedrooms')
    box_plot_of_home_prices_based_on_number_of_bedrooms(filtered_homes)

    st.subheader('Median Home Price in Each City')
    median_home_price_in_each_city(filtered_homes)

    st.subheader("GitHub Repository")
    github_link = "https://github.com/justinpferdner/semester_project"
    st.markdown(github_link, unsafe_allow_html=True)

if __name__ == "__main__":
    main()