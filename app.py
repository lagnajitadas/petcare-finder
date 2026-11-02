import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="PetCare Finder",
    page_icon="🐾",
    layout="wide"
)

st.title("🐾 PetCare Finder")
st.subheader("Find Veterinary Hospitals, Clinics & Pet Medicine Shops")

st.write(
    "Your one-stop platform to discover pet healthcare facilities."
)

# Load location data
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

df = load_data()

# Search
st.header("🔍 Find Pet Care Services")

search = st.text_input("Search by name, city or address")

# Category filter
category = st.selectbox(
    "Select Facility Category",
    [
        "All",
        "Hospital",
        "Clinic",
        "Medicine Shop"
    ]
)

filtered = df.copy()

if category != "All":
    filtered = filtered[
        filtered["category"] == category
    ]

if search:
    mask = (
        filtered["name"].str.contains(
            search, case=False, na=False
        )
        | filtered["city"].str.contains(
            search, case=False, na=False
        )
        | filtered["address"].str.contains(
            search, case=False, na=False
        )
    )

    filtered = filtered[mask]

# Results
st.header("📍 Available Pet Care Locations")

st.write(f"Found {len(filtered)} locations.")

if not filtered.empty:

    # Interactive map
    center = [
        filtered["latitude"].mean(),
        filtered["longitude"].mean()
    ]

    m = folium.Map(
        location=center,
        zoom_start=13
    )

    for _, row in filtered.iterrows():

        popup = f"""
        <b>{row['name']}</b><br>
        Category: {row['category']}<br>
        City: {row['city']}<br>
        Address: {row['address']}<br>
        Phone: {row['phone']}
        """

        folium.Marker(
            location=[
                row["latitude"],
                row["longitude"]
            ],
            popup=popup,
            tooltip=row["name"]
        ).add_to(m)

    st_folium(
        m,
        width=None,
        height=500
    )

    # Facility information
    st.subheader("Facility Details")

    for _, row in filtered.iterrows():

        with st.container(border=True):

            st.write(f"### {row['name']}")
            st.write(f"Category: {row['category']}")
            st.write(f"Location: {row['address']}")
            st.write(f"Contact: {row['phone']}")

else:
    st.warning("No matching facilities found.")

st.divider()

st.caption(
    "PetCare Finder | Built with Python, Streamlit and OpenStreetMap"
)

st.info(
    "Sample locations are for demonstration only. "
    "Verify facility details before visiting."
)
