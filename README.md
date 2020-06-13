# Facebook Message Analytics

Generates participation and word count CSVs on Facebook message dumps.

## Prerequisites
### Requirements
- Python 3
- pip

Install the required pip modules.

```bash
cd fb-msg-analytics
pip install -r requirements.txt
```

### Data Download
Go to Facebook's [Download Your Information](https://www.facebook.com/dyi/) page and select:
1. Date Range: _All of my data_
2. Format: _JSON_ (__important__)
3. Media Quality: _Low_
4. _Deselect All_ and only select _Messages_

Click _Create File_ and it'll email you when the .zip is ready to be downloaded.

## Usage
Extract the downloaded .zip and point the script to the conversation of interest.

```bash
mkdir ~/fbdata
unzip facebook-[username].zip -d ~/fbdata

cd fb-msg-analytics
python ./fbMsgAnalytics.py ~/fbdata/messages/inbox/[convo_name]/

ls *.csv
participation.csv  wordCount.csv
```
