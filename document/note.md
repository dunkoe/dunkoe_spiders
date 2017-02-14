# 笔记

### 进入shell

        scrapy shell <url>  
        
        scrapy shell "https://www.lagou.com"
        
        response.selector.xpath("//div[contains(@class, 'menu_box')]//a").extract()
