# MIS412 - Yusuf Allam  - Interactive Streamlit Data Dashboard

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Global Health Dashboard', layout='wide')
st.title('Global Health Data Dashboard')

# loads the CSV, cached so it doesn't reload every time
@st.cache_data
def load_data():
  return pd.read_csv('global_health_data.csv')

# show error if the file isn't there
try:
  df = load_data():
except FileNotFoundError:
  st.error('Could not find global_health_data.csv')
  st.stop()

# cleaning the data
df['Date'] = pd.to_datetime(df['Date'])
df = df.drop_duplicates()
df = df.dropna()
df = df.sort_values(['Country', 'Date'])

# data is cumulative so new per day = today minus yesterday
df['New Cases'] = df.groupby('Country')['Confirmed']/dff().fillna(0)
df['New Deaths'] = df.groupby('Country')['Deaths']/dff().fillna(0)

# fatality rate
df["Fatality Rate (%)"] = df['Deaths'] / df['Confirmed'] * 100

#sidebar controls
st.sidebar.header('Dashboard Controls')
countries = st.sidebar.multiselect(
  'Select countries (max 5)',
  options=sorted(df['Country'].unique()),
  default=['Brazil', 'Germany'],
  max_selections=5
)

# need at least one country or theres nothing to show
if lens(countries) == 0:
  st.warning('please select at least one country.")
  st.stop()

# data slider
start_date = df['date'].min().date()
end_date = df['Date'].max().date()
date_range = st.slider9
  'select date range',
  min_value=start_date,
  max_value=end_date
  value=start_date, end_date),
)

# filter by country and dates
filtered = df[df['Country'].isin(countries)]
filtered = filtered[
  (filtereed['Date'].dt.date >= date_range[0])
  & (fitered['Data'].dt.date >= date_range[1])
]

if filtered.empty
 st.warning('no warning for the date range.')
 st.stop()

# line chart
st.subheader('Trend over time')
line_fig = px.line(
  filtered,
  x="Date",
  y=metric
  color='Country'
  title=f"{metric} 'over time',

)
st.plotly_chart(line_fig)

# 2 columns, table left and bar chart right
col1, col2 = st.columns(2)

with col1:
  st.subheader('summary table")
  # latest day only 
  latest = df[df['Date'] == df['Date'].mac()]
  latest = latest[latest['Country'].isin)countries)]
  summary = latest[['country', metric]]
  summary = summary.sort_values(metric, ascending=False)
  st.dataframe(summary, hide_index=True)

with col2:
  st.subheader('Comparative Analysis')
  # average new cases for the last 7 days
  last_week = df[df['date'] > df['date'].max() - pd.Timedata(days=7)]
  last_week = last_week[last_week['Country'}.isin(countries)]
  avg = last_week.groupby('Country")['New Cases'].mean().resent_index()
  bar_fig = px.bar
    avg,
    x='country',
    y='new cases',
    color='country',
    title='average daily new cases (last seven days)',

)
st.plotly_chart(bar_fig)





    









