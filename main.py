# This script scrape the moon changing phases (full, new) from timeanddate.com
# And print the information.
# This was 

import urllib2
from BeautifulSoup import BeautifulSoup

def GetPhases():
    # Set the source of the information
    source = 'https://www.timeanddate.com/moon/phases/'
    req = urllib2.Request(source)
    # Set http header to get the page in english
    req.add_header('Accept-Language', 'en-US')
    # Get the page data
    soup = BeautifulSoup(urllib2.urlopen(req).read())
    # Get the rows of the table that contains the moon phases
    therows = soup('table', {'id': 'mn-cyc'})[0].tbody('tr')
    # The first row contains the name of the event (Full Moon, New Moon, ...)
    events_row = therows[0]
    # The third row contains the dates and time of the occuring events
    # Get all the cell from that third row
    date_tabledata = therows[2].findChildren('td')

    # Loop through all phases
    for index, td in enumerate(events_row):
        phase_name = td.a.string
        # Check the phase name in lower case without spaces
        if ''.join(phase_name.lower().split(' ')) in ['fullmoon', 'newmoon']:
            # It is a full or new moon, get the date without the time
            date_occurence = date_tabledata[index].text[:-5]
            print phase_name, date_occurence

if __name__ == "__main__":
    GetPhases()