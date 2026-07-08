import pandas as pd

# Dataset paths
mozilla_path = "../datasets/mozilla/mozilla_bug_report_data.csv"
eclipse_path = "../datasets/eclipse/eclipse_bug_report_data.csv"
apache_path = "../datasets/apache/cassandra_bugs-combined.csv"

# Read datasets
mozilla_df = pd.read_csv(mozilla_path)
eclipse_df = pd.read_csv(eclipse_path)
apache_df = pd.read_csv(apache_path)

print("\n========== DATASET SUMMARY ==========\n")

print("Mozilla Bugs :", len(mozilla_df))
print("Eclipse Bugs :", len(eclipse_df))
print("Apache Bugs  :", len(apache_df))

print("\n========== MOZILLA SAMPLE ==========\n")
print(mozilla_df.head())

print("\n========== ECLIPSE SAMPLE ==========\n")
print(eclipse_df.head())

print("\n========== APACHE SAMPLE ==========\n")
print(apache_df.head())