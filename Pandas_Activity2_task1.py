import pandas as pd

# Create dictionary of family member list
familyMember = ["Karma Dorji", "Urmila Sharma", "Sangay Dorji", "Denay Lhamo"]
df = pd.Series(familyMember, index = ["Dad", "Mom", "Bro", "Sis"])

# Print data frame
print(df)


