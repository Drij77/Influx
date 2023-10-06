import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "VIVslV7WE-3ynIKh95WnR3t3SsAltTM1wUh8rnv6beCuBfOMkKp1UYAu082bYF72Sc8is8R4mZgoJakr_9KK6w=="
org = "temp"
url = "http://localhost:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket = "bulk_data"

write_api = write_client.write_api(write_options=SYNCHRONOUS)


def dump_data():
  for value in range(5):
   point = (
    Point("measurement1")
    .tag("location", "Prague")
    .field("temperature", value)
   )
   write_api.write(bucket=bucket, org="temp", record=point)
   time.sleep(1)  # separate points by 1 second

# query_api = write_client.query_api()
#
# query = """from(bucket: "bulk_data")
#  |> range(start: -10m)
#  |> filter(fn: (r) => r._measurement == "measurement1")"""
# tables = query_api.query(query, org="temp")
#
# for table in tables:
#   for record in table.records:
#     print(record)
