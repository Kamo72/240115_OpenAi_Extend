# -*- coding: cp949 -*-
<<<<<<< HEAD
from distutils import extension
=======
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
import json
import os, shutil, sys
import threading
from time import sleep
import time
from httpx import Headers
from openai import OpenAI
import openai
from openai.pagination import SyncCursorPage, SyncPage

from openai.types import FileObject, FineTune
from openai.types.fine_tuning import FineTuningJob

from Addon.PdfConverter import Pdf2TextConverter;
<<<<<<< HEAD
from Addon.SpeechToTextConverter import SpeechToTextConverter;
=======
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2

from datetime import datetime
import pytz


def dirUp(dire , times) :
    return dirUp(os.path.dirname(dire), times-1) if times >0 else dire

sys.path.append(f'{ dirUp(os.path.abspath(__file__), 3) }')
from Addon.CustomConsolePrinter import printProcess, printError, printNor, printSucceed, printWarning;


class FineTuneManager () :
    def __init__(self) :
        self.pm = None;

        # lecture : str => filePaths : list[str]
        self.trainingTree : dict[str,  list[str]] = {}
        
        # lecture : str => filePaths : list[str]
        self.trainedTree : dict[str,  list[str]] = {}
        
        # lecture : str => modelName : str
        self.modelLib : dict[str,  str] = {}
        

        user_documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
        saveDirectory = "WB38\\Lectures"
        self.rootPath = f"{user_documents_path}\\{saveDirectory}"
        
        
    # 새로운 강좌를 만듭니다.
    def LecturesCreate(self, lecture : str) : 
        
        lecPath = self.__lectureToPath__(lecture=lecture)
        
        # 이미 존재하면 생성 불가
        if os.path.exists(lecPath) :
            printError(f"{lecture} 과목은 이미 존재하기 때문에 생성할 수 없습니다.")
            return False
        
        # 디렉토리 생성
        os.makedirs(lecPath)
        os.makedirs(lecPath + r"\\RAW_DATA");
        os.makedirs(lecPath + r"\\TRAINING_DATA");
        os.makedirs(lecPath + r"\\MERGED_DATASET");
        
        
        # 자료구조에 저장
        self.trainedTree[lecture] = list[str]();
        self.trainingTree[lecture] = list[str]();
        self.modelLib[lecture] = None;
        
        # lecture_info.json 생성
        lectureData = {
            "modelName": None,
            "trainedList" : []
        }
        
        with open(rf"{lecPath}\lecture_info.json", "w") as json_file:
            json.dump(lectureData, json_file)
            
        printSucceed(f"성공적으로 '{lecture}'를 생성하는데 성공했습니다.")
        return True;
    
    # 기존 강좌를 삭제합니다.
    def LecturesDelete(self, lecture : str) :
        
        lecPath = self.__lectureToPath__(lecture=lecture)
        if not os.path.exists(lecPath):
            printError(f"존재하지 않는 과목 '{lecPath}'을 삭제하려고 시도하고 있습니다.")
            return False
            
        # 디렉토리 삭제(내부의 파일까지 모두 삭제함)
        shutil.rmtree(lecPath)
        
        del self.trainingTree[lecture]
        del self.trainedTree[lecture]
        del self.modelLib[lecture]
        printSucceed(f"성공적으로 '{lecture}'를 삭제하는데 성공했습니다.")
        
        return True

    # 강의들 로드
    def LecturesLoad(self) : 
        try :
            # 저장자료 초기화
            self.trainingTree : dict[str,  list[str]] = {}
            self.trainedTree : dict[str,  list[str]] = {}
            self.modelLib : dict[str,  str] = {}
        
            # 모든 과목 디렉토리에 접근

            tPath = self.rootPath;
            directories = [item for item in os.listdir(tPath) if os.path.isdir(os.path.join(tPath, item))]

            for lecture in directories:
                full_path = os.path.join(self.rootPath, lecture)
                
                # lecture_info를 읽어오기
                with open(rf"{full_path}\lecture_info.json", "r") as json_file:
                    data = json.load(json_file)
                    
                    self.modelLib[lecture] = data["modelName"];
                    self.trainedTree[lecture] = data["trainedList"]
                    
                    self.trainingTree[lecture] = list[str]()

                ttPath = full_path + "\\TRAINING_DATA";
                files = [item for item in os.listdir(ttPath) if os.path.isfile(os.path.join(ttPath, item))]                

                # lecture TRAINING_DATA를 읽어오기
                for file_path in files:
                        
                    # MERGED_DATASET은 예외
                    if self.trainingTree[lecture].__contains__(file_path) : continue;
                        
                    # 찾은 트레이닝 데이터 경로를 저장
                    self.trainingTree[lecture].append(file_path)
                            
            printSucceed(f"과목 정보 로드에 성공했습니다. \n학습 예정 자료 : \n{self.trainingTree}\n학습 완료 자료 : \n{self.trainedTree}\n모델 : \n{self.modelLib}")
            return True;
    
        except Exception as ex :
            printError(f"과목 로드가 실패했습니다. 상세 정보 : {ex}")
            input("더 이상의 진행은 위험하므로, 프로세스를 정지합니다.")
            exit()
            
            return False;
    
    # 강의들 저장
    def LecturesSave(self) : 
        tPath = self.rootPath;
        directories = [item for item in os.listdir(tPath) if os.path.isdir(os.path.join(tPath, item))]

        for lecture in directories:
            full_path = os.path.join(self.rootPath, lecture)
                    
            lectureData = {
                "modelName": self.modelLib[lecture],
                "trainedList" : self.trainedTree[lecture]
            }
                    
            # lecture_info를 읽어오기
            with open(rf"{full_path}\lecture_info.json", "w") as json_file:
                json.dump(lectureData, json_file)
    
    # 강의들 리스트
    def LecturesList(self) : 
        return list(self.modelLib.keys())


    # 모델 값을 가져오기
    def GetModel(self, lecture : str) : 
        try :
            modelName : str = self.modelLib[lecture]
        except KeyError as ex :
            printWarning(f"{lecture}과목은 존재하지 않습니다.")
            return "(유효하지 않은 과목)"
        
        if modelName == None or modelName == "" :
            printWarning(f"{lecture}은 파인튜닝 모델이 존재하지 않습니다. 다시 한번 확인해주십시오.")
            return "gpt-3.5-turbo-1106"
        
        printSucceed(f"{lecture}의 파인튜닝 모델({modelName})을 찾았습니다.")
        return modelName


    # 파인튜닝 관리 스레드 시작
    def StartFineTuneChecker(self) :
        thread_unit = threading.Thread(target=self.__threadFineTuneChecker__, args=[30.]);
        thread_unit.start()
    
    # 파인튜닝 관리 스레트
    def __threadFineTuneChecker__(self, frequency : float) :
        try :
            while True :
                try :
                    api = self.pm.api;
                         
                    files :SyncPage[FileObject]

                    ftData, files =  api.GetFineTuneData()
                    ftJobs : list[FineTune] = ftData.data
                    ftFiles : list[FileObject] =  files.data
                
                    self.__fineTuneListPrint__(ftJobs, ftFiles)
                    
                    sleep(frequency)
                    
                except Exception as ex:   
                    printError(ex)
        except Exception as ex:   
            printError(ex)     
    def __fineTuneListPrint__(self, ftJobs : list[FineTune], ftFiles : list[FileObject]) :
        msg = f"<파인튜닝 모델 작업 목록 : {len(ftJobs)}개>\n"
        for job in ftJobs :
            startTime = datetime.fromtimestamp(job.created_at)
                        
            timeFormat = "%Y-%m-%d %H:%M:%S" 
                        
            if (job.status in ["succeeded"]) :
                msg += f"[SUCCEED] [{startTime.strftime(timeFormat)}] [{job.id}] Name : {job.fine_tuned_model} \n"
                            
            elif (job.status in ["failed", "cancelled"]) :
                msg += f"[FAILURE] [{startTime.strftime(timeFormat)}] [{job.id}] Name : {job.fine_tuned_model} \n"
                            
            else :
                msg += f"[PROCESS] [{startTime.strftime(timeFormat)}] [{job.id}] Name : {job.fine_tuned_model} \n"
            
            for trFile in job.result_files :
                print()
                msg += f"\t<{trFile}>\n"
                
        msg += f"<학습 파일 목록 : {len(ftFiles)}개>\n"        
        for file in ftFiles :
            startTime = datetime.fromtimestamp(file.created_at)
                        
            timeFormat = "%Y-%m-%d %H:%M:%S" 
                        
            if (file.status in ["uploaded"]) :
                msg += f"[ UPLOAD] [{startTime.strftime(timeFormat)}] [{file.id}] FileName : {file.filename}({file.bytes}) \n"
                            
            elif (job.status in ["error"]) :
                msg += f"[FAILURE] [{startTime.strftime(timeFormat)}] [{file.id}] FileName : {file.filename}({file.bytes}) \n"
                            
            else :
                msg += f"[DEFAULT] [{startTime.strftime(timeFormat)}] [{file.id}] FileName : {file.filename}({file.bytes}) \n"
                            
        msg += "<목록 끝>\n"
        print(msg)


    # 파인튜닝 시작
    def StartFineTuneJob(self, lectureName : str) :
        try :
            printProcess(f"'{lectureName}' 과목의 자가 학습을 준비 중입니다...")
        
            #머지데이터 생성 
            self.__MergeDataSet__("C# 프로그래밍")
        
            #머지데이터 업로드
            fo : FileObject = self.pm.api.UploadFile("C# 프로그래밍")
         
            #파인튜닝 시작
            ftj : FineTuningJob = openai.fine_tuning.jobs.create(model = "gpt-3.5-turbo-1106", training_file = fo.id)
        
            # 콜백 정의
       
        
            #파인튜닝 작업 추적 스레드 생성
            thread_unit : threading.Thread = threading.Thread(target = self.__threadFineTuneJob__, args = (lectureName, ftj,  self.__FineTuneJobCallback__))
            thread_unit.start()
            printProcess(f"'{lectureName}' 과목의 자가 학습을 시작합니다.")
        

            # 파인튜닝 작업 세이브포인트 생성
            self.__MakeFineTuneCheckPoint__(lecture=lectureName, ft= ftj)
            
            return True
        except :
            return False
        
    # 파인튜닝 스레드
    def __threadFineTuneJob__(self, lectureName : str, ftJobData : FineTuningJob,  callback) : 
        
        ft : FineTuningJob
        
        while True :
            from _240102_OpenAI_API._240102_OpenAI_API.AiProcessSources.ProcessManager import p1, p2
            try :
                printProcess(f"'{lectureName}' 과목의 자가 학습이 진행 중입니다.")
            
                # 파인튜닝 과정 중 정보를 가져온다.
                ft = openai.fine_tuning.jobs.retrieve(ftJobData.id)
            
                #시작 시간, 경과된 초를 얻는다.
                startTime = datetime.fromtimestamp(ft.created_at)
                pastTick = int(time.time()) - ft.created_at
                jobStatus = ft.status       

                printProcess(f"자가학습 쓰레드 - 과목 명 : {lectureName}\t 시작 시간 : {startTime}\t 경과 시간 : {pastTick}초\t 진행 상태 : {jobStatus}")
                
                #해치웠나?
                if(jobStatus in ["succeeded"]) :
                    printSucceed(f"성공적으로 자가학습이 완료되었습니다. 완성된 AI의 모델 키 : {ft.fine_tuned_model}")
                    printSucceed(f"과목 명 : {lectureName}\t 시작 시간 : {startTime}\t 경과 시간 : {ft.finished_at - ft.created_at}초\t 종료 시간 : {datetime.fromtimestamp(ft.finished_at)}")
                    callback(lectureName, ft.fine_tuned_model)
                    break
                
                #망했나?
                elif (jobStatus in ["failed", "cancelled"]) :
                    printError(f"자가학습에 실패했습니다! state : {jobStatus}")
                    printError(f"과목 명 : {lectureName}\t 시작 시간 : {startTime}\t 경과 시간 : {pastTick}초\t 종료 시간 : {pastTick}")
                    
                    #치명적인 오류에 대한 처리
                    self.pm.client.Send(f"FineTuneEnd{p1}{str(False)}{p2}{lectureName}")
                    return
                
            except Exception as e: 
                printError(f"__threadFineTuneJob__ 에러 : {e}\n{e.with_traceback.format_exc()}")
                
                #치명적인 오류에 대한 처리
                self.pm.client.Send(f"FineTuneEnd{p1}{str(False)}{p2}{lectureName}")
                return 
              
            #아니야? 그럼 반복  
            sleep(10.)
        
        # 결과 반환
        callback(ft.fine_tuned_model, lectureName)
    
    # 파인튜닝 스레드 콜백
    def __FineTuneJobCallback__ (self, lectureName, modelName) : 
        from _240102_OpenAI_API._240102_OpenAI_API.AiProcessSources.ProcessManager import p1, p2
        try :
            # 이미 같은 값이 있을 시 스킵.
            if(self.modelLib[lectureName] == modelName) : return;
        
            # 기존 모델은 삭제
            printProcess(f"{lectureName}의 모델을 {modelName}로 교체합니다.")
            if(self.modelLib[lectureName] != None) :
                printProcess(f"기존 모델 {self.modelLib[lectureName]}을 제거합니다...")
                self.pm.api.DeleteFineTuneModel(self.modelLib[lectureName])
                
            #새로운 모델 복붙
            printProcess(f"새로운 모델 {modelName}을 배치합니다.")
            self.modelLib[lectureName] = modelName
            self.trainedTree[lectureName] = self.trainingTree[lectureName]
            
            self.LecturesSave()
        
            # 끝났으니 정상적인 종료 반응 보이기
            self.pm.client.Send(f"FineTuneEnd{p1}{str(True)}{p2}{lectureName}")
            
        except Exception as ex:
            # 비정상적인 종료에 대해 반응 보이기
            printError(f"파인튜닝 콜백에서 오류 발생 : {ex}\n{ex.with_traceback.format_exc()}")
            self.pm.client.Send(f"FineTuneEnd{p1}{str(False)}{p2}{lectureName}")


    # 로우 데이터를 패쓰를 통해 복사해 옵니다. txt > txt
    def AddRawData(self, lecture : str, txtFilePath : str) : 
        try:
            # 텍스트 파일의 내용 읽어오기
            with open(txtFilePath, "r", encoding ="utf-8") as source_file:
                file_content = source_file.read()

            # 새로운 디렉토리에 텍스트 파일 생성하고 내용 복사
            file_name = os.path.basename(txtFilePath)
            destination_path = rf"{self.__lectureToPath__(lecture)}\RAW_DATA\{file_name}"

            with open(destination_path, "w", encoding ="utf-8") as destination_file:
                destination_file.write(file_content)
            
            if not self.trainingTree[lecture].__contains__(file_name) :
                self.trainingTree[lecture].append(file_name);
            self.LecturesSave();
            
            printSucceed(f"로우 데이터를 추가 완료: {destination_path}")
            return True;
    
        except FileNotFoundError:
            printError(f"로우 데이터를 추가하지 못헀습니다. 해당 파일을 찾을 수 없습니다. {txtFilePath}")
            return False;
        
        except Exception as e:
            printError(f"로우 데이터 추가 중, 오류 발생: <{txtFilePath}> {e}")
            return False;

    # pdf > txt
    def AddPdfData(self, lecture : str, pdfFilePath : str) : 
        try:
            
            # 새로운 디렉토리에 텍스트 파일 생성하고 내용 복사
            file_name = os.path.basename(pdfFilePath).replace('.pdf','')
            destination_path = rf"{self.__lectureToPath__(lecture)}\RAW_DATA\{file_name}.txt"

            pdfCon = Pdf2TextConverter();
            pdfCon.convert(pdfFilePath, destination_path)
            
            if not self.trainingTree[lecture].__contains__(file_name) :
                self.trainingTree[lecture].append(file_name);
            self.LecturesSave();
            
            printSucceed(f"로우 데이터를 추가 완료: {destination_path}")
            return True;
    
        except FileNotFoundError:
            printError(f"로우 데이터를 추가하지 못헀습니다. 해당 파일을 찾을 수 없습니다. {pdfFilePath}")
            return False;
        
        except Exception as e:
            printError(f"로우 데이터 추가 중, 오류 발생: {pdfFilePath} - {e}")
            return False;
        
