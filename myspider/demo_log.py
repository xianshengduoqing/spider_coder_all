#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Jeffery LL'

import logging

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    #filename='myapp.log',
                    #filemode='w'
                    )

logger = logging.getLogger(__name__)



if __name__ == '__main__':
    logger.info("==========================")