import speedtest

teste = speedtest.Speedtest()

print("Testando a velocidade da sua internet. Aguarde...")
velocidade_download = teste.download() / 1_000_000  
velocidade_upload = teste.upload() / 1_000_000      
ping = teste.results.ping

print(f"Velocidade de Download: {velocidade_download:.2f} Mbps")
print(f"Velocidade de Upload: {velocidade_upload:.2f} Mbps")
print(f"Ping: {ping:.2f} ms")
