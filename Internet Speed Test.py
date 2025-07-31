import speedtest
st = speedtest.Speedtest()
print("Download:", round(st.download()/10**6, 2), "Mbps")
print("Upload:", round(st.upload()/10**6, 2), "Mbps")
