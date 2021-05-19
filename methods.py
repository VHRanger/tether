import json
import os
import matplotlib.dates as md
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate_known_addresses():
    """
    generate Known address dict from existing dict
    """
    files = [x for x in os.listdir("whaleapi") if 'json' in x]
    res = []
    for fname in files:
        with open("whaleapi/" + fname) as f:
            res.append(json.load(f)['transactions'])
    res = sum(res, [])
    df = pd.DataFrame(res)
    df['from_owner'] = df['from'].apply(lambda x : x.get('owner', ""))
    df['to_owner'] = df['to'].apply(lambda x : x.get('owner', ""))
    df['from_type'] = df['from'].apply(lambda x : x.get('owner_type', ""))
    df['to_type'] = df['to'].apply(lambda x : x.get('owner_type', ""))
    df['from_addr'] = df['from'].apply(lambda x : x.get('address', ""))
    df['to_addr'] = df['to'].apply(lambda x : x.get('address', ""))
    df['timestamp'] = pd.to_datetime(df.timestamp, unit='s')
    df = df.drop(columns=['hash', 'from', 'to', 'transaction_count'])

    # known addresses
    # Mix of whaleAPI labels and manual labels
    with open("data/known_addresses.json", 'r') as f:
        addr = json.load(f)

    for k in addr:
        df.loc[df.from_addr == k, 'from_owner'] = addr[k]
        df.loc[df.to_addr == k, 'to_owner'] = addr[k]


    #### Make dict of known addresses
    idx = df.from_owner.str.len() > 0
    idx2 = df.to_owner.str.len() > 0
    d1 = dict(zip(df.loc[idx].from_addr, df.loc[idx].from_owner))
    d2 = dict(zip(df.loc[idx2].to_addr, df.loc[idx2].to_owner))
    known_addresses = {}
    for d in (d1, d2, addr): # you can list as many input dicts as you want here
        for key, value in d.items():
            known_addresses[key] = value

    return known_addresses