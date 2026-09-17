# AI Smart City Intrusion Detection

AI-powered Intrusion Detection System (IDS) developed for the IT8520 Digital Transformation course at Bahrain Polytechnic.

The project combines an isolated virtual smart city network, network traffic generation, feature engineering, supervised machine learning, and real-time packet classification to detect normal and malicious network traffic.

# Project Overview

This project focuses on developing an intelligent Intrusion Detection System for a simulated smart city network.

An isolated laboratory environment was created using Oracle VirtualBox with four virtual machines:

- Kali Linux - Attacker
- Windows Server 2022 - Target Web Server
- Windows 10 - Normal Client
- Ubuntu Monitor Server - Traffic Monitoring and IDS

The virtual machines were connected through an isolated VirtualBox Internal Network.

The project generated both normal and malicious traffic, captured the traffic as PCAP files, converted the packet captures into structured data, trained multiple machine learning models, and deployed a real-time IDS application.

# Project Objectives

- Build an isolated smart city network environment
- Generate normal and malicious network traffic
- Capture network traffic using tcpdump
- Convert PCAP files into structured datasets
- Perform feature selection and feature engineering
- Train and evaluate machine learning models
- Develop a real-time Intrusion Detection System
- Capture live packets using Scapy
- Classify traffic as normal or attack
- Display detection results through a Streamlit interface

# Network Lab

The project used an isolated VirtualBox Internal Network named:

IT8520_SmartCityLab

Network:

192.168.82.0/24

The four virtual machines were assigned the following addresses:

| Machine | IP Address | Role |
|---|---|---|
| Kali Linux | 192.168.82.10 | Attacker |
| Windows Server 2022 | 192.168.82.20 | Target Web Server |
| Windows 10 | 192.168.82.30 | Normal Client |
| Ubuntu Monitor Server | 192.168.82.40 | Traffic Capture and IDS |

The isolated design allowed traffic generation and monitoring without affecting the physical network.

# Network Traffic

The dataset was generated using normal traffic and three simulated attack categories.

| Traffic Type | Packets |
|---|---:|
| Normal Traffic | 50,000 |
| SYN Flood | 17,000 |
| UDP Flood | 17,000 |
| HTTP Flood | 16,000 |
| Total | 100,000 |

The traffic was captured on the Ubuntu monitoring server using tcpdump.

# Dataset Preparation

Raw PCAP files cannot be directly used by the machine learning models.

The captured packets were processed using Python, Scapy, and pandas.

The processing workflow was:

PCAP Files
→ Packet Extraction
→ Feature Engineering
→ Data Cleaning
→ CSV Dataset
→ Machine Learning

The resulting dataset contained:

- 100,000 records
- 26 columns

The cleaned dataset was stored as:

smartcity_clean_dataset_100k.csv

# Feature Engineering

The dataset included packet-level and flow-level information.

Important features included:

- src_port
- dst_port
- protocol
- packet_length
- payload_size
- tcp_flags
- flow_packet_count
- flow_total_bytes
- flow_duration
- flow_packet_rate
- flow_byte_rate
- flow_syn_count
- flow_ack_count
- flow_rst_count
- flow_fin_count
- flow_udp_count
- flow_http_count

Feature engineering was used to represent packet characteristics and network traffic behavior.

# Feature Selection

For machine learning training, a smaller set of realistic packet-level features was selected.

The final model used:

- src_port
- dst_port
- protocol
- packet_length
- payload_size

IP addresses, timestamps, attack-specific labels, and flow identifiers were excluded from model training to reduce the possibility of data leakage and unrealistic accuracy.

# Data Labeling

Two labels were maintained in the dataset.

Binary label:

- normal
- attack

Detailed attack category:

- normal
- syn_flood
- udp_flood
- http_flood

The binary label was used as the target variable for the machine learning classification task.

# Data Preprocessing

The machine learning pipeline included preprocessing before model training.

Categorical features such as protocol were converted using One-Hot Encoding.

Numerical features were scaled using StandardScaler.

The preprocessing pipeline was applied consistently during both training and testing.

# Machine Learning Models

Five supervised machine learning algorithms were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

# Model Evaluation

