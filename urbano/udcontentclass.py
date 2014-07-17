# Imports
import requests
from contextlib import closing
from sys import exit


# Author and licensing
__Author__      =       "b-mcg"
__Email__       =       "bmcg0890@gmail.com"
__License__     =       """
Copyright (C) 2014-2016  b-mcg   <bmcg0890@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

class UD(object):
    """
    Urban Dictionary API interface
    class.

    """

    def __init__(self, word):
        """
        Initializes necessary attributes.

        @param word: word to look up definition for

        """
        # Base URL for definition lookup
        self.url    =   "http://api.urbandictionary.com/v0/define?term={0}"
        self.word   =   word

    def grabJSON(self):
        """
        Returns JSON
        from GET request.

        """
        with closing(requests.get(self.url.format(self.word.replace(' ', '+')))) as res:
            if res.status_code != 200:
                print "\nError: Non 200 status code returned: {0}\n".format(res.status)
                sys.exit(1)

            else:

                return res.json()
