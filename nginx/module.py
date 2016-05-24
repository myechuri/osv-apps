from osv.modules import api

default = api.run('/tools/nginx.so -c /usr/local/nginx/conf/nginx.conf')
