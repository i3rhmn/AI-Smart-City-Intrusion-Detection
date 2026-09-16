import streamlit as st
import pandas as pd
import joblib
from scapy.all import sniff, TCP, UDP, Raw, get_if_list

# Load the trained best model
model = joblib.load("it8520_model.pkl")

st.title("IT8520 Smart City AI Threat Detection System")

st.write("""
This Threat Detection System captures live packets from a selected network interface
and classifies them as normal or attack using the trained machine learning model.
""")

# Get available network interfaces
interfaces = get_if_list()

selected_interface = st.selectbox("Select Network Interface", interfaces)

packet_count = st.number_input(
    "Number of packets to capture",
    min_value=1,
    max_value=5000,
    value=50
)

def extract_features(pkt):
    src_port = 0
    dst_port = 0
    protocol = "OTHER"
    packet_length = len(pkt)
    payload_size = 0

    if TCP in pkt:
        protocol = "TCP"
        src_port = pkt[TCP].sport
        dst_port = pkt[TCP].dport

    elif UDP in pkt:
        protocol = "UDP"
        src_port = pkt[UDP].sport
        dst_port = pkt[UDP].dport

    if Raw in pkt:
        payload_size = len(pkt[Raw].load)

    return {
        "src_port": src_port,
        "dst_port": dst_port,
        "protocol": protocol,
        "packet_length": packet_length,
        "payload_size": payload_size
    }

if st.button("Start Capture and Classify"):
    st.info(f"Capturing {packet_count} packets on interface: {selected_interface}")

    packets = sniff(
        iface=selected_interface,
        count=int(packet_count),
        timeout=30
    )

    rows = []

    for pkt in packets:
        features = extract_features(pkt)
        rows.append(features)

    if len(rows) == 0:
        st.warning("No packets captured.")
    else:
        live_df = pd.DataFrame(rows)

        predictions = model.predict(live_df)

        live_df["prediction"] = predictions

        st.subheader("Live Packet Classification Results")
        st.dataframe(live_df)

        st.subheader("Detection Summary")
        st.write(live_df["prediction"].value_counts())

        attack_count = (live_df["prediction"] == "attack").sum()
        normal_count = (live_df["prediction"] == "normal").sum()

        if attack_count > normal_count:
            st.error("Threat Status: Malicious traffic detected")
        else:
            st.success("Threat Status: Traffic appears normal")