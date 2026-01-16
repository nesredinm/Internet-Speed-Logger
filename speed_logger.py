import speedtest
from datetime import datetime
import csv

# Initialize speedtest
st = speedtest.Speedtest(secure=True)

st.get_best_server()
# Run
download_speed = st.download()/1_000_000
upload_speed = st.upload()/1_000_000
ping = st.results.ping

# Timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("\n", download_speed,"\n",  upload_speed,"\n", ping, "\n", timestamp)

# Save ot csv
with open("internet_speed_log.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([timestamp, download_speed, upload_speed, ping])