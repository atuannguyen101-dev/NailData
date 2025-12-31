"""
Upload MLTable to Azure ML using Python SDK
Run: pip install azure-ai-ml azure-identity mltable azureml-dataprep[pandas]
Then: python upload_mltable.py
"""
import mltable
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
import time

# Your Azure ML workspace details - UPDATE THESE
SUBSCRIPTION_ID = "64eb24fa-6f44-446f-8b8d-bc20193be063"  # from your screenshot
RESOURCE_GROUP = "tuan"  # update this
WORKSPACE_NAME = "azureml"  # update this

# Connect to workspace
try:
    credential = DefaultAzureCredential()
    ml_client = MLClient(credential, SUBSCRIPTION_ID, RESOURCE_GROUP, WORKSPACE_NAME)
except Exception:
    credential = InteractiveBrowserCredential()
    ml_client = MLClient(credential, SUBSCRIPTION_ID, RESOURCE_GROUP, WORKSPACE_NAME)

print("Connected to workspace")

# Create MLTable from CSV
paths = [{"file": "./mltable_import/labels.csv"}]
tbl = mltable.from_delimited_files(paths=paths, delimiter=",", header="all_files_same_headers")

# Save MLTable
tbl.save("./mltable_import")
print("MLTable saved locally")

# Create data asset
VERSION = time.strftime("%Y%m%d%H%M%S", time.gmtime())
my_data = Data(
    path="./mltable_import",
    type=AssetTypes.MLTABLE,
    description="Labels for nail images import",
    name="nail-labels-import",
    version=VERSION,
)

ml_client.data.create_or_update(my_data)
print(f"Data asset 'nail-labels-import' version {VERSION} created successfully!")
