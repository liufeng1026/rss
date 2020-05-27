# coding=utf8

from HttpRequests import HttpRequests
from bs4 import BeautifulSoup
import sys
from qqmail import qqMail
reload(sys)
sys.setdefaultencoding('utf-8')


class WxGzhArticle:

    def __init__(self):
        self.prefix = 'https://weixin.sogou.com{}'
        self.params = {
            "type": 1,
            "s_from": "input",
            "ie": "utf8",
            "_sug_": "n",
            "_sug_type_": "",
            # default 公众号
            "query": "ok数码2016"
        }
        self.client = HttpRequests()

    def getNewGzhArticle(self, gzh="ok数码2016"):
        self.params['query'] = gzh
        url = self.prefix.format('/weixin')
        res = self.client.get(url, self.params)
        if res is not None and res.status_code == 200:
            soup = BeautifulSoup(res.content, 'html.parser')
            article_0 = soup.find(name='a', attrs={"uigs": "account_article_0"})
            if article_0 is not None:
                article = {
                    "href": self.prefix.format(article_0['href']),
                    "title": article_0.contents[0]
                }
                return article
            else:
                return None
        else:
            return None


if '__main__' == __name__:
    gzhArticle = WxGzhArticle()
    qqmail = qqMail()
    # 定义一个公众号列表
    gzh_list = ['OK数码2016', 'python', '全民独立经纪人', '程序视界', '非著名程序员']
    for gzh in gzh_list:
        art = gzhArticle.getNewGzhArticle(gzh)
        if art is not None:
            qqmail.send_mail(title= art['title'], content= art['href'], receiver= '76816025@qq.com')
