#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging

try:
    from google.appengine.api import urlfetch
    from google.appengine.runtime import apiproxy_errors
except ImportError:
    urlfetch = None


def  gae_application(environ, start_response):
    
    logging.info(environ['QUERY_STRING'])
    result =urlfetch.fetch("http://www.sina.com.cn")
    #result.headers['Connection'] = 'close'
    logging.info(result.headers)

    
    #start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
    new_headers = []
    for k ,v in result.headers.iteritems():
        tmp = (k,v)
        new_headers.append(tmp)
    #new_headers.append(('Connection','close'))
   
    logging.info(new_headers)

    start_response('200 OK', new_headers)
    #urlfetch.fetch("http://www.sina.com.cn", 0, environ['QUERY_STRING'], headers, allow_truncated=False, follow_redirects=False, deadline=deadline, validate_certificate=validate_certificate)
    return result.content

        

app = gae_application
