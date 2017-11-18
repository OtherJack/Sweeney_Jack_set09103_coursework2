import ConfigParser
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def root():
  return render_template('index.html'), 200


@app.route('/MartinScorsese')
def ms():
  return render_template('MS.html'), 200

@app.route('/Director1')
def rems():
  return redirect(url_for('ms')), 301

@app.route('/MartinScorsese/TheWolfOfWallStreet')
def wolf():
  return render_template('wolf.html'), 200

@app.route('/WolfOfWallStreet')
def rewolf():
  return redirect(url_for('wolf')), 301

@app.route('/MartinScorsese/Goodfellas')
def good():
  return render_template('good.html'), 200

@app.route('/Goodfellas')
def regood():
  return redirect(url_for('good')), 301


@app.route('/QuentinTarantino')
def qt():
  return render_template('QT.html'),200

@app.route('/Director2')
def reqt():
  return redirect(url_for('qt')), 301

@app.route('/QuentinTarantino/TheHateful8')
def hate():
  return render_template('hate.html'), 200

@app.route('/Hateful8')
def rehate():
  return redirect(ur_for('hate')), 301

@app.route('/QuentinTarantino/PulpFiction')
def pulp():
  return render_template('pulp.html'), 200

@app.route('/PulpFiction')
def repulp():
  return redirect(url_for('pulp')), 301


@app.route('/DenisVilleneuve')
def dv():
  return render_template('DV.html'),200

@app.route('/Director3')
def redv():
  return render_redirect(url_for('dv')), 301

@app.route('/DenisVilleneuve/BladeRunner2049')
def blade():
  return render_template('blade.html'), 200

@app.route('/BladeRunner')
def reblade():
  return redirect(url_for('blade')), 301

@app.route('/DenisVilleneuve/Arrival')
def arrival():
  return render_template('arrival.html'), 200

@app.route('/Arrival')
def rearrival():
  return redirect(url_for('arrival')), 301


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
      app.config['log_file'] = config.get("logging", "name")
      app.config['log_location'] = config.get("logging", "location")
      app.config['log_level'] = config.get("logging", "level")
  except:
      print "Could not read configs from: ", config_location

def logs(app):
    log_pathname = app.config['log_location'] + app.config['log_file']
    file_handler = RotatingFileHandler(log_pathname, maxBytes=1024*1024 * 10 , backupCount=1024)
    file_handler.setLevel( app.config['log_level'] )
    formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(module)s | %(funcName)s | %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.setLevel( app.config['log_level'] )
    app.logger.addHandler(file_handler)

if __name__ == "__main__":
  init(app)
  logs(app)
  app.run(
      host=app.config['ip_address'],
      port=int(app.config['port']))
