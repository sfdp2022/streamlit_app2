import streamlit as st
import pandas as pd
import plotly.express as px

bar_col, pie_col = st.columns(2)  # add columns

# Read in datasets - boy & girl names England & Wales 2021
all_nms_grls = pd.read_excel(r"..\streamlit_app2\data\2021girlsnames.xlsx", 
                sheet_name="6", skiprows=6)
    
all_nms_boys = pd.read_excel(r"..\streamlit_app2\data\2021boysnames.xlsx", 
                sheet_name="6", skiprows=6)

# Concat datasets & createing sort/filters for visualisations                          
df = pd.concat((all_nms_grls,all_nms_boys), ignore_index=True)

az_sort = df.sort_values(by=["Rank", "Name"])
girls_sort = all_nms_grls.sort_values(by="Name")
boys_sort = all_nms_boys.sort_values(by="Name")

st.sidebar.header("Pick names to compare.")  # Sidebar for selections
girl_select = st.sidebar.multiselect("Girl names.", options=(girls_sort["Name"]))

boy_select = st.sidebar.multiselect("Boy names", options=(boys_sort["Name"]))

def filt_all(az_sort): 
        names = az_sort[az_sort["Name"].isin(girl_select + boy_select)]  # Can't figure out how to add boy_select!
        return names

def bar_all(az_sort):
        bar_ch = px.bar(az_sort, x="Count", y="Name", color="Name", title="Bar chart",
                color_discrete_sequence=["#12436D", "#28A197", "#801650", "#F46A25", "#3D3D3D", "#A285D1"])

        st.plotly_chart(bar_ch)

def pie(az_sort):
        pie_ch = px.pie(az_sort, values="Count", names="Name",
                hole=0.5, title="Pie chart", 
                color_discrete_sequence=["#12436D", "#28A197", "#801650", "#F46A25", "#3D3D3D", "#A285D1"])
        
        st.plotly_chart(pie_ch)

# Dashboard visualisations
st.title("2021 England & Wales baby name dashboard")

pick_names = filt_all(az_sort)

if pick_names.empty:
        st.write("No data selected")
else:
        bar_all(pick_names)
        pie(pick_names)

#