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
Microsoft Azure: QnAMaker：AI 언어 이해 모듈，질문과 답을 통해 QnAMaker를 훈련하고 입력한 내용과 유사한 경우 자동으로 어울리는 답을 출력하게 함.

Python + Django：Python Line Bot API를 사용하여 LINE 메세지에 자동으로 응답하는 백엔드 서비스 서버를 개발.

Heroku + Git：Linebot 백엔드 서비스 서버 배포.

Line Developer 관리：Line Developer 계정 (또는 Line@ 계벙）

# 관련 학습 글

[01 QnaMaker만들기](https://medium.com/@hatsukiotowa/手把手教你搭建聊天機器人-linebot-python-qnamaker-heroku-01建造qnamaker-99b88e8993b4)

[02 Heroku에 LineBot Backend Server 배포하기](https://medium.com/@hatsukiotowa/手把手教你搭建聊天機器人-linebot-python-qnamaker-heroku-02建造linebot-backend-server-並部署至heroku-59b36357cd9d)

[03 QnAMaker Service 연결하기](https://medium.com/@hatsukiotowa/手把手教你搭建聊天機器人-linebot-python-qnamaker-heroku-03串接qnamaker-service-beb892cd72ee)
