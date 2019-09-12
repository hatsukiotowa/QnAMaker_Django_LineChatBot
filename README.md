# 시스템목표

LINE 챗봇 개발을 통해 사용자의 질문에 답을 할 수 있게 합니다.
일본 스키장 기본 자료를 챗봇으로 만들어 사용자가 스키장의 이름을 입력하면 비슷한 일본의 큰 스키장의 기본자료를 응답하게 합니다.

![DEMO](demo.jpg)

# 시스템구조

![STRUCTURE](structure.jpg)

# 사전준비

기초 Python 활용능력（Linebot 백엔드）

Command Line 활용능력（Heroku 배치，Run Django）

Git 활용능력（Heroku 배치）

# 사용할 도구
Microsoft Azure: QnAMaker：AI 언어 이해 모듈，透過輸入題庫及答案，丟進去給QnAMaker訓練，輸入類似問題時會自動比對出對應的答案。

Python + Django：搭配Python Line Bot API ，開發自動回應LINE訊息的後端服務Server。

Heroku + Git：部署我們的Linebot後端服務Server

Line Developer管理：須申請Line Developer帳號（或Line生活圈帳號）

# 相關教學文章

[01建造QnaMaker](https://medium.com/@hatsukiotowa/手把手教你搭建聊天機器人-linebot-python-qnamaker-heroku-01建造qnamaker-99b88e8993b4)

[02建造LineBot Backend Server 並部署至Heroku](https://medium.com/@hatsukiotowa/手把手教你搭建聊天機器人-linebot-python-qnamaker-heroku-02建造linebot-backend-server-並部署至heroku-59b36357cd9d)

[03串接QnAMaker Service](https://medium.com/@hatsukiotowa/手把手教你搭建聊天機器人-linebot-python-qnamaker-heroku-03串接qnamaker-service-beb892cd72ee)
