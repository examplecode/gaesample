
import wsgiref.handlers

def application(environ, start_response):
  start_response('200 OK', [('Content-type','text/plain')])
  return ['%s: %s\n' % (k, v) for k, v in environ.iteritems()]

def main():
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