<<<<<<< HEAD
    # wav > txt
    def AddWavData(self, lecture : str, wavFilePath : str) : 
        try:
            # 새로운 디렉토리에 텍스트 파일 생성하고 내용 복사
            extension = os.path.splitext(wavFilePath)[1]
            file_name = os.path.basename(wavFilePath).replace(extension,'')
            destination_path = rf"{self.__lectureToPath__(lecture)}\RAW_DATA\{file_name}.txt"

            sttc = SpeechToTextConverter();
            gsutil = sttc.upload_file(wavFilePath);
            transcript = sttc.transcribe_gcs(gsutil);      
            
            with open(destination_path, "w", encoding="utf-8") as file :
                file.write(transcript)

            if not self.trainingTree[lecture].__contains__(file_name) :
                self.trainingTree[lecture].append(file_name);
            self.LecturesSave();
            
            printSucceed(f"로우 데이터를 추가 완료: {destination_path}")
            return True;
    
        except FileNotFoundError:
            printError(f"로우 데이터를 추가하지 못헀습니다. 해당 파일을 찾을 수 없습니다. {wavFilePath}")
            return False;
        
        except Exception as e:
            printError(f"로우 데이터 추가 중, 오류 발생: {wavFilePath} - {e}")
            return False;
=======
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
  
         
    # 가져온 로우 데이터로 GPT 를 사용해 학습 데이터로 만듭니다. txt > json
    def __MakeDataSet__(self, lecture : str, txtFilePath : str) : 
        
        printProcess(f"로우 데이터에서 GPT를 이용해 학습 데이터를 추출합니다...  대상 파일 : {txtFilePath}...")
        
        api = self.pm.api;
        #학습 내용 추출
        dataSet : list = api.InitDataSet(lecture, txtFilePath);
        
        # 저장할 텍스트 jsonl
        txtFileName = os.path.basename(txtFilePath).replace(".txt", "")
        dataSetPath : str = fr"{self.__lectureToPath__(lecture)}\TRAINING_DATA\{txtFileName}.jsonl"
        
        printSucceed(f"로우 데이터에서 GPT를 이용해 학습 데이터를 추출하는데 성공했습니다 대상 파일 : {dataSetPath}...")
        
        with open(dataSetPath, "w", encoding = "utf-8") as json_file:
            json_file.write(json.dumps(dataSet, ensure_ascii=False))
    
    # 해당 강좌의 모든 데이터셋을 하나로 합쳐 업로드를 준비합니다. json, json... > jsonl
    def __MergeDataSet__(self, lecture : str) : 
        
        printProcess(f"'{lecture}'과목의 통합 데이터 생성을 시작합니다... ")
        
        lecPath = self.__lectureToPath__(lecture);        
        trainingFileDir = rf"{lecPath}\TRAINING_DATA"

        jsonl_contents = []

        # 디렉토리 내부의 파일들 가져오기
        files = [f for f in os.listdir(trainingFileDir) if os.path.isfile(os.path.join(trainingFileDir, f))]

        # JSONL 파일들에 대해 반복
        for file_name in files: 
            if file_name.endswith('.jsonl'):
                jsonlPath = os.path.join(trainingFileDir, file_name)
                with open(jsonlPath, 'r', encoding='utf-8') as jsonl_file:
                    # 파일 내용 읽어오기
                    file_content = jsonl_file.read()
                    dataList = json.loads(file_content)
                    jsonl_contents.extend([data for data in dataList])

        
        dataSetPath : str = fr"{self.__lectureToPath__(lecture)}\MERGED_DATASET\{lecture}_MERGED.jsonl"

        with open(dataSetPath, "w", encoding="utf-8") as json_file:
            
            for item in jsonl_contents:
                json_file.write(json.dumps(item, ensure_ascii=False) + '\n')
            
        printSucceed(f"'{lecture}'과목의 통합 데이터를 생성하는데에 성공했습니다. 경로 : {dataSetPath}")
    
    # 과목 이름으로 빠른 경로 찾기
    def __lectureToPath__(self, lecture : str) :
        filePath : str = f"{self.rootPath}\\{lecture}"
        return filePath 
    
    
    # 파인튜닝 잡 세이브포인트 생성
    def __MakeFineTuneCheckPoint__(self, lecture : str, ft : FineTuningJob) : 
        user_documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
        saveDirectory = "WB38"
        cpPath = f"{user_documents_path}\\{saveDirectory}\\finetune_checkpoint.json"
        
        dataPre : list
        
        with open(cpPath, "r", encoding="utf-8") as jsonFile :
            dataPre = json.load(jsonFile)
            
        dataPre.append({"lecture" : lecture, "fineTuneJob" : ft.id})
        
        with open(cpPath, "w", encoding="utf-8") as jsonFile :
            json.dump(dataPre, jsonFile, ensure_ascii=False)
            
        printSucceed(f"'{lecture}' 과목의 자가 학습 세이브포인트를 저장헀습니다!")
        
    # 파인튜닝 잡 세이브 포인트 로드. 적합한 파인튜닝 잡이 있을 시, 스레드 재생성
    def __LoadFineTuneCheckPoint__(self) : 
        try : 
            user_documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
            saveDirectory = "WB38"
            cpPath = f"{user_documents_path}\\{saveDirectory}\\finetune_checkpoint.json"
            
            # 세이브 포인트 로드
            dataPre : list
            with open(cpPath, "r", encoding="utf-8") as jsonFile :
                dataPre = json.load(jsonFile)
        
            # API의 진행중인 잡들을 로드
            from ApiManager import OpenAiManagerV2 
            api : OpenAiManagerV2 = self.pm.api;
            ftData, files = api.GetFineTuneData()
            ftJobs : list[FineTuningJob] = ftData.data
    
            # 세이브 포인트들을 순회하며 진행중인 잡들을 확인

            for data in  dataPre : # 세이브포인트 순회
            
                lecture : str = data["lecture"]
                ftId : str = data["fineTuneJob"]
            
                for ftJob in ftJobs : # 파인튜닝 잡 순회
                    if(ftJob.id == ftId) :  # 세이브포인트와 일치
                        if(ftJob.status in ["failed", "cancelled"]) : #유효하지 않은 파인튜닝 잡
                            printError(f"'{lecture}' 과목의 세이브포인트를 불러오는데 실패했습니다. state : {ftJob.status}")
                            break;
        
                        #파인튜닝 작업 추적 스레드 생성
                        thread_unit : threading.Thread = threading.Thread(target = self.__threadFineTuneJob__, args = (lecture, ftJob, self.__FineTuneJobCallback__))
                        thread_unit.start()
                        printSucceed(f"'{lecture}' 과목의 자가 학습 세이브포인트를 불러왔습니다!")
            
            with open(cpPath, "w", encoding="utf-8") as jsonFile :
                json.dump([], jsonFile, ensure_ascii=False)
                
        except FileNotFoundError as ex :
            printWarning(f" finetune_checkpoint.json 파일이 존재하지 않습니다. 새로 생성합니다. ")
            with open(cpPath, "w", encoding="utf-8") as jsonFile :
                json.dump([], jsonFile, ensure_ascii=False)
            
        except Exception as ex : 
            printError(f"__LoadFineTuneCheckPoint__ 실행 중 오류발생. {ex}\n{ex.with_traceback.format_exc()}")
               
