# -*- coding: cp949 -*-
import sys
import time
from AiModuleProcess import AiModuleProcess


# AI 모델 사용예.
try :
    ai = AiModuleProcess();
    
    # ai.ExecuteDebugCode();
    # ai.ExecuteTestQandA

    # ai.DoLectureCreate("박상한의 케로로학")
    # ai.DoSendDataTxt("박상한의 케로로학", r"S:\[GitHub]\240102_OpenAI_API\새 텍스트 문서.txt")
    # time.sleep(1.)
    # ai.DoFineTuneCreate("박상한의 케로로학")
    sys.exit()

except Exception as ex : 
    print(ex + ex.with_stacktrace().format_exc())
