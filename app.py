import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="PetCare Finder",
    page_icon="🐾",
    layout="wide"
)

st.title("🐾 PetCare Finder")
st.subheader("Veterinary Hospitals, Clinics & Pet Medicine Shops")

st.write(
    "Find veterinary hospitals, clinics and pet medicine shops near you."
)

# Search section
search = st.text_input("🔍 Search by location")

# Category filter
category = st.selectbox(
    "Select Facility Type",
    [
        "All",
        "Veterinary Hospital",
        "Veterinary Clinic",
        "Pet Medicine Shop"
    ]
)

# Initial map
m = folium.Map(
    location=[22.975, 88.434],
    zoom_start=13
)

st.subheader("📍 Explore PetCare Locations")

st_folium(m, width=1100, height=500)

st.info(
    "PetCare Finder is currently under development."
)

st.caption("Made with ❤️ for pet owners.")
