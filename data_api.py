from flask import Blueprint, jsonify, current_app
from influxdb_client_3 import InfluxDBClient3
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from data_dump import dump_data
# Create a Blueprint object with a unique name 'data_bp'
data_bp = Blueprint('data', __name__)



token = "VIVslV7WE-3ynIKh95WnR3t3SsAltTM1wUh8rnv6beCuBfOMkKp1UYAu082bYF72Sc8is8R4mZgoJakr_9KK6w=="
org = "temp"
url = "http://localhost:8086"



bucket = "bulk_data"



def convert_flux_table_to_json(flux_table):
    data = []
    if not flux_table:
        dump_data()
    for row in flux_table:

        for record in row.records:
                print(record)
                data_point = {
                    'location': record['location'],
                    'temperature': record['_value'],
                    # Add more fields as needed
                }
                data.append(data_point)
    return data


@data_bp.route('/api/bulk-data', methods=['GET'])
def get_bulk_data():
    try:
        # Connect to the InfluxDB database using the configured settings
        # client = current_app.config['INFLUXDB_CLIENT']
        write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
        query_api = write_client.query_api()
        # Implement the logic to query bulk data from InfluxDB
        query = """from(bucket: "bulk_data")
         |> range(start: -10m)
         |> filter(fn: (r) => r._measurement == "measurement1")"""

        data = query_api.query(query, org="temp")
        result=convert_flux_table_to_json(data)
        # Extract the data points from the query result
        # data_points = list(result.get_points())

        # Handle any necessary data manipulation or formatting
        # Example: formatted_data = format_data(data_points)

        # Return the data as a JSON response using jsonify
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return an error response if something goes wrong
