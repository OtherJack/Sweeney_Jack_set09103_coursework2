import ConfigParser
from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('index.html'), 200


@app.route('/MartinScorsese')
def ms():
  return render_template('MS.html'), 200

@app.route('/MartinScorsese/TheWolfOfWallStreet')
def wolf():
  return render_template('wolf.html'), 200

@app.route('/MartinScorsese/Goodfellas')
def good():
  return render_template('good.html'), 200


@app.route('/QuentinTarantino')
def qt():
  return render_template('QT.html'),200

@app.route('/QuentinTarantino/TheHateful8')
def hate():
  return render_template('hate.html'), 200

@app.route('/QuentinTarantino/PulpFiction')
def pulp():
  return render_template('pulp.html'), 200


@app.route('/DenisVilleneuve')
def dv():
  return render_template('DV.html'),200

@app.route('/DenisVilleneuve/BladeRunner2049')
def blade():
  return render_template('blade.html'), 200

@app.route('/DenisVilleneuve/Arrival')
def arrival():
  return render_template('arrival.html'), 200


@app.errorhandler(404)
def page_not_found(error):
  return render_template('404.html'),404


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
