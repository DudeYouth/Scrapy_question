# -*- coding: utf-8 -*-
import scrapy
import time
import numpy


class TencentpostionSpider(scrapy.Spider):
    name = 'tencentPostion'
    allowed_domains = ['www.jyeoo.com']
    start_urls = ['http://www.jyeoo.com/math3/ques/search','http://www.jyeoo.com/chinese3/ques/search','http://www.jyeoo.com/english3/ques/search']
    type_url = 'http://www.jyeoo.com/math3/ques/partialcategory'
    ques_url = 'http://www.jyeoo.com/math3/ques/partialques'
    subjects = {'http://www.jyeoo.com/math3/ques/search':"数学",'http://www.jyeoo.com/chinese3/ques/search':"语文",'http://www.jyeoo.com/english3/ques/search':"英语"}
    subject = ''
    level = 1
    question = ''
    options = []
    answer = ''
    type = ["语文","数学","英语"]
    def parse(self, response):
        self.subject = subjects[response.url]
        for each in response.xpath("//tr[@class='JYE_GRADE']"):
            # 初始化模型对象
            # item = TencentItem()
            for qt in each.xpath("./td/ul/li/a"):
                # print(self.base_url + '?a='+qt+'&f=0&r='+str(int(t)))
                strs = qt.re(r'return\s*_gradeClick\(this[,0-9]+?\'([0-9a-zA-Z-]+)\'\)')
                self.level = qt.xpath("./text()").extract()
                t = time.time()
                yield scrapy.Request(self.type_url + '?a='+strs+'&f=0&r='+str(int(t)), callback=self.gettype)
            # 获取难度
            # item['difficulty'] = each.xpath("./td[2]/text()").extract()[0]
            # 获取题目类型
            # item['type'] =  each.xpath("./td[3]/text()").extract()[0]

            # yield 'http://www.jyeoo.com/math3/ques/partialcategory?a=f0a726bc-14ff-4a2a-8155-2b267bb59c39&f=0&r=0.06657410056821766'
    # 获取题目类型
    def gettype(self,response):
        for each in response.xpath("//ul/li/a/@pk"):
            t = time.time()
            yield scrapy.Request(self.ques_url + '?q='+each.extract()+'&ct=1&dg=0&fg=0&po=0&pd=1&lbs=&so=0&so2=0&r='+str(int(t)), callback=self.getpage)

    # 获取分页
    def getpage(self,response):
        page = response.xpath("//a[@class='last ']/@href").re(r'javascript:goPage\(([0-9]+),this\)')
        p = 1
        if( len(page) ):
            p = page[0]
        for index in numpy.arange(1,int(p),1):
            yield scrapy.Request(response.url+'&pi='+str(index), callback=self.getquestion)

    # 获取题目
    def getquestion(self,response):
        for each in response.xpath('//li[@class="QUES_LI"]'):
            if !len(each.xpath('./fieldset/div[@class="pt1"]/span/table').extract()):
                question = each.xpath('./fieldset/div[@class="pt1"]/text()').extract()
                options = each.xpath('./fieldset/div[@class="pt2"]/table/tr/td/label/text()').re(ur'^[A-Da-d]．([\s\S]+)')
                href = each.xpath('./span[@class="fieldtip"]/a[@target="_blank"]/@href').extract()
                if !('' in options):
                    self.question = question
                    self.options = options
                    yield scrapy.Request(href, callback=self.getanswer)
    
    # 获取答案
    def getanswer(self,response):
        item = Question()
        answer = response.xpath('//div[@class="pt6"]/text()').extract()
        print(  )


                    

            
            
        
            

        

            
            
        
