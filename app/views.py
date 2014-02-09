from flask import render_template, flash, redirect, request
from app import app
from app import helpers
from forms import PlsForm
from app.redismodel import redis

@app.route('/', methods = ['GET', 'POST'])
def root():
    helpers.process_request(request.data) 
    form = PlsForm()
    pls_links = redis.hgetall('stations')
    # ex: {'SKY.FM Reggae': 'http://pub3.sky.fm:80/sky_rootsreggae', 'Death.FM': 'http://hi5.death.fm/listen.pls', 'KDVS': 'http://169.237.101.239:8000/kdvs128'}
    return render_template("pls_bookmark.html",
        pls_links = pls_links,
        form = form)

@app.route('/index')
def index():
    return redirect('/')

@app.route('/delete/<nick>', methods=['POST'])
def delete(nick):
  helpers.delete_pls(nick)
  return redirect('/index')
