# -*- coding: cp949 -*-
import sys
import time
from AiModuleProcess import AiModuleProcess


# AI �� ��뿹.
try :
    ai = AiModuleProcess();
<<<<<<< HEAD
    # ai.DoSendDataPpt("C# ���α׷���", r"C:\Users\skyma\Downloads\Win32API.pptx")
    # ai.DoSendDataWav("C# ���α׷���", r"C:\Users\skyma\Downloads\0ee369ae-e4df-4f8e-907f-a4977376fc78.wav")
=======
    
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
    # ai.ExecuteDebugCode();
    # ai.ExecuteTestQandA

    # ai.DoLectureCreate("�ڻ����� �ɷη���")
    # ai.DoSendDataTxt("�ڻ����� �ɷη���", r"S:\[GitHub]\240102_OpenAI_API\�� �ؽ�Ʈ ����.txt")
    # time.sleep(1.)
    # ai.DoFineTuneCreate("�ڻ����� �ɷη���")
<<<<<<< HEAD

    # ai.DoGetAnswer("112", "C# ���α׷���", r"�����̵忡�� ȸ�� ������ ����,  �˻�, ����, �����ϴ� ���α׷��� ��ɰ� ���õ� ������ ���ԵǾ� �ֽ��ϴ�. ȸ�� ������ �������� �̷��� �ֳ���?")
    ai.ExecuteTestQandA("C# ���α׷���");
=======
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
    sys.exit()

except Exception as ex : 
    print(ex + ex.with_stacktrace().format_exc())
