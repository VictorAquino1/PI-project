# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
from unittest import result
import uuid
import time
from datetime import timedelta, datetime
from azure.iot.device import IoTHubDeviceClient
from azure.iot.device import Message
import json
import random
import numpy as np

def weighted_speed():
    # A random weighted result is generated.
    numberList = [random.randint(20,80), random.randint(81,150)]
    results = np.random.choice(numberList, 1, replace = False, p=[0.70, 0.30])
    for resultsStr in results:
        results.astype(int)
        return resultsStr

def weighted_temp():
    # A random weighted result is generated.
    numberList = [random.randint(10,15), random.randint(16,28)]
    results = np.random.choice(numberList, 1, replace = False, p=[0.30, 0.70])
    for resultsStr in results:
        results.astype(int)
        return resultsStr

def main():

    # Olá Aluno(a), substitua o valor da string abaixo pela chave de conexão do dispositivo criado no IoT Hub
    #conn_str = "HostName=victor02211061.azure-devices.net;DeviceId=victor02211061;SharedAccessKey=IipYpYWBcZ5+lBVJZHZ3G0qyUD9Gkd7tlo+cWxOzpM0="
    
    conn_str = "HostName=felipe01211037.azure-devices.net;DeviceId=dispositivo01211037;SharedAccessKey=B9pUpMEtnrE56dwcVx5rPoHkfoHW9p78vuhYrv9Zt+Q="
    # The client object is used to interact with your Azure IoT hub.
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    print("IoTHub Device Client Recurring Telemetry Sample")
    print("Press Ctrl+C to exit")
    try:
        # Connect the client.
        device_client.connect()

        # Send recurring telemetry
        i = 0
        while True:
            i += 1
            windspeed = weighted_speed()
            temp = weighted_temp()
            dateTime = datetime.now()
            msg= {"Id": i, "Time:": str(dateTime), "WSpeed": int(windspeed), "Temp": int(temp)}
            msg = Message(json.dumps(msg))
            msg.custom_properties["tornado-warning"] = "yes" if windspeed >= 81 else "no"
            msg.message_id = uuid.uuid4()
            msg.correlation_id = "correlation-1234"
            msg.content_encoding = "utf-8"
            msg.content_type = "application/json"
            print(f"sending message #{i}: body: {msg}, Alert: {str(msg.custom_properties['tornado-warning'])}")
            device_client.send_message(msg)
            time.sleep(2)
    except KeyboardInterrupt:
        print("User initiated exit")
    except Exception:
        print("Unexpected exception!")
        raise
    finally:
        device_client.shutdown()


if __name__ == "__main__":
    main()