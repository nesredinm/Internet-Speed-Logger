import speedtest
from datetime import datetime

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