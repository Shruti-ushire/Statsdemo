import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# To import data iris
st.title("Iris Dashboard")
df = pd.read_csv('iris.csv')
st.dataframe(df)

# To make scatter lot
st.title("sepal Length and sepal width")
fig1, ax = plt.subplots()
ax.scatter(df.iloc[:,0],df.iloc[:,1])
plt.scatter(df.iloc[:,2],df.iloc[:,3])
st.pyplot(fig1)
#2 scatter plot
st.title("Scatter plot 2 ")
fig2,ax=plt.subplots()
ax.scatter(df.iloc[:,2],df.iloc[:,3])
st.pyplot(fig2)

#To make draw bar chart
t=df['species'].value_counts()
st.write(t)
st.title("bar chart")
st.bar_chart(t)

st.bar_chart(df[['sepal_length','sepal_width','petal_length','petal_width']])

# To make area chart
st.title("area chart")
st.area_chart(df.iloc[:,3])

#to make  Line chart
st.title("line chart")
st.line_chart(df.iloc[:,0])

# To make Histogram
st.title('Histogram')
fig,ax=plt.subplots()
ax.hist(df.iloc[:,1],color="red")
st.pyplot(fig)


fig4,ax=plt.subplots()
ax.boxplot(df.iloc[:,3])
st.pyplot(fig4)
