# 🐾 PetCare Finder – Veterinary & Pet Medicine Locator

### Find Veterinary Hospitals, Clinics & Pet Medicine Shops in One Place!

PetCare Finder is a location-based web application designed to help pet owners discover veterinary hospitals, clinics, and pet medicine shops in Kalyani, West Bengal.

The platform provides a simple way to search pet healthcare facilities, explore available information, and navigate to locations using Google Maps.

🌐 **Live Demo:** https://petcare-finder-lagnajita.streamlit.app

---

## 📌 Project Overview

Finding reliable veterinary services and pet medicine shops can sometimes be challenging, especially in unfamiliar locations.

PetCare Finder aims to simplify this process by providing a centralized platform where pet owners can discover nearby pet healthcare facilities.

The application combines search functionality, category-based filtering, facility information, and map-based navigation in one user-friendly interface.

## ✨ Key Features

* 🔍 **Search Functionality:** Search facilities by name, city, or address.
* 🏥 **Category Filtering:** Filter veterinary hospitals, clinics, and medicine shops.
* 📍 **Location Details:** View facility names, addresses, and available contact information.
* 🗺️ **Interactive Mapping:** Display facility markers using Folium and OpenStreetMap when coordinates are available.
* 🧭 **Google Maps Navigation:** Open facility locations directly in Google Maps.
* 📊 **Facility Count:** View the number of matching locations.
* 💻 **User-Friendly Interface:** Simple and responsive Streamlit interface.

## 🛠️ Technology Stack

| Technology                | Purpose                                 |
| ------------------------- | --------------------------------------- |
| Python                    | Core programming language               |
| Streamlit                 | Web application framework               |
| Pandas                    | Data handling and processing            |
| Folium                    | Interactive map visualization           |
| OpenStreetMap             | Map data                                |
| Streamlit-Folium          | Streamlit and Folium integration        |
| GitHub                    | Version control and source code hosting |
| Streamlit Community Cloud | Application deployment                  |

## 📂 Project Structure

```text
petcare-finder/
│
├── app.py              # Main Streamlit application
├── data.csv            # Pet care facility dataset
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## ⚙️ Installation & Setup

Follow these steps to run PetCare Finder locally.

### 1. Clone the Repository

```bash
git clone https://github.com/lagnajitadas/petcare-finder.git
```

### 2. Navigate to the Project Directory

```bash
cd petcare-finder
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📍 Dataset

The project uses a CSV-based dataset (`data.csv`) containing pet care facility information.

The dataset
