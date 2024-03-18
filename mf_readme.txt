1. Place the mf_updater.py and mf_worksheet.xlsx under a same directory path.
2. Update the mf_worksheet with the MF details.
3. The script would fetch mutual fund data from https://www.amfiindia.com/spages/NAVAll.txt? and run against the column 8th of the worksheet and update the current NAV field for calculation.
4. The accuracy of the NAV rates depends on the data available from the amfi portal.

Command to run script
python3 mf_updater.py

Note:
This is a script which I wrote for mypersonal use and is only tested in Linux, I expect it to work on Windows as well.
Feel free to tweak to suit your enviornment.
