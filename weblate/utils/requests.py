# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2020 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import requests

from weblate import USER_AGENT


def request(method, url, headers=None, **kwargs):
    agent = {"User-Agent": USER_AGENT}
    if headers:
        headers.update(agent)
    else:
        headers = agent
    response = requests.request(method, url, headers=headers, **kwargs)
    response.raise_for_status()
    return response


def uri_exists(uri):
    try:
        with request("get", uri, stream=True):
            return True
    except requests.exceptions.HTTPError:
        return False
    except requests.exceptions.ConnectionError:
        return False
