# Andrew Shen, 06/22/2022
# Script to process qPCR data and pipe into Benchling, input qPCR file is in csv form
# To run: python process_qpcr.py <path to input file>

# Import packages
import sys
import pandas as pd
# importing the get_sequence_source.py file from the zf_sequence_source package directory
from zf_sequence_source import get_sequence_source
# importing the package_data.py file from the benchling_sgmo package directory
from benchling_sgmo import package_data

# Assign input files
qpcr_in = sys.argv[1]

# Read in input qPCR file and convert to proper dictionary format
df = pd.read_csv(qpcr_in)
df = df.reset_index()
#print(df["Sample"])
#print(df)
qpcr_dict = {}
for i, row in df.iterrows():
    qpcr_dict[row["Sample"]] = [row["ZFC ID"], row["Target"], row["Well"], row["Data Set"], row["Content"], row["Type"], row["Cq"], row["Starting Quantity (SQ)"], row["Control"], row["cDNA"], row["fn"], row["sample excluded"], row["SQ"], row["Absolute Quantity"], row["Absolute Quantity SD"], row["Mean Cq"], row["Cq SD"], row["Efficiency"], row["Relative Quantity"], row["Relative Quantity SD"], row["Normalization Factor"], row["Normalization Factor SD"], row["Expression"], row["Expression SD"], row["Dose"]]
#for k,v in qpcr_dict.items():
#    print(v)

# Connect to Benchling
#seq_source = get_seq_source()
#print(seq_source)
def connect_to_bench():
    # Calls the get_seq_source() function within the get_sequence_source.py file
    seq_source = get_sequence_source.get_seq_source()
    return seq_source
#    seq_source = get_seq_source(is_test=True)
bench = connect_to_bench()
#bench =

# Package data
schema = "qPCR Result"
bench_list = package_data.bulk_package_data(data=qpcr_dict, schema_name=schema, api_client=bench)
# Upload to Benchling
print(bench_list)


# print(df)


