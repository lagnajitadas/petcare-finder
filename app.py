import streamlit as st
import pandas as pd
import folium
from urllib.parse import quote_plus
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
    df = pd.read_csv("data.csv")

    # Convert coordinates into numeric values
    df["latitude"] = pd.to_numeric(
        df["latitude"], errors="coerce"
    )
    df["longitude"] = pd.to_numeric(
        df["longitude"], errors="coerce"
    )

    return df


df = load_data()

# Search section
st.header("🔍 Find Pet Care Services")

search = st.text_input("Search by name, city or address")

category = st.selectbox(
    "Select Facility Category",
    ["All", "Hospital", "Clinic", "Medicine Shop"]
)

filtered = df.copy()

# Category filter
if category != "All":
    filtered = filtered[
        filtered["category"] == category
    ]

# Search filter
if search:
    mask = (
        filtered["name"].fillna("").str.contains(
            search, case=False
        )
        | filtered["city"].fillna("").str.contains(
            search, case=False
        )
        | filtered["address"].fillna("").str.contains(
            search, case=False
        )
    )

    filtered = filtered[mask]

# Results
st.header("📍 Available Pet Care Locations")
st.write(f"Found {len(filtered)} locations.")

if not filtered.empty:

    # Only use facilities with valid coordinates
    map_data = filtered.dropna(
        subset=["latitude", "longitude"]
    )

    if not map_data.empty:

        center = [
            map_data["latitude"].mean(),
            map_data["longitude"].mean()
        ]

        m = folium.Map(
            location=center,
            zoom_start=13
        )

        for _, row in map_data.iterrows():

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

    else:
        st.info(
            "Map coordinates are not available for these facilities yet."
        )
                # Facility details
    st.subheader("Facility Details")

    for _, row in filtered.iterrows():
        with st.container(border=True):

            st.write(f"### {row['name']}")
            st.write(f"Category: {row['category']}")
            st.write(f"City: {row['city']}")
            st.write(f"Location: {row['address']}")
            st.write(f"Contact: {row['phone']}")

            location_query = quote_plus(
                f"{row['name']}, {row['address']}, {row['city']}"
            )

            maps_url = (
                f"https://www.google.com/maps/search/?api=1&query={location_query}"
            )

            st.link_button(
                "📍 Open in Google Maps",
                maps_url
            )
     

else:
    st.warning("No matching facilities found.")

st.divider()

st.caption(
    "PetCare Finder | Built with Python, Streamlit and OpenStreetMap"
)

st.info(
    "Facility information should be verified before visiting."
)
