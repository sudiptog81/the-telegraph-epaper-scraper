# The Telegraph ePaper Scraper

Script for scraping the e-paper of the prestigious English daily 'The Telegraph' from the house of Ananda Bazar Patrika (ABP). The script downloads the Calcutta edition. This script is written for UNIX.

This script uses the `requests` module to fetch all the images from the concerned e-paper website.

Once all images are downloaded, it executes the `convert` tool (part of ImageMagick) that is responsible for converting all the pages of the newspaper to a single PDF.  A push notification is also sent to the devices subscribed to receive them.

This PDF is then uploaded to a MEGA folder and then deleted from the local machine. The PDF can then be accessed from all devices supported by the MEGA clients. One may override the behaviour of the script in `upload.py` to change the uploading and cleanup logic.

## Sample Downloads

[View The Telegraph ePaper folder on MEGA](https://mega.nz/folder/KJ1DzJAa#jATxs9OV_7HeCyfPQ0gW9A)

[Subscribe to Sample Push Notifications](https://notify.run/c/ovzNEOD6IXThQpjN)

## Quick Start

  - Install ImageMagick on your system. Refer [https://imagemagick.org/script/download.php](https://imagemagick.org/script/download.php) or check your repositories on unices.
  - Install all dependencies from PyPI using the command `pip install -r requirements.txt`.
  - Register your devices with `notify-run register` to receive push notifications.
  - Run the script by executing `./scrape.sh`.

## Scheduling the Job

One can schedule the task to be run daily at 06:00 AM (take care of the time zone) using cron jobs. Open the cron table using the command `crontab -e` and add the line `0 6 * * * /location/to/scrape.sh` to the end of the file and save the file. The task will run automatically and the latest edition of 'The Telegraph' will be uploaded to the MEGA folder everyday by 06:05 AM.

## Author

Sudipto Ghosh ([sudipto.ghosh.pro](https://sudipto.ghosh.pro))

## License

Source code is distributed under the MIT License.

All rights to the textual and non-textual media sourced from 'The Telegraph e-Paper' using this script are reserved by Ananda Bazar Patrika (ABP) Group.
