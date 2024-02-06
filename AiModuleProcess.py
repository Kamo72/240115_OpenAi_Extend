# -*- coding: cp949 -*-
import os, threading, time, subprocess
import socket
import GlobalReference
from _240102_OpenAI_API.AiProcessSources.Addon.CustomConsolePrinter import printError, printNor, printProcess, printSucceed, printWarning
from _240102_OpenAI_API.AiProcessSources.Addon.ServerAndClient import Server


class AiModuleProcess():
    def __init__(self) :
    
        self.p1 = GlobalReference.PARSER[0]
        self.p2 = GlobalReference.PARSER[1]        

        self.loadAiThread : threading.Thread = None
        self.initAiThread : threading.Thread = None
        
        self.server : Server;
        self.clientIsAvailable : bool = False;
        
        self.__ServerInit__()
    
    def __ServerInit__(self) :
        # ���� ����
        self.server = Server('127.0.0.1', 4090, self.__ServerDel__)
        self.server.Deploy()

        #������ ������ Ŭ���̾�Ʈ�� ���� AI ���μ����� �ҷ��´�.
        self.__LoadAiProcess__()
        
        while self.clientIsAvailable == False : time.sleep(1.)
        
    def __ServerDel__(self, client_socket : socket, packet) :
        p1 = self.p1
        p2 = self.p2
        
        sp = packet.split(p1)
        flag = sp[0]
        
        try : 
            match flag: 
                case "ProcessStart": 
                    self.clientIsAvailable = True;
            
                case "ProcessEnd":
                    ssp = sp[1].split(p2)
                    isSucceed = True if ssp[0] == str(True) else False
                    if isSucceed :
                        printSucceed("���������� AI ���μ����� ����ƽ��ϴ�.")
                    else:
                        printWarning("AI ���μ��� ���� �� �� �� ���� ������ �־����ϴ�. AI ���μ����� Ȯ�����ּ���.")
                    
                case "LectureCreate":
                    ssp = sp[1].split(p2)
                    isSucceed = True if ssp[0] == str(True) else False
                    lecture = ssp[1]
                    
                    if isSucceed :
                        printSucceed(f"���������� '{lecture}' ������ �����߽��ϴ�.")
                    else:
                        printError(f"'{lecture}' ������ �����ϴµ� �����߽��ϴ�.")
                
                case "LectureDelete": 
                    ssp = sp[1].split(p2)
                    isSucceed = True if ssp[0] == str(True) else False
                    lecture = ssp[1]
                    
                    if isSucceed :
                        printSucceed(f"���������� '{lecture}' ������ �����߽��ϴ�.")
                    else:
                        printError(f"'{lecture}' ������ �����ϴµ� �����߽��ϴ�.")
                
                case "LectureList":
                    ssp = sp[1].split(p2)
                    lecList = list(filter(None, ssp[0].split(p2)))
                    
                    ret = f"���������� ���� ����Ʈ�� �ҷ����� ����. ({len(lecList)}��)\n"
                    for lec in lecList : ret += f"{lecList}\n"

                    printSucceed(ret)
                
                case "SendDataPpt": 
                    ssp = sp[1].split(p2)
                    isSucceed = True if ssp[0] == str(True) else False
                    lecture = ssp[1]
                    path = ssp[2]
                    
                    if isSucceed :
                        printSucceed(f"���������� '{path}' PPT������ '{lecture}'������ ���ε��߽��ϴ�.")
                    else:
                        printError(f"'{path}' PPT������ '{lecture}'���� ���ε��ϴµ� �����߽��ϴ�.")
                        
                case "SendDataPdf": 
                    ssp = sp[1].split(p2)
                    isSucceed = True if ssp[0] == str(True) else False
                    lecture = ssp[1]
                    path = ssp[2]
                    
                    if isSucceed :
                        printSucceed(f"���������� '{path}' PDF������ '{lecture}'������ ���ε��߽��ϴ�.")
                    else:
                        printError(f"'{path}' PDF������ '{lecture}'���� ���ε��ϴµ� �����߽��ϴ�.")
                
                case "SendDataWav":
                    ssp = sp[1].split(p2)
                    isSucceed = True if ssp[0] == str(True) else False
                    lecture = ssp[1]    
                    path = ssp[2]
                    
                    if isSucceed :
                        printSucceed(f"���������� '{path}' ���� ������ '{lecture}'������ ���ε��߽��ϴ�.")
                    else:
                        printError(f"'{path}' ���� ������ '{lecture}'���� ���ε��ϴµ� �����߽��ϴ�.")
                
                case "SendDataTxt": 
                    ssp = sp[1].split(p2)
                    isSucceed = True if ssp[0] == str(True) else False
                    lecture = ssp[1]
                    path = ssp[2]
                    
                    if isSucceed :
                        printSucceed(f"���������� '{path}' TXT������ '{lecture}'������ ���ε��߽��ϴ�.")
                    else:
                        printError(f"'{path}' TXT������ '{lecture}'���� ���ε��ϴµ� �����߽��ϴ�.")
                
                case "FineTuneCreate":
                    ssp = sp[1].split(p2)
                    isSucceed = True if ssp[0] == str(True) else False
                    lecture = ssp[1]
                    
                    if isSucceed :
                        printSucceed(f"'{lecture}'������ ����Ʃ���� ���۵ƽ��ϴ�.")
                    else:
                        printSucceed(f"'{lecture}'������ ����Ʃ���� ���������� ���۵��� �ʾҽ��ϴ�. AI ���μ����� Ȯ�����ֽʽÿ�.")
                
                case "FineTuneEnd" : 
                    ssp = sp[1].split(p2)
                    isSucceed = True if ssp[0] == str(True) else False
                    lecture = ssp[1]
                    
                    if isSucceed :
                        printSucceed(f"���������� '{lecture}'������ ����Ʃ���� �������ϴ�.")
                    else:
                        printSucceed(f"'{lecture}'������ ����Ʃ���� ���������� ������� ����ƽ��ϴ�. AI ���μ����� Ȯ�����ֽʽÿ�.")
                
                case "GetModel":
                    ssp = sp[1].split(p2)
                    lecture = ssp[0]
                    modelName = ssp[1]
                    
                    printSucceed(f"'{lecture}'������ ���� '{modelName}' ���� ��� ���Դϴ�.")
                
                case "SessionDelete": 
                    ssp = sp[1].split(p2)
                    isSucceed = True if ssp[0] == str(True) else False
                    sid = ssp[1]
                    lecture = ssp[2]
                
                    if isSucceed :
                        printSucceed(f"���������� '{sid}'������� '{lecture}' ���� ������ �����ƽ��ϴ�.")
                    else:
                        printSucceed(f"'{sid}'������� '{lecture}' ���� ������ �����ϴµ��� �����߽��ϴ�.")
                
                case "GetAnswer": 
                    ssp = sp[1].split(p2)
                    sid = ssp[0]
                    lecture = ssp[1]
                    answer = ssp[2]
                    image = ssp[3]
                
                    printSucceed(f"['{sid}' ������� '{lecture}' ����] : {answer}\n [image]{image}")
            
                case _:
                    if flag == "" : return;
            
                    printWarning(f"""'{flag}'�� ��ȿ�� ��Ŷ Ÿ���� �ƴմϴ�. reciecve : {packet}""")
            

        except Exception as ex:
            printError(f"���� ��� �� ���ܰ� �߻��߽��ϴ�! {ex}\n{ex.with_stacktrace().format_exc()}")
            

    # ���μ��� �ε� �Լ�
    def __LoadAiProcess__(self) :
        
        server = self.server
        
        def LoadAiThread (server : Server) :
            printProcess("AI ���μ����� �ε� ���Դϴ�. ��ø� ��ٷ� �ֽʽÿ�...")
            
            # AI ���μ����� ���ο� â���� ����.
            program_path = GlobalReference.cmdProcessPath
            subprocess.Popen(["python", program_path], creationflags=subprocess.CREATE_NEW_CONSOLE)

            # AI ���μ����� �⵿�� ������ ���
            while self.clientIsAvailable == False : pass
            printProcess("AI ���μ����� �ε�Ǿ����ϴ�!")
        
        def InitAiThread (server : Server) :
            while True :
            
                if len(server.clients) != 0 or self.clientIsAvailable == False :
                    time.sleep(1.0);
                    continue
            
                self.clientIsAvailable = False
                server.clients = [];
            
                printError("AI ���μ����� ���������� ���� ���ᰡ �߻��߽��ϴ�.")
                printError("AI ���μ����� �ٽ� �����մϴ�. ���α׷��� �����Ϸ��� ������ ���� �����Ͻʽÿ�.")
                self.loadAiThread = threading.Thread(target= LoadAiThread, args=[server])
                self.loadAiThread.start()
    
        self.loadAiThread = threading.Thread(target= LoadAiThread, args= [server])
        self.loadAiThread.start()
        self.initAiThread = threading.Thread(target= InitAiThread, args= [server])
        self.initAiThread.start()
    
        # AI ���μ����� �⵿�� ������ ���
        while self.clientIsAvailable == False : pass
    
    # ����׿� ��� üũ
    def ExecuteDebugCode(self) : 
        
        printNor("�׽�Ʈ �ڵ�� ����� Ȯ���� �����մϴ�...")
        
        # ���
        user_documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
        saveDirectory = "WB38\\Lectures"
        rootPath = f"{user_documents_path}\\{saveDirectory}"
        
        # �׽�Ʈ�� �� PDF
        from reportlab.pdfgen import canvas
        pdfPath = f"{rootPath}\\empty_pdf.pdf"
        c = canvas.Canvas(pdfPath)
        c.save()
        
        printProcess(f"�� PDF ������ {pdfPath} ��ο� �����Ǿ����ϴ�.")

        # �׽�Ʈ�� �� TXT
        txtPath = f"{rootPath}\\empty_txt.txt"
        with open(txtPath, "w", encoding="utf-8") as file :
            file.write("asdadsa");
        
        printProcess(f"�� TXT ������ {txtPath} ��ο� �����Ǿ����ϴ�.")

        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        
        server = self.server;
        
        # ���� �׽�Ʈ ���� ����

        self.DoLectureCreate("�������� ���� ����")
        time.sleep(1.0)
        self.DoLectureDelete("�������� ���� ����")
        time.sleep(1.0)
        self.DoLectureCreate("�ڻ����� �ɷη���")
        time.sleep(1.0)
        self.DoLectureList()
        time.sleep(1.0)
        
        
        self.DoGetModel("�ڻ����� �ɷη���")
        time.sleep(1.0)
        self.DoGetAnswer("1", "�ڻ����� �ɷη���", "C#���� �������� �ּ��� ����ϴ� ����� ���� �˷���.")
        time.sleep(1.0)
        self.DoSessionDelete("1", "�ڻ����� �ɷη���")
        time.sleep(1.0)
        self.DoSendDataPdf("�ڻ����� �ɷη���", {pdfPath})
        time.sleep(1.0)
        self.DoSendDataTxt("�ڻ����� �ɷη���", {txtPath})
        time.sleep(1.0)
        
        #self.DoFineTuneCreate("�ڻ����� �ɷη���")
        time.sleep(1.0)
        
        printNor("�׽�Ʈ �ڵ�� ����� Ȯ���� ���ƽ��ϴ�...")
        
    # ����׿� Q and A
    def ExecuteTestQandA(self, lecture : str) :
        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        
        server = self.server;
        
        #������ ������ ����
        sid = 0;
        lectureName = lecture
    
        while True :
            inputText = input(f"(sid : {sid})�� ({lectureName} ����) ���� : ")
            server.Send(f"GetAnswer{p1}{sid}{p2}{lectureName}{p2}{inputText}")
            sid+=1
        

    def DoLectureCreate(self, lecture : str) :
        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        server = self.server;
        
        server.Send(f"LectureCreate{p1}{lecture}")
        
    def DoLectureDelete(self, lecture : str) :
        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        server = self.server;
        
        server.Send(f"LectureDelete{p1}{lecture}")
        
    def DoLectureList(self) :
        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        server = self.server;
        
        server.Send(f"LectureList{p1}")

    def DoGetModel(self, lecture : str) :
        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        server = self.server;
        
        server.Send(f"GetModel{p1}{lecture}")
        
    def DoGetAnswer(self, sid : str, lecture : str, question : str) :
        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        server = self.server;
        
        server.Send(f"GetAnswer{p1}{sid}{p2}{lecture}{p2}{question}")
        
    def DoSessionDelete(self, sid : str, lecture : str) :
        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        server = self.server;
        
        server.Send(f"SessionDelete{p1}{sid}{p2}{lecture}")
            
    def DoSendDataPpt(self, lecture : str, path : str) :
        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        server = self.server;
        
        server.Send(f"SendDataPpt{p1}{lecture}{p2}{path}")
        
    def DoSendDataPdf(self, lecture : str, path : str) :
        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        server = self.server;
        
        server.Send(f"SendDataPdf{p1}{lecture}{p2}{path}")
        
    def DoSendDataTxt(self, lecture : str, path : str) :
        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        server = self.server;
        
        server.Send(f"SendDataTxt{p1}{lecture}{p2}{path}")
        
    def DoSendDataWav(self, lecture : str, path : str) :
        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        server = self.server;
        
        server.Send(f"SendDataWav{p1}{lecture}{p2}{path}")
    
    def DoFineTuneCreate(self, lecture : str) :
        # ��Ÿ �������� ª�� ó��
        p1 = self.p1
        p2 = self.p2
        server = self.server;
        
        server.Send(f"FineTuneCreate{p1}{lecture}")



