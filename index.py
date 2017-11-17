import ConfigParser
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('index.html'), 200

@app.route('/MartinScorsese')
def ms():
  return render_template('MS.html'), 200

@app.route('/config/')
def config():
  str = []
  str.append('Debug:'+app.config['DEBUG'])
  str.append('port:'+app.config['port'])
  str.append('url:'+app.config['url'])
  str.append('ip_address:'+app.config['ip_address'])
  return '/t'.join(str)

def init(app):
  config = ConfigParser.ConfigParser()
  try:
      config_location = "etc/defaults.cfg"
      config.read(config_location)

      app.config['DEBUG'] = config.get("config", "debug")
      app.config['ip_address'] = config.get("config", "ip_address")
      app.config['port'] = config.get("config","port")
      app.config['url'] = config.get("config", "url")
  except:
      print "Could not read configs from: ", config_location

if __name__ == '__main__':
  init(app)
  app.run(
      host=app.config['ip_address'],
      port=int(app.config['port']))
