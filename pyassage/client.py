# -*- coding: utf-8 -*-

"""
Simple Python API client for the CloudPassage API.
"""

import base64
import logging
import requests

from datetime import datetime, timedelta
from pyassage import models
from requests.auth import AuthBase


log = logging.getLogger("pyassage")


class CloudPassageAPI:
    """Provides an interface to the CloudPassageAPI"""
    def __init__(self, client_id, client_secret,
                 base_url='https://api.cloudpassage.com'):
        self.base_url = base_url
        self.cp_auth = CloudPassageAuth(client_id, client_secret, base_url)

    def get_system_announcements(self, active=True):
        url = "{0}/v1/system_announcements".format(self.base_url)
        if active:
            url = "{0}?status=active".format(url)

        r = requests.get(url, auth=self.cp_auth)
        r.raise_for_status()

        announcements = []
        for a in r.json()['announcements']:
            sa = models.SystemAnnouncement()
            announcements.append(sa.parse(a))

        return announcements


class CloudPassageAuth(AuthBase):
    """Handles authenticating to the Cloud Passage API"""

    def __init__(self, client_id, client_secret, base_url):
        self.base_url = base_url
        self.grant_type = 'client_credentials'
        self.auth_token = None
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_token_expiry = None

    def __call__(self, r):
        if self.auth_token_expiry is None:
            self.authenticate()

        if datetime.utcnow() >= self.auth_token_expiry:
            self.authenticate()
            log.debug("No valid auth_token, re-authenticating.")

        r.headers['Authorization'] = "Bearer {0}".format(self.auth_token)
        return r

    def authenticate(self):
        url = "{0}/oauth/access_token?grant_type={1}".format(
            self.base_url, self.grant_type)
        log.debug("Authentication URI: %s", url)

        log.debug("Client ID: %s, Client Secret (Last 4): ...%s",
                  self.client_id, self.client_secret[-4:])

        auth = "{0}:{1}".format(self.client_id, self.client_secret)
        base64_auth = base64.b64encode(auth.encode('ascii'))
        headers = {'Authorization': "Basic " + base64_auth.decode('ascii')}

        r = requests.post(url, headers=headers)
        r.raise_for_status()

        resp_json = r.json()
        log.debug("Authentication Response: %s", resp_json)
        self.auth_token = resp_json['access_token']
        self.auth_token_expiry = datetime.utcnow() + timedelta(
            seconds=resp_json['expires_in'])
        log.debug("CPAPI Authentication successful")
