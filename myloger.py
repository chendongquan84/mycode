#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年10月16日

@author: chendq
'''
import logging

def update_logging(log_name):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=log_name,
                        filemode='w')
    
    #################################################################################################
    #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    #################################################################################################
    
    # logging.debug('This is debug message')
    # logging.info('This is info message')
    # logging.warning('This is warning message')
#import os, sys
if __name__ == '__main__':
    update_loging()
    logging.debug('This is debug message')
    logging.info('This is info message')
    logging.warning('This is warning message')
    pass
