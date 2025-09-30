import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Load demo structured dataset
# -------------------------------
audiogram_df = pd.read_csv(r"C:\Users\skim\OneDrive - AAO-HNS\Documents\Reg-ent\Research Projects\Audiogram\Audiogram_DF.csv")

# -------------------------------
# Streamlit App UI
# -------------------------------
st.title("🎧 Audiogram AI Transformation Demo")

st.markdown("""
This demo shows how we can take **unstructured audiogram images** 
and transform them into **structured, analyzable data** using AI.
""")

# Sidebar filter
category = st.sidebar.multiselect(
    "Filter by Hearing Category:",
    options=audiogram_df["Category"].unique(),
    default=audiogram_df["Category"].unique()
)

# Filter dataset
filtered_df = audiogram_df[audiogram_df["Category"].isin(category)]

# Show dataset
st.subheader("📊 Structured Audiogram Dataset")
st.dataframe(filtered_df, use_container_width=True)

# -------------------------------
# Demo Mode (Before vs After)
# -------------------------------
st.subheader("✨ Demo Mode: From Image to Structured Data")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Unstructured Audiogram (Image/PDF Scan)**")
    # Example image - replace with your own sample audiogram image
    st.image("sample_audiogram.png", caption="Raw Audiogram (Unstructured)")

with col2:
    st.markdown("**Structured Data + Recreated Plot**")

    # Select patient to demo
    patient_id = st.selectbox("Select PatientID:", filtered_df["PatientID"].unique())
    patient_data = filtered_df[filtered_df["PatientID"] == patient_id].iloc[0]

    frequencies = [500, 1000, 2000, 4000]
    right_ear = [
        patient_data["Right_500Hz"],
        patient_data["Right_1000Hz"],
        patient_data["Right_2000Hz"],
        patient_data["Right_4000Hz"],
    ]
    left_ear = [
        patient_data["Left_500Hz"],
        patient_data["Left_1000Hz"],
        patient_data["Left_2000Hz"],
        patient_data["Left_4000Hz"],
    ]

    # Plot recreated audiogram
    fig, ax = plt.subplots()
    ax.plot(frequencies, right_ear, 'ro-', label="Right Ear")
    ax.plot(frequencies, left_ear, 'bx-', label="Left Ear")
    ax.invert_yaxis()
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Hearing Level (dB HL)")
    ax.set_title(f"Recreated Audiogram for Patient {patient_id}")
    ax.legend()
    st.pyplot(fig)

    # Show structured results
    st.write({
        "PTA_Right": patient_data["PTA_Right"],
        "PTA_Left": patient_data["PTA_Left"],
        "SRT_Right": patient_data["SRT_Right"],
        "SRT_Left": patient_data["SRT_Left"],
        "WRS_Right": patient_data["WRS_Right"],
        "WRS_Left": patient_data["WRS_Left"],
        "Tymp_Right": patient_data["Tymp_Right"],
        "Tymp_Left": patient_data["Tymp_Left"],
    })
