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
