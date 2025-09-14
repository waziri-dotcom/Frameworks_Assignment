import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers (metadata.csv)")

@st.cache_data
def load_data():
    return pd.read_csv("data/metadata.csv", low_memory=False)

df = load_data()
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

st.subheader("Sample of Data")
st.write(df[['title', 'journal', 'publish_time']].head())

st.subheader("Publications Over Time")
year_counts = df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax, color="skyblue")
ax.set_title("Publications by Year")
st.pyplot(fig)

st.subheader("Top Journals")
top_journals = df['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax, palette="muted")
ax.set_title("Top 10 Journals")
st.pyplot(fig)

st.subheader("Word Cloud of Titles")
titles = " ".join(df["title"].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(titles)
fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
