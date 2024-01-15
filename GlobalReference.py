import subprocess
import os

def dirUp(dire , times) :
    return dirUp(os.path.dirname(dire), times-1) if times >0 else dire

<<<<<<< HEAD
# ëª…ë ¹ì–´ ì„¤ì •
cmd_command = 'setx OPENAI_API_KEY "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"'
subprocess.run(cmd_command, shell=True)


# í˜„ìž¬ ìž‘ì—… ë””ë ‰í† ë¦¬ ê°€ì ¸ì˜¤ê¸°
=======
# ¸í·É¾î ¼³Á¤
cmd_command = 'setx OPENAI_API_KEY "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"'
subprocess.run(cmd_command, shell=True)


# ÇöÀç ÀÛ¾÷ µð·ºÅä¸® °¡Á®¿À±â
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
current_directory = os.path.dirname(os.path.abspath(__file__))


envPath = fr"{current_directory}\_240102_OpenAI_API"
initPath = fr"{current_directory}\_240102_OpenAI_API\AiProcessSources\ProcessManager.py"
cmdProcessPath = fr"{current_directory}\_240102_OpenAI_API\AiProcessSources\AI_PROCESS_INIT.py"



parseMark = ["^&*)", "$%^&!"]
PARSER = parseMark