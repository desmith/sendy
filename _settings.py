#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""RSS2Email settings."""

import os

DEFAULTS = {
    "sendy_url": "https://mail.iskconnews.org",
    "sendy_api_key": os.getenv("SENDY_API_KEY"),
    "database": "/tmp/feed_log.db",
    "feed_url": "https://iskconnews.org/feed/rss/",
    # 'feed_url': 'https://iskconnews.org/feed/sendy/',
    "template": "responsive.html,text.txt",
    "from_name": "ISKCON News",
    "from_email": "newsletter@mail.iskconnews.org",
    "reply_to": "newsletter@mail.iskconnews.org",
    "subject": "Latest Stories From ISKCON News",
    "list_ids": os.getenv("SENDY_LIST_ID"),  # live list
    "list_ids_test": os.getenv('SENDY_LIST_ID_TEST'),  # test list
}
