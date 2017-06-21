from common import *
from selenium.webdriver.support.ui import WebDriverWait          #available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC #available since 2.26.0

"""Test alert box"""

##region prepare the html file
html='''
<!DOCTYPE html>
<html>
<body>

<p>An alert box must show on start-up</p>

<script>
alert("Hello! I am an alert box!");
</script>

</body>
</html>
'''

#generate temp file
import tempfile
htmlFile = tempfile.NamedTemporaryFile().name #ref. https://stackoverflow.com/a/13717435/248616

#write html to file ref. https://stackoverflow.com/a/27708256/248616
with open(htmlFile, 'w') as f:
  f.write(html)
##endregion prepare the html file

#open sample alert page
driver = loadWebDriverCHROME()
url = 'file:///'+htmlFile
print('Testing at %s' % url)
driver.get(url)

WebDriverWait(driver,10).until(EC.alert_is_present()) #TODO Why alert box not available? We got error here
alertBox = driver.switch_to_alert()
alertBox.accept()
