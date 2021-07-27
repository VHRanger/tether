import json
import pandas as pd
import requests
import time

USDC_ADDR = '0x55fe002aeff02f77364de339a1292923a15844b8'
API_KEY = '5B22PBXZ27QCXWJZP12PEMXG3P7HMJQNM5'

base_query = "https://api.etherscan.io/api?module=account&action=tokentx"
base_query += f"&address={USDC_ADDR}"
base_query += f"&apikey={API_KEY}"

CURRENT_BLOCK = 0
res = []
i = 0
while True:
    r = requests.get(
            base_query + f"&startblock={CURRENT_BLOCK}",
    )
    r = json.loads(r.content)
    if len(r['result']) == 0: break
    CURRENT_BLOCK = r['result'][-1]['blockNumber']
    res.append(r)
    if i > 30: break
    time.sleep(0.25) # API rate limits
print(i)
print(len(res))

# Save intermediate JSON result object
j = json.dumps(res, indent=4)
with open("data/usdc/usdc.json", 'w') as f:
    f.write(j)
    
# Load JSON and convert transactions to df
with open("data/usdc/usdc.json", "r") as f:
    j = json.load(f)

uc = pd.DataFrame(sum([a['result'] for a in j], []))
uc.to_csv("data/usdc.csv", index=False)