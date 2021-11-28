#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coinbase Websocket
Created on Sun Nov 14 12:52:45 2021

@author: james
"""

import websocket, json
import pandas as pd
from datetime import timedelta


cbws = "wss://ws-feed.exchange.coinbase.com"
message = {"type": "subscribe",
               "channels":[{
                   "name": "ticker",
                   "product_ids": ["LINK-USD"]
                   }]
               }




def on_open(ws=cbws,message=message):
    global check
    print('websocket open')
    ws.send(json.dumps(message))

def on_message(ws=cbws,message=message):
    test = json.loads(message)
    t = test.get('time')
    t = pd.to_datetime(t,format='%Y-%m-%d %H:%M:%S') - timedelta(hours=5)
    s = t.strftime('%Y-%m-%d %H:%M:%S.%f')
    
    volusd = pd.to_numeric(test.get('price')) * pd.to_numeric(test.get('last_size'))
    #print(check)
    print("time: "+s[:-4]+", price: "+str(test.get('price'))+", size: "+str(test.get('last_size'))+", vol: "+str(volusd))

#def on_data(ws=cbws,message=message):
    
ws = websocket.WebSocketApp(cbws,on_message=on_message,on_open=on_open,header={"volume_24h":""})
ws.run_forever()
