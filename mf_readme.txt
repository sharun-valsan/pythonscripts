1. Place the mf_updater.py and mf_worksheet.xlsx under the same directory path.
2. Populate the mf_worksheet template with your MF investment details.
3. The script would fetch mutual fund data from https://www.amfiindia.com/spages/NAVAll.txt? and run against the column 8th of the worksheet and update the current NAV field for Mutual fund absolute return calculation.
4. The accuracy of the NAV rates depends on the data available from the amfi portal.
5. Per my observation all the mutual fund NAV's are not daily updated, but a weekly update is always noticed.

Command to run script: 
From terminal/CMD prompt navigate to the directory where the script and workbook is placed using cd command, then run below command to execute the script.
python3 mf_updater.py

Note:
I wrote this script for my personal use and is only tested in Linux, I expect it to work on Windows as well.
Feel free to tweak it to suit your enviornment.
