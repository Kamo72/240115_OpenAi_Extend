# -*- coding: cp949 
import subprocess
import os

def dirUp(dire , times) :
    return dirUp(os.path.dirname(dire), times-1) if times >0 else dire

# ��ɾ� ����
cmd_command = 'setx OPENAI_API_KEY "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"'
subprocess.run(cmd_command, shell=True)


# ���� �۾� ���丮 ��������
current_directory = os.path.dirname(os.path.abspath(__file__))


envPath = fr"{current_directory}\_240102_OpenAI_API"
initPath = fr"{current_directory}\_240102_OpenAI_API\AiProcessSources\ProcessManager.py"
cmdProcessPath = fr"{current_directory}\_240102_OpenAI_API\AiProcessSources\AI_PROCESS_INIT.py"



parseMark = ["^&*)", "$%^&!"]
PARSER = parseMark