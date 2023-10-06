# Influx

# Application Setup Guide

This guide will help you set up and run the application.

## Prerequisites

- Python 3.x installed
- Virtual environment tool (usually included with Python)

## Installation

1. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## InfluxDB Configuration

For InfluxDB connection, install it locally and replace your credentials with the following:

```python
token = "VIVslV7WE-3ynIKh95WnR3t3SsAltTM1wUh8rnv6beCuBfOMkKp1UYAu082bYF72Sc8is8R4mZgoJakr_9KK6w=="
org = "temp"
url = "http://localhost:8086"
bucket = "bulk_data"
 ```

## Running the Application

To run the application, execute the following command:
```python
python app.py
```

## API Endpoint

Access the following API endpoint once the application is running:

GET http://127.0.0.1:5000/api/bulk-data

Example Response

```python
[
    {
        "location": "Prague",
        "temperature": 0
    },
    {
        "location": "Prague",
        "temperature": 1
    },
    {
        "location": "Prague",
        "temperature": 2
    },
    {
        "location": "Prague",
        "temperature": 3
    },
    {
        "location": "Prague",
        "temperature": 4
    }
]
```
