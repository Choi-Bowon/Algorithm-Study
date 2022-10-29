from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

from email.mime.base import MIMEBase 
from email import encoders
from os.path import basename

import smtplib

# 이메일 발송을 위한 상수 변수들 설정
SMTP_SERVER='smtp.naver.com'
SMTP_PORT=465
SMTP_USER='cbw1999@naver.com'
SMTP_PASSWORD= open('email_config','r').read().rstrip() # 파일 읽어와서 저장

def send_mail(from_user:str,to_users:list,subject:str,content:str,attachment:list=[],cc_targets=None):
    '''
    메일을 발송하는 함수입니다.

    **필수값**
    from_user:
    to_users:
    subject:
    content:

    **선택**

    '''

    try:
        # 이메일 전송 서버에 접속
        smtp=smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
        print('메일 전송 서버 접속 성공')
        smtp.login(SMTP_USER,SMTP_PASSWORD)
        print('로그인 성공 !')
        msg=MIMEMultipart('alternative')

        # 첨부 파일 여부
        if email_file:
            mag=MIMEMultipart('mixed')

            for attachment in attachments:
                # 파일 담을 공간
                email_file = MIMEBase('application', 'octet-stream') 

            # 파일 읽어오기
            with open(attachment, 'rb') as f:
                file_data = f.read()

            # 파일 데이터를 첨부파일에 담아준다.
            email_file.set_payload(file_data)
            # base64 인코딩형식으로 인코딩
            encoders.encode_base64(email_file)

            file_name = basename(attachment) 
            email_file.add_header('Content-Disposition', 'attachment', filename=file_name)

            msg.attach(email_file)

        # 편지 내용
        contents="테스트"

        msg['From']=from_user
        msg['To']='cbw1999@naver.com'
        msg['Subject']='제목제목'

        # 편지지를 편지봉토에 담아준다.
        text=MIMEText(contents)
        msg.attach(text)

        # sendmail('보내는 사람','받는 사람',msg.as_string())
        smtp.sendmail(from_user,','.join(to_users+cc_targets),msg.as_string())
        print('이메일 발송 성공')

        return True
        
    except Exception as e:
        # 에러 났을 때 실행할 코드
        print('#### 에러 발생 ####')
        print(e)
    finally:
        # 에러 여부 상관없이 무조건 실행할 코드
        # smtp 연결 해제
        smtp.close()
        print('파이널리')