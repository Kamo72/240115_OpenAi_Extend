# -*- coding: cp949 
import subprocess
import os

def dirUp(dire , times) :
    return dirUp(os.path.dirname(dire), times-1) if times >0 else dire

# 명령어 설정
<<<<<<< HEAD
cmd_command = 'setx OPENAI_API_KEY "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"'
=======
cmd_command = 'setx OPENAI_API_KEY "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"'
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
subprocess.run(cmd_command, shell=True)


# 현재 작업 디렉토리 가져오기
current_directory = os.path.dirname(os.path.abspath(__file__))


envPath = fr"{current_directory}\_240102_OpenAI_API"
initPath = fr"{current_directory}\_240102_OpenAI_API\AiProcessSources\ProcessManager.py"
cmdProcessPath = fr"{current_directory}\_240102_OpenAI_API\AiProcessSources\AI_PROCESS_INIT.py"



parseMark = ["^&*)", "$%^&!"]
PARSER = parseMark