The models were compared based on their classification performance.

Random Forest demonstrated strong and stable performance, while SVM also performed effectively in separating normal and attack traffic.

Logistic Regression provided a useful baseline.

Decision Tree showed some signs of overfitting.

KNN performed reasonably well but was sensitive to feature scaling and neighbor selection.

The evaluation focused on realistic packet-level features rather than directly using information that could reveal the traffic class.

# Real Time IDS

A real-time Intrusion Detection System was developed using:

- Python
- Streamlit
- Scapy
- pandas
- joblib
- scikit-learn

The IDS runs on the Ubuntu Monitor Server.

The trained machine learning model is loaded from:

it8520_model.pkl

The real-time application is implemented in:

ai_threat_detection_system.py

# IDS Features

The real-time IDS extracts the same five features used during model training:

- src_port
- dst_port
- protocol
- packet_length
- payload_size

These features are extracted from live packets and passed to the trained machine learning model.

# IDS Workflow

The IDS operates using the following workflow:

1. Open the Streamlit web interface
2. Load the trained model
3. Select the network interface
4. Select the number of packets
5. Capture live packets using Scapy
6. Extract packet features
7. Store features in a pandas DataFrame
8. Send features to the trained model
9. Classify packets as normal or attack
10. Display packet-level results
11. Display the detection summary
12. Display the threat status

# IDS User Interface

The Streamlit interface allows the user to:

- Select the network interface
- Select the number of packets
- Start packet capture
- View packet classification results
- View detection statistics
- View the overall threat status

The application includes a:

Start Capture and Classify

button for starting live packet capture and classification.

# Project Technologies

| Technology | Purpose |
|---|---|
| Python | Data processing, machine learning, and IDS development |
| Oracle VirtualBox | Virtual laboratory environment |
| Kali Linux | Attack simulation |
| Windows Server 2022 | IIS target web server |
| Windows 10 | Normal network client |
| Ubuntu | Monitoring and IDS server |
| tcpdump | Network traffic capture |
| Scapy | Packet extraction and live packet capture |
| pandas | Dataset processing |
| scikit-learn | Machine learning |
| Streamlit | IDS web interface |
| joblib | Machine learning model loading |
| Google Colab | Dataset processing and model development |
| Matplotlib | Results visualization |

# My Contribution

This was a group project, and my assigned contribution was 20% of the overall project workload.

I completed 100% of my assigned workload.

My main contributions were:

- Feature Selection and Engineering Justification
- IDS Development
- Real-Time Threat Detection
- Report Structure
- References

I contributed to the implementation and testing of the real-time IDS, including the feature extraction and classification workflow.

# Skills Demonstrated

- Intrusion Detection Systems
- Machine Learning
- Network Security
- Network Traffic Analysis
- Feature Engineering
- Feature Selection
- Python
- Scapy
- Streamlit
- scikit-learn
- pandas
- tcpdump
- VirtualBox
- Linux
- Windows Server
- Packet Analysis
- Cybersecurity
- Real-Time Threat Detection

# Project Architecture

The overall project follows this architecture:

Virtual Smart City Network
→ Traffic Generation
→ PCAP Capture
→ Feature Extraction
→ Dataset Creation
→ Feature Selection
→ Data Preprocessing
→ ML Training
→ Model Evaluation
→ Model Export
→ Real-Time Packet Capture
→ Feature Extraction
→ ML Classification
→ IDS Results

# Future Improvements

Potential future improvements include:

- Adding more attack categories
- Increasing dataset diversity
- Incorporating deep learning models
- Improving real-time detection performance
- Deploying the IDS in a larger network environment
- Adding automated response mechanisms
- Integrating alerting and logging capabilities

# Project Report

To view the full project report, you can download it here:

[Download the IT8520 Smart City AI IDS Project Report](report/Project_IT8520.docx)

# Academic Information

Course: IT8520 - Digital Transformation

Institution: Bahrain Polytechnic

Project Topic: Intelligent Intrusion Detection System for Smart City Networks

# Disclaimer

This project was developed in an isolated virtual laboratory for academic and educational purposes.

All simulated network traffic and security testing were performed within the controlled lab environment.
