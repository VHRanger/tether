import json
import pandas as pd
import requests
import time

ADDRESS = 'TAUN6FwrnwwmaEqYcckffC7wYmbaS6cBiX'
INITIAL_TIMESTAMP = int(time.time() * 1000)
LIMIT = 199

intial_url = f'https://api.trongrid.io/v1/accounts/{ADDRESS}/transactions/trc20'

headers = {
    'Content-Type': "application/json",
    'TRON-PRO-API-KEY': "8f6799a3-30ea-4d9a-a99b-6d9fa9b74730",
}

r = requests.get(
        intial_url, 
        headers=headers, 
        params={
            "limit":LIMIT,
            "max_timestamp": INITIAL_TIMESTAMP,
        }
)
print(json.loads(r.content)['meta'])


res = []
for i in range(20_000):
    try:
        rs = json.loads(r.content)
        res.append(rs)
        # get last time due to stupid API restriction
        this_time = rs['data'][-1]['block_timestamp']
        for d in rs['data']:
            if d['block_timestamp'] < this_time:
                this_time = d['block_timestamp']
        # Get next part of the response
        r = requests.get(
                intial_url, 
                headers=headers, 
                params={
                    "limit":LIMIT,
                    "max_timestamp": this_time,
                    "min_timestamp": this_time - 1_000_000_000,
                }
        )
    except:
        break

print(len(res))

# Save intermediate JSON result object
j = json.dumps(res, indent=4)
with open("binance.json", 'w') as f:
    f.write(j)


# Load JSON and convert transactions to df
with open("binance.json", "r") as f:
    j = json.load(f)

df = pd.DataFrame(sum([a['data'] for a in j], []))
df.to_csv("../binance.csv", index=False)
print(df.head())