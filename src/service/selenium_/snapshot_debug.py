import os
import sys

#TODO simplify snapshot params

#TODO replace this config.py by .env using py-dotenv
s=os.path.abspath(os.path.dirname(__file__)) ; APP_HOME=os.path.abspath(f'{s}/..'); sys.path.insert(0, APP_HOME)  # add my folder to PYTHONPATH ref. http://flask.pocoo.org/docs/0.11/deploying/mod_wsgi/#creating-a-wsgi-file
from src.config import SNAPSHOT_DEBUG, SNAPSHOT_FOLDER  #TODO Why this required above path registered i.e. APP_HOME

#snapshot counter
SNAPSHOT_COUNTER=0


#taking snapshot util
def takeSnapshot(driver, prefix=None, suffix=None, forceSnapshot=False):
    if not forceSnapshot:  # check if snapshot required (and not being forced to do so)
        if not SNAPSHOT_DEBUG: return  # just do nothing when the flag is off

    # prepare filename
    global SNAPSHOT_COUNTER
    filename = '{SNAPSHOT_FOLDER}/{prefix}{SNAPSHOT_COUNTER:02d}{suffix}.png'.format(  # format number ref. https://stackoverflow.com/a/135157/248616
        SNAPSHOT_FOLDER  = SNAPSHOT_FOLDER,
        prefix           = '%s-' % prefix if prefix else 'snap',
        suffix           = '-%s' % suffix if suffix else '',
        SNAPSHOT_COUNTER = SNAPSHOT_COUNTER,
    )

    # do take snapshot
    os.makedirs(SNAPSHOT_FOLDER, exist_ok=True)
    driver.get_screenshot_as_file(filename) ; SNAPSHOT_COUNTER += 1

    return filename
