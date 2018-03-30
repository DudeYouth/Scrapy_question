# -*- coding: utf-8 -*-
import scrapy
import time
import numpy
from Question.items import QuestionItem


class TencentpostionSpider(scrapy.Spider):
    name = 'tencentPostion'
    allowed_domains = ['www.jyeoo.com']
    start_urls = ['http://www.jyeoo.com/math3/ques/search','http://www.jyeoo.com/chinese3/ques/search','http://www.jyeoo.com/english3/ques/search']
    #start_urls = ['http://www.jyeoo.com/math3/ques/detail/7bbcf3cd-614e-44be-bd0f-e3cdde83a300']
    type_url = 'http://www.jyeoo.com/math3/ques/partialcategory'
    ques_url = 'http://www.jyeoo.com/math3/ques/partialques'
    subjects = {'http://www.jyeoo.com/math3/ques/search':"数学",'http://www.jyeoo.com/chinese3/ques/search':"语文",'http://www.jyeoo.com/english3/ques/search':"英语"}
    subject = ''
    level = 1
    question = ''
    options = []
    answer = ''
    qid = ''
    answers = ['A','B','C','D']
    type = ["语文","数学","英语"]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.18 Safari/537.36',
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests':1,
        'Cache-Control':'max-age=0',
        'Host':'www.jyeoo.com',

        'Origin':'http://www.jyeoo.com',

    }
    def parse(self, response):
        self.subject = self.subjects[response.url]
        for each in response.xpath("//tr[@class='JYE_GRADE']"):
            # 初始化模型对象
            # item = TencentItem()
            for qt in each.xpath("./td/ul/li/a"):
                # print(self.base_url + '?a='+qt+'&f=0&r='+str(int(t)))
                strs = qt.re(r'return\s*_gradeClick\(this[,0-9]+?\'([0-9a-zA-Z-]+)\'\)')
                self.level = qt.xpath("./text()").extract()[0]
                t = time.time()
                yield scrapy.Request(self.type_url + '?a='+strs[0]+'&f=0&r='+str(int(t)), callback=self.gettype)
            # 获取难度
            # item['difficulty'] = each.xpath("./td[2]/text()").extract()[0]
            # 获取题目类型
            # item['type'] =  each.xpath("./td[3]/text()").extract()[0]

            # yield 'http://www.jyeoo.com/math3/ques/partialcategory?a=f0a726bc-14ff-4a2a-8155-2b267bb59c39&f=0&r=0.06657410056821766'
    # def start_requests(self):
    #     t = str(int(time.time() * 1000))
    #     cookies = { 
    #         'JYERN':'0.8425840998116187',
    #         'remind_check':'1',
    #         'QS_ED':'13',
    #         'QS_GD':'3',
    #         'QS_TM':'1',
    #         'j_math3_q_q_0':'',
    #         'j_math3_q_ct':'1',
    #         'j_math3_q_dg':'0',
    #         'j_math3_q_fg':'0',
    #         'j_math3_q_so':'0',
    #         'j_math3_q_so2':'0',
    #         'j_math3_q_po':'0',
    #         'j_math3_q_pd':'1',
    #         'j_q_lbs':'',
    #         'jyean':'aasgGf7K9YW29wGeDYWhnIB1FWJO17wbrrqbnf-4MLGgzeWK0FB33OVPM5bmQItR5jv85abvlczJ72rnNmoksI_2aafAKlTQcj6fSsjORHO1IzDI3vqR4VOKmtuFxG-U0',
    #         'UM_distinctid':'1626b9a9ce25d-0d93560c66728-681f1b7e-1fa400-1626b9a9ce3211',
    #         'LF_Email':'18312168363',
    #         'remind_check':'1',
    #         'CNZZDATA2018550':'cnzz_eid%3D1427837169-1522218522-%26ntime%3D1522391355',
    #         'jy':'4327C18D9AFD0F663F5E2E664CD31B6BAD1618691106D6FA29CF628921335618FA9D2A9B80C7591333442F41C5D7F1CF76348FF16B005369525E41C0832CD045952CB34CE3AD35CF73E85129050A52EAF3F43FF4FA5AED33B36CD23F397666841CDB1F33A84CC1BC11BD95E88B67770B19CBDEA6EC8C41F11C7A2A17C9907B01304BD3264F581356B0FA0E0B3DD7FED8D379BF8D9EE85A190247B77F554C8FA6142A1A6AF2CB2B2706A376424DC90E82EA281C917366610338E67042F95A4FA2967082D17F9A9DAB0AECFB1C721038B7D5E638C1CC63D6D912170200254AA2D834457CA25B7AA0D626DDE2A036D3D00FF48D245AC3F61D3502B6B36CB5CCD4AE900F1576E0E5350E332602B5EAC74E38F24015AD926E2C9AB77AC9885B922CFD9C9DF443FD8264458EC2A0ED1220FAEDA8429E9CFB980F21EEF345AB6AE20A550ED0979314A1B7545544715372E2B77B',
    #         'JYERN':'0.6250200085709037',
    #     }
    #     #captcha_url = 'http://www.jyeoo.com/api/captcha/ec60c29912fd4306b8d4c03a0daae809?w=160&r=0.'+t
    #     qurl = 'http://www.jyeoo.com/math3/ques/detail/7bbcf3cd-614e-44be-bd0f-e3cdde83a300'
    #     return [scrapy.Request(url=qurl, headers=self.headers,cookies=cookies,callback=self.parse)]
    def parser_captcha(self, response):
        with open('captcha.jpg', 'wb') as f:
            f.write(response.body)
            f.close()
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            print(123)
        captcha = input("please input the captcha")
        print(captcha)
        post_url = 'http://www.jyeoo.com/account/loginform'
        post_data = {
            "Email": '18312168363',
            "Password": 'Nzc5NzQ4MGFh',
            "Captcha": str(captcha),
            "Remember":"false",
            "Ver":"True",
            "AnonID":"ec60c299-12fd-4306-b8d4-c03a0daae809",
            "Title":"",
            "RUrl":"",
        }
        cookies = { 
            'jyean':'aasgGf7K9YW29wGeDYWhnIB1FWJO17wbrrqbnf-4MLGgzeWK0FB33OVPM5bmQItR5jv85abvlczJ72rnNmoksI_2aafAKlTQcj6fSsjORHO1IzDI3vqR4VOKmtuFxG-U0',
            'UM_distinctid':'1626b9a9ce25d-0d93560c66728-681f1b7e-1fa400-1626b9a9ce3211',
            'LF_Email':'18312168363',
            'remind_check':'1',
            'CNZZDATA2018550':'cnzz_eid%3D1427837169-1522218522-%26ntime%3D1522391355',
            'jy':'4327C18D9AFD0F663F5E2E664CD31B6BAD1618691106D6FA29CF628921335618FA9D2A9B80C7591333442F41C5D7F1CF76348FF16B005369525E41C0832CD045952CB34CE3AD35CF73E85129050A52EAF3F43FF4FA5AED33B36CD23F397666841CDB1F33A84CC1BC11BD95E88B67770B19CBDEA6EC8C41F11C7A2A17C9907B01304BD3264F581356B0FA0E0B3DD7FED8D379BF8D9EE85A190247B77F554C8FA6142A1A6AF2CB2B2706A376424DC90E82EA281C917366610338E67042F95A4FA2967082D17F9A9DAB0AECFB1C721038B7D5E638C1CC63D6D912170200254AA2D834457CA25B7AA0D626DDE2A036D3D00FF48D245AC3F61D3502B6B36CB5CCD4AE900F1576E0E5350E332602B5EAC74E38F24015AD926E2C9AB77AC9885B922CFD9C9DF443FD8264458EC2A0ED1220FAEDA8429E9CFB980F21EEF345AB6AE20A550ED0979314A1B7545544715372E2B77B',
            'JYERN':'0.6250200085709037',
        }
        return [scrapy.FormRequest(url=post_url, formdata=post_data, headers=self.headers,cookies=cookies,callback=self.check_login)]

    def check_login(self, response):
        print(response.headers)
        with open('index.html', 'wb') as f:
            f.write(response.body)
            f.close()


    def login(self,response):
        print(response.body,99999)
        with open('index.html', 'wb') as f:
            f.write(response.body)
            f.close()
    # 获取题目类型
    def gettype(self,response):
        for each in response.xpath("//ul/li/a/@pk"):
            t = time.time()
            qid = each.extract()[0]
            self.qid = qid
            yield scrapy.Request(self.ques_url + '?q='+qid+'&ct=1&dg=0&fg=0&po=0&pd=1&lbs=&so=0&so2=0&r='+str(int(t)), callback=self.getpage)

    # 获取分页
    def getpage(self,response):
        page = response.xpath("//a[@class='last ']/@href").re(r'javascript:goPage\(([0-9]+),this\)')
        p = 1
        if len(page) :
            p = page[0]
        for index in numpy.arange(1,int(p),1):
            yield scrapy.Request(response.url+'&pi='+str(index), callback=self.getquestion)

    # 获取题目
    def getquestion(self,response):
        cookies = { 
            'JYERN':'0.8425840998116187',
            'remind_check':'1',
            'QS_ED':'13',
            'QS_GD':'3',
            'QS_TM':'1',
            'j_math3_q_q_0':self.qid,
            'j_math3_q_ct':'1',
            'j_math3_q_dg':'0',
            'j_math3_q_fg':'0',
            'j_math3_q_so':'0',
            'j_math3_q_so2':'0',
            'j_math3_q_po':'0',
            'j_math3_q_pd':'1',
            'j_q_lbs':'',
            'jyean':'aasgGf7K9YW29wGeDYWhnIB1FWJO17wbrrqbnf-4MLGgzeWK0FB33OVPM5bmQItR5jv85abvlczJ72rnNmoksI_2aafAKlTQcj6fSsjORHO1IzDI3vqR4VOKmtuFxG-U0',
            'UM_distinctid':'1626b9a9ce25d-0d93560c66728-681f1b7e-1fa400-1626b9a9ce3211',
            'LF_Email':'18312168363',
            'remind_check':'1',
            'CNZZDATA2018550':'cnzz_eid%3D1427837169-1522218522-%26ntime%3D1522391355',
            'jy':'4327C18D9AFD0F663F5E2E664CD31B6BAD1618691106D6FA29CF628921335618FA9D2A9B80C7591333442F41C5D7F1CF76348FF16B005369525E41C0832CD045952CB34CE3AD35CF73E85129050A52EAF3F43FF4FA5AED33B36CD23F397666841CDB1F33A84CC1BC11BD95E88B67770B19CBDEA6EC8C41F11C7A2A17C9907B01304BD3264F581356B0FA0E0B3DD7FED8D379BF8D9EE85A190247B77F554C8FA6142A1A6AF2CB2B2706A376424DC90E82EA281C917366610338E67042F95A4FA2967082D17F9A9DAB0AECFB1C721038B7D5E638C1CC63D6D912170200254AA2D834457CA25B7AA0D626DDE2A036D3D00FF48D245AC3F61D3502B6B36CB5CCD4AE900F1576E0E5350E332602B5EAC74E38F24015AD926E2C9AB77AC9885B922CFD9C9DF443FD8264458EC2A0ED1220FAEDA8429E9CFB980F21EEF345AB6AE20A550ED0979314A1B7545544715372E2B77B',
            'JYERN':'0.6250200085709037',
        }
        for each in response.xpath('//li[@class="QUES_LI"]'):
            if not (len(each.xpath('./fieldset/div[@class="pt1"]/span/table').extract())):
                question = each.xpath('./fieldset/div[@class="pt1"]/text()').extract()[0]
                options = each.xpath('./fieldset/div[@class="pt2"]/table/tr/td/label/text()').re(ur'^[A-Da-d]．([\s\S]+)')
                href = each.xpath('./span[@class="fieldtip"]/a[@target="_blank"]/@href').extract()[0]
                if '' not in options:
                    # print(href,options)
                    self.question = question
                    self.options = options
                    yield scrapy.Request(href, callback=self.getanswer,cookies=cookies)
    
    # 获取答案
    def getanswer(self,response):
        item = QuestionItem()
        data = response.xpath('//div[@class="pt6"]/text()')
        analysis = data.extract()[0];
        answer = data.re(ur'故选：([A-D])．')
        with open('index.html', 'wb') as f:
            f.write(response.body)
            f.close()
        print(analysis,answer)
        # if answer:
        #     if len(self.options)<=3:
        #         self.options.append('其他答案均不正确')
        #     item['question'] = self.question
        #     item['options'] = self.options
        #     item['level'] = self.level
        #     item['subject'] = self.subject
        #     item['analysis'] = analysis
        #     item['answer'] = answer



                    

            
            
        
            

        

            
            
        
