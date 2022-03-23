#Pgm to read csv file from blob storage

from azure.storage.blob import BlobServiceClient
import pandas as pd
# import tables

STORAGEACCOUNTNAME = <storage_account_name>
# STORAGEACCOUNTKEY= <storage_account_key>
LOCALFILENAME = 'file.csv'
CONTAINERNAME = 'azuretest'
BLOBNAME = 'Sample100.csv'

# download from blob
blob_service = BlobServiceClient(
    account_url=<storage_account_url>)

blob_client_instance = blob_service.get_blob_client(
    CONTAINERNAME, BLOBNAME, snapshot=None)
    
with open(LOCALFILENAME, "wb") as my_blob:
    blob_data = blob_client_instance.download_blob()
    blob_data.readinto(my_blob)

# LOCALFILE is the file path
dataframe_blobdata = pd.read_csv(LOCALFILENAME)
print(dataframe_blobdata.head())
