"""
 * Copyright 2020 Mia srl
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
"""

from wsgiref.simple_server import make_server
import falcon
import json

class HelloResource:
  def on_get(self, req, resp):
    resp.status = falcon.HTTP_200
    hello = { 'message': "Hello World!" }
    resp.body = json.dumps(hello, ensure_ascii=False)

class ReadyResource:
  def on_get(self, req, resp):
    resp.status = falcon.HTTP_200
    ready = { 'statusOK': True }
    resp.body = json.dumps(ready, ensure_ascii=False)

class HealthResource:
  def on_get(self, req, resp):
    resp.status = falcon.HTTP_200
    health = { 'statusOK': True }
    resp.body = json.dumps(health, ensure_ascii=False)


helloer = HelloResource()
ready = ReadyResource()
health = HealthResource()

app = falcon.API()

app.add_route('/hello', helloer)
app.add_route('/-/ready', ready)
app.add_route('/-/healthz', health)

if __name__ == '__main__':
  with make_server('', 3000, app) as httpd:
    print('Serving on port 3000...')
    httpd.serve_forever()
