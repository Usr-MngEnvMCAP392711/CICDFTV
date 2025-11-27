# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "47ca4b6a-c6ed-45c8-87d2-fa544dbdeecc",
# META       "default_lakehouse_name": "LakehouseSecurity",
# META       "default_lakehouse_workspace_id": "886736af-92a7-431e-b4bd-ec324906c645",
# META       "known_lakehouses": [
# META         {
# META           "id": "47ca4b6a-c6ed-45c8-87d2-fa544dbdeecc"
# META         }
# META       ]
# META     },
# META     "environment": {
# META       "environmentId": "9dce5ec7-29aa-4a09-9141-0566be808cc9",
# META       "workspaceId": "0eb6768c-7f57-4d4e-b1ee-ed8b0b68a08e"
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/ChanelOutput24.csv")
# df now is a Spark DataFrame containing CSV data from "Files/ChanelOutput24.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
