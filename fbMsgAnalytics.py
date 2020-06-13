import sys
import os, glob
import json
import pandas as pd

def main():
    # Use first and only arg as path to Facebook message_*.json dump files
    # e.g. facebook-[username].zip/messages/inbox/[convo_name]/
    inputDir = sys.argv[1]

    fbMsgJsonDirToStatsCsv(inputDir)

# Generates participation.csv for msg count per user and total msg count
# and wordCount.csv for number is instances per word
def fbMsgJsonDirToStatsCsv(inputDir):
    dfList = []
    df = pd.DataFrame()

    # Need to loop through all files since dumps are restricted to 10K msgs per JSON
    for filename in glob.glob(os.path.join(inputDir, '*.json')):
        with open(filename, 'r', encoding='utf-8-sig') as f:
            dfList.append(pd.DataFrame.from_dict(json.load(f).get('messages')))

    # Create one df out of multiple dfs
    df = pd.concat(dfList)

    # Want text messages only
    df = df[df['type'] == "Generic"]

    # Strip out unneeded cols
    df = df[['sender_name', 'content']]

    # Save participation.csv before modifying df further
    df2 = df['sender_name'].value_counts()
    df2['Total'] = df2.sum()
    df2.to_csv('participation.csv', header=["count"], encoding='utf-8-sig')

    # Remove non-wordy chars
    df['content'].replace(r'\n|[^\w\s]', '', regex=True, inplace=True)

    # Remove rows with empty strings after replacement
    df = df[df['content'].astype(bool)]

    # Set all msgs to lowercase and split into words
    df['content'] = df['content'].str.lower()
    df['content'] = df['content'].str.split(" +")

    # Save wordCount.csv
    df['content'].explode().value_counts().to_csv('wordCount.csv', header=["count"], encoding='utf-8-sig')

if __name__ == "__main__":
    main()