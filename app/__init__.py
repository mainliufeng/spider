from flask import Flask, render_template, url_for, request
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
import pycurl
import StringIO
import json
import inspect
import pymongo
import datetime
import subprocess
import os
from .libs import sample_handler
# from infomation_crawler.spiders import *

default_script = inspect.getsource(sample_handler)



app = Flask(__name__)
projectName = 'infomation_crawler'

@app.route('/')
def index():
  return render_template('index.html', spiderListUrl=url_for('spiderList'))


@app.route('/edit/<groupName>/<spiderName>')
def editSpider(groupName,spiderName):
  filePath = os.path.join(os.path.dirname(__file__),'../'+groupName+'/'+groupName+'/spiders/'+spiderName+'.py')

  if not os.path.exists(filePath):
    script = (default_script.replace('__SPIDER_NAME__',spiderName).replace('__GROUP_NAME__',groupName))
  else:
    fileObj = open(filePath,'r')
    try:
      script = fileObj.read()
    finally:
      fileObj.close()

  return render_template('edit_spider.html', spiderName=spiderName, groupName=groupName, script=script)

  # return default_script

@app.route('/save', methods=['POST'])
def saveSpider():
  spiderName = request.form['spiderName']
  groupName = request.form['groupName']
  script = request.form['script']

  conn = pymongo.Connection('localhost',27017)
  spiderManagerDB = conn.spider_manager
  tSpiders = spiderManagerDB.spiders

  data = {'script':script,'group':groupName, 'edittime':datetime.datetime.now()}
  tSpiders.update({'spiderName':spiderName},{'$set':data},True)

  conn.close()

  filePath = os.path.join(os.path.dirname(__file__),'../'+groupName+'/'+groupName+'/spiders/'+spiderName+'.py')
  fileObj = open(filePath,'w')
  try:
    fileObj.write(script)
  finally:
    fileObj.close()

  return "spider saved: " + spiderName



@app.route('/show/<spiderName>')
def showSpider(spiderName):

  # script = inspect.getsourcefile('SinaSpider')
  filePath = os.path.join(os.path.dirname(__file__),'../infomation_crawler/spiders')
  if not os.path.exists(filePath + '/' + '36dsj.py'):

    return 'the file is not exists'
  else:
    fileObj = open(filePath + '/' + '36dsj.py','r')
    code = fileObj.read()

    fileObj.close()
    return code.replace('\n','<br />')
  # return render_template('show_spider.html', spiderName=spiderName, script=script)


@app.route('/joblist/<groupName>')
def jobList(groupName):
  c = pycurl.Curl()
  c.setopt(pycurl.URL, 'http://172.20.8.3:6800/listjobs.json?project='+groupName)

  b = StringIO.StringIO()
  c.setopt(pycurl.WRITEFUNCTION, b.write)
  c.perform()
  jsonStr = b.getvalue()
  jobList = json.loads(jsonStr)

  return render_template('job_list.html', jobList=jobList, groupName=groupName)

@app.route('/deploy', methods=['POST'])
def deployGroup():
  groupName = request.form['groupName']
  filePath = os.path.join(os.path.dirname(__file__),'../'+groupName)

  # returnCode = subprocess.check_output('cd '+filePath+'; scrapyd-deploy office -p '+groupName)
  returnCode = subprocess.check_output('cd '+filePath+'; scrapyd-deploy office -p '+groupName, shell=True)
  return returnCode







@app.route('/run', methods=['POST'])
def runSpider():
  '''
  settings = get_project_settings()
  crawler = Crawler(settings)
  crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
  crawler.configure()
  spider = crawler.spiders.create(spiderName)
  crawler.crawl(spider)
  crawler.start()
  log.start()
  reactor.run()
  '''
  spiderName = request.form['spiderName']
  c = pycurl.Curl()
  c.setopt(pycurl.URL, 'http://172.20.8.3:6800/schedule.json')
  c.setopt(c.POSTFIELDS, 'project=infomation_crawler&spider=%s' % spiderName)

  b = StringIO.StringIO()
  c.setopt(pycurl.WRITEFUNCTION, b.write)
  c.perform()
  jsonStr = b.getvalue()
  # jobList = json.loads(jsonStr)
  return jsonStr


@app.route('/resultslist/<resultsType>')
def resultsList(resultsType):
  return resultsType




@app.route('/spiderlist')
def spiderList():
  conn = pymongo.Connection('localhost',27017)
  spiderManagerDB = conn.spider_manager
  tSpiders = spiderManagerDB.spiders

  # tSpiders.update({'spiderName':spiderName},{'$set':data},True)
  spiderList = tSpiders.find()

  conn.close()

  # crawler = Crawler(get_project_settings())
  # crawler.configure()
  # spiderList = crawler.spiders.list()
  # spiderList = spiderList[:8]
  # return spiderList
  return render_template('spider_list.html',spiderList = spiderList)







if __name__ == '__main__':
  app.debug = True
  app.run()