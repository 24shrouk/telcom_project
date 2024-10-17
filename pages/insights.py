

import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import numpy as np


def main():
    # Title
    st.title("📊 Customer Churn Insights")
   # def app():
    # Load your Telco Customer Churn data
    df = pd.read_csv('projectdata.csv')

    # Pie Chart: Churn Distribution
    st.subheader("Churn Distribution")
    churn_counts = df['Churn'].value_counts()
    fig = px.pie(churn_counts, values=churn_counts.values, names=churn_counts.index, title="Churn Distribution")
    st.plotly_chart(fig)

    # Bar Chart: Churn by Gender and Internet Service
    st.subheader("Churn by Gender and Internet Service")
    df_gender_internet = df.groupby(['gender', 'InternetService', 'Churn']).size().reset_index(name='counts')
    fig = px.bar(df_gender_internet, x="InternetService", y="counts", color="Churn", barmode="group", facet_col="gender", title="Churn by Gender and Internet Service")
    st.plotly_chart(fig)

    # Box Plot: Tenure vs Churn
    st.subheader("Box Plot of Tenure vs Churn")
    fig = px.box(df, x='Churn', y='tenure', title="Tenure Distribution by Churn")
    st.plotly_chart(fig)

    # Distribution Plot: Monthly Charges by Churn
    st.subheader("Distribution of Monthly Charges by Churn")
    fig = px.histogram(df, x="MonthlyCharges", color="Churn", marginal="rug", title="Monthly Charges Distribution by Churn")
    st.plotly_chart(fig)

    # Correlation Heatmap
    st.subheader("Heatmap of Correlations")
    corr = df.corr(numeric_only=True)
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig_corr = sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm')
    st.pyplot(fig_corr.figure)

    # Additional Charts
    # Contract Type Distribution
    st.subheader("Contract Type Distribution")
    contract_counts = df['Contract'].value_counts()
    fig = px.pie(contract_counts, values=contract_counts.values, names=contract_counts.index, title="Contract Type Distribution")
    st.plotly_chart(fig)

    # Stacked Bar Chart for Churn and Phone Service
    st.subheader("Churn Distribution w.r.t. Phone Service")
    df_phone_service = df.groupby(['PhoneService', 'Churn']).size().reset_index(name='counts')
    fig = px.bar(df_phone_service, x="PhoneService", y="counts", color="Churn", barmode="stack", title="Churn by Phone Service")
    st.plotly_chart(fig)

    # Senior Citizens Churn Rates
    st.subheader("Churn Distribution w.r.t Senior Citizen")
    senior_counts = df.groupby(['SeniorCitizen', 'Churn']).size().reset_index(name='counts')
    fig = px.bar(senior_counts, x="SeniorCitizen", y="counts", color="Churn", title="Churn by Senior Citizen")
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
