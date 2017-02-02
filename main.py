import urllib2
from BeautifulSoup import BeautifulSoup

def GetIt():
    page = 'https://www.timeanddate.com/moon/phases/'
    soup = BeautifulSoup(urllib2.urlopen(page).read())

    print '\nLets get the next moon changes\n'
    
    # Get the rows of the table tha contains the moon phases
    therows = soup('table', {'id': 'mn-cyc'})[0].tbody('tr')
    # Get all the cell from last row that contains the date of occurence
    date_tabledata = therows[2].findChildren('td')

    for index, td in enumerate(therows[0]):
        phase = ''.join(td.a.string.lower().split(' '))
        if phase in ['fullmoon', 'newmoon']:
            print phase, date_tabledata[index].text

    print '\n'

if __name__ == "__main__":
    GetIt()