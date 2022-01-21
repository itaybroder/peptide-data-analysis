import pandas as pd

#merge between the two tables(netMHCpan ranks, the main df)
df1 = pd.read_csv("result.csv")
mhcpan_df = pd.read_csv("mhc_resualt.csv")

MHC_TYPES = list(set(mhcpan_df["mhc_type"]))

for mhc_type in MHC_TYPES[::-1]:
    df1 = df1.merge(mhcpan_df[mhcpan_df["mhc_type"]== mhc_type][["peptide", "rank"]].rename(columns={"rank":mhc_type + "_rank"}), left_on="peptide", right_on="peptide")
df1.to_csv("yair.csv")