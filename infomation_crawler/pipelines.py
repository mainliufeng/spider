# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class BaiduNewsPipeline(object):
    def process_item(self, item, spider):
      if spider.name not in ['baidu']:
	return item

      conn = pymongo.Connection('localhost',27017)
      infoDB = conn.info
      tArticles = infoDB.articles
      article = {"title":item['title'][0],'sitename':item['sitename'][0],'posttime':item['posttime'][0]}
      tArticles.update({'link':item['href'][0]},{'$set':article},True)

      # print "#"*20
      # print item["title"][0],item['href'][0],item['sitename'][0],item['posttime'][0]

      return item

class StockCompanyInfoPipeline(object):
    def process_item(self, item, spider):
      if spider.name not in ['cninfo']:
	return item
      else:
	if item['iType'] == 'companyInfo':
	  print "yes"
	  print "enter StockCompanyInfoPipeline....."
	  print '='*10
	'''
	conn = pymongo.Connection('localhost',27017)
	infoDB = conn.info
	tCompanyInfo = infoDB.stock_companyinfo
	

	company = {
	  "stockName":item['stockName'],
	  "fullName":item['fullName'],
	  "englishName":item['englishName'],
	  "regAddress":item['regAddress'],
	  "shortName":item['shortName'],
	  "legalPerson":item['legalPerson'],
	  "secretary":item['secretary'],
	  "regCapital":item['regCapital'],
	  "industry":item['industry'],
	  "postCode":item['postCode'],
	  "phone":item['phone'],
	  "fax":item['fax'],
	  "website":item['website'],
	  "listTime":item['listTime'],
	  "ipoTime":item['ipoTime'],
	  "issueAmount":item['issueAmount'],
	  "issuePrice":item['issuePrice'],
	  "issuePer":item['issuePer'],
	  "issueMode":item['issueMode'],
	  "underWriter":item['underWriter'],
	  "listSponsor":item['listSponsor'],
	  "recomInstitution":item['recomInstitution']
	}
	tCompanyInfo.update({'stockCode':item['stockCode']},{'$set':company},True)

	# print "#"*20
	# print item["stockCode"],item['stockName'],item['regAddress']

	'''
      return item


class StockBalanceSheetPipeline(object):
    def process_item(self, item, spider):
      if spider.name not in ['cninfo']:
	return item
      else:
	if item['iType'] == 'balanceSheet':
	  print "enter StockBalanceSheetPipeline....."
	  print '='*10
	return item

class StockIncomeStatementsPipeline(object):
    def process_item(self, item, spider):
      if spider.name not in ['cninfo']:
	return item
      else:
	if item['iType'] == 'incomeStatements':
	  print "enter StockIncomeStatementsPipeline....."
	  print '='*10
	return item

class StockCashFlowPipeline(object):
    def process_item(self, item, spider):
      if spider.name not in ['cninfo']:
	return item
      else:
	if item['iType'] == 'cashFlow':
	  print "enter StockCashFlowPipeline....."
	  print '='*10
	return item

class StockFinancialReportPipeline(object):
    def process_item(self, item, spider):
      if spider.name not in ['cninfo']:
	return item
      else:
	if item['iType'] == 'financialReport':
	  print "enter StockFinancialReportPipeline....."
	  print '='*10
	return item

class SteelIndexNumberPipeline(object):
  def process_item(self, item, spider):
    if spider.name not in ['steel']:
      return item

    conn = pymongo.Connection('localhost',27017)
    infoDB = conn.info
    tSteelIndex = infoDB.steelindex

    print "enter SteelIndexNumberPipeline....."
    for index,pubDate in enumerate(item['pubDate']):
      print pubDate, item['indexNumber'][index]
      data = {"indexnum":item['indexNumber'][index]}
      tSteelIndex.update({'pubdate':pubDate},{'$set':data},True)

    return item

class StatsMacroIndexPipeline(object):
  def process_item(self, item, spider):
    if spider.name not in ['statsindex']:
      return item

    conn = pymongo.Connection('localhost',27017)
    infoDB = conn.info
    tMacroIndex = infoDB.bm_macro_index

    print "enter StatsMacroIndexPipeline....."
    data = {"name":item['name'],"parentcode":item['parentCode'],"period":item['period'],'ts':item['ts'],'ifdata':item['ifData'],'unit':item['unit'],'note':item['note']}
    tMacroIndex.update({'code':item['code']},{'$set':data},True)

    return item

class StatsMacroDataPipeline(object):
  def process_item(self, item, spider):
    if spider.name not in ['statsdata']:
      return item

    conn = pymongo.Connection('localhost',27017)
    infoDB = conn.info
    tMacroIndex = infoDB.bm_macro_index
    tMacroData = infoDB.bm_macro_data

    print "enter StatsMacroDataPipeline....."
    if item['types'] == 'index':
      print "Update index's unit....."
      indexItem = tMacroIndex.find_one({'code':item['code']})
      indexItem['unit'] = item['unit']
      indexItem['note'] = item['note']
      tMacroIndex.update({'code':item['code']},indexItem)
    elif item['types'] == 'data':
      print "Insert macro data....."
      data = {"code":item['code'],"name":item['name'],'area':item['area'],'ydate':item['ydate'],'qdate':item['qdate'],'mdate':item['mdate'],'value':item['value'],'desc':item['desc'],'ts':item['ts']}
      tMacroData.update({'key':item['key']},{'$set':data},True)
    return item


