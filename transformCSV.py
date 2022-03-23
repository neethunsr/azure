'''
Program to perform transformation on csv everytime a csv file is uploaded to blob storage
and upload it back to the blob storage.
'''

from azure.storage.blob import BlobClient, BlobServiceClient
import pandas as pd
from io import StringIO
from azure.servicebus import ServiceBusClient
from ast import literal_eval

connstr = '<queue connstr>'
queue_name = '<queue name>'
connectionstr = '<storage account connstr>'

with ServiceBusClient.from_connection_string(connstr) as client:
    with client.get_queue_receiver(queue_name) as receiver:
        for msg in receiver:
            strmsg = literal_eval(str(msg))
            BLOB_URL = strmsg['data']['url']
            print(BLOB_URL)
            receiver.complete_message(msg)

            # download file from blob url
            blob_client_from_url = BlobClient.from_blob_url(
                blob_url=BLOB_URL
                # credential=creds
            )
            blob_download = blob_client_from_url.download_blob()
            df = pd.read_csv(StringIO(blob_download.content_as_text()))
            print("Before Transformation:")
            print(df.head())
            
            df['full_name'] = df['first_name'] + ' ' + df['last_name']
            print("After Transformation:")
            print(df.head())

            filename = BLOB_URL.split('azuretest/')[1].split('.csv')[0]
            blobname = f'transform{filename}.csv'

            # saving the DataFrame as a CSV file
            csv_data = df.to_csv(blobname, index=True)

            blob_service_client = BlobServiceClient.from_connection_string(connectionstr)
            blob_client = blob_service_client.get_blob_client(container="azuretest", blob=blobname)
            with open(blobname, "rb") as data:
                blob_client.upload_blob(data)
            print(f'{blobname} uploaded successfully!')
