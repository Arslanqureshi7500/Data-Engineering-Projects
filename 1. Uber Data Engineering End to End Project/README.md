# Uber Data Analytics | Modern Data Engineering GCP Project

## Introduction

The goal of this project is to perform data analytics on Uber data using various tools and technologies, including GCP Storage, Python, Compute Instance, Mage Data Pipeline Tool, BigQuery, and Looker Studio.

## Architecture 
<img src="architecture.jpg">

## Technology Used
- Programming Language - Python

Google Cloud Platform
1. Google Storage
2. Compute Instance 
3. BigQuery
4. Looker Studio

Modern Data Pipeine Tool - https://www.mage.ai/

Contibute to this open source project - https://github.com/mage-ai/mage-ai


## Dataset Used
TLC Trip Record Data
Yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts. 

Here is the dataset used in the video - https://github.com/darshilparmar/uber-etl-pipeline-data-engineering-project/blob/main/data/uber_data.csv

More info about dataset can be found here:
1. Website - https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
2. Data Dictionary - https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf

## Data Model
<img src="data_model.jpeg">
---

Here's how to **safely install everything in a Python virtual environment**, avoiding system-wide installations.

---

### ✅ **Step-by-Step: Install Everything in a Virtual Environment**

#### 1. **Update apt and install system-level dependencies (outside virtual env)**  
These are required only once and **must be run as sudo**:
```bash
sudo apt-get update
sudo apt-get install python3-venv python3-distutils python3-apt wget
```

#### 2. **Create & activate virtual environment**
```bash
python3 -m venv myenv
source myenv/bin/activate
```

> Now you're working *inside* the virtual environment — any Python packages installed now will **not** affect your system Python.

#### 3. **Install pip (if not already included in the venv)**
Usually comes preinstalled, but to ensure:
```bash
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```

---

### ✅ **Install Required Python Packages in venv (no `sudo`)**

Once you're inside the virtual environment (`myenv` is active):

```bash
pip install mage-ai
pip install pandas
pip install google-cloud
pip install google-cloud-bigquery
```

> ✅ Note: Don't use `sudo` inside a virtual environment. It's unnecessary and may break things.

---

### 🔍 Check Installed Packages (Optional)
```bash
pip list
```

---

### ✅ Tip: Reuse the environment later
Just activate it again whenever you need it:
```bash
source myenv/bin/activate
```
