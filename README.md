# auto-crawler-send-mail
定时爬取目标网站数据并发送到指定邮箱

### Technology Stack
Python + requests + lxml + Xpath +celery + redis + supervisor + xlwd + smtplib + email

### 实现流程

- ① requests 请求目标网站，获取响应资源
- ② lxml+xpath 进行数据提取
- ③ xlwd 将爬取的数据写入Excel
- ④ smtplib+eamil 将Excel数据当做附件发送到指定邮箱
- ⑤ celery beat + redis 进行任务的定时调度 
- ⑥ supervisor 进行后台进程管理
