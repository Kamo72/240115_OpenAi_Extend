# -*- coding: cp949 -*-
import sys
import time
from AiModuleProcess import AiModuleProcess


# AI 모델 사용예.
try :
    ai = AiModuleProcess();
<<<<<<< HEAD
    # ai.DoSendDataPpt("C# 프로그래밍", r"C:\Users\skyma\Downloads\Win32API.pptx")
    # ai.DoSendDataWav("C# 프로그래밍", r"C:\Users\skyma\Downloads\0ee369ae-e4df-4f8e-907f-a4977376fc78.wav")
=======
    
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
    # ai.ExecuteDebugCode();
    # ai.ExecuteTestQandA

    # ai.DoLectureCreate("박상한의 케로로학")
    # ai.DoSendDataTxt("박상한의 케로로학", r"S:\[GitHub]\240102_OpenAI_API\새 텍스트 문서.txt")
    # time.sleep(1.)
    # ai.DoFineTuneCreate("박상한의 케로로학")
<<<<<<< HEAD

    # ai.DoGetAnswer("112", "C# 프로그래밍", r"슬라이드에는 회원 정보를 저장,  검색, 수정, 삭제하는 프로그램의 기능과 관련된 내용이 포함되어 있습니다. 회원 정보는 무엇으로 이뤄져 있나요?")
    ai.ExecuteTestQandA("C# 프로그래밍");
=======
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
    sys.exit()

except Exception as ex : 
    print(ex + ex.with_stacktrace().format_exc())
