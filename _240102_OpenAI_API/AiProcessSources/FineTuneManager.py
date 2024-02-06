<<<<<<< HEAD
ï»¿# -*- coding: utf-8 -*-
from distutils import extension
=======
# -*- coding: cp949 -*-
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
import json
import os, shutil, sys
import threading
from time import sleep
import time
from httpx import Headers
<<<<<<< HEAD

import openai
from openai import OpenAI
from openai.pagination import SyncCursorPage, SyncPage
=======
from openai import OpenAI
import openai
from openai.pagination import SyncCursorPage, SyncPage

>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
from openai.types import FileObject, FineTune
from openai.types.fine_tuning import FineTuningJob

from Addon.PdfConverter import Pdf2TextConverter;
<<<<<<< HEAD
from Addon.SpeechToTextConverter import SpeechToTextConverter;
=======
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2

from datetime import datetime
import pytz


<<<<<<< HEAD

=======
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
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
        
<<<<<<< HEAD
        self.imageData : dict[str, dict[str,  str]] = {}
        
        self.uploadingCount : dict[str, int] = {}
=======
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2

        user_documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
        saveDirectory = "WB38\\Lectures"
        self.rootPath = f"{user_documents_path}\\{saveDirectory}"
        
        
<<<<<<< HEAD
    # ìƒˆë¡œìš´ ê°•ì¢Œë¥¼ ë§Œë“­ë‹ˆë‹¤.
=======
    # »õ·Î¿î °­ÁÂ¸¦ ¸¸µì´Ï´Ù.
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
    def LecturesCreate(self, lecture : str) : 
        
        lecPath = self.__lectureToPath__(lecture=lecture)
        
<<<<<<< HEAD
        # ì´ë¯¸ ì¡´ì¬í•˜ë©´ ìƒì„± ë¶ˆê°€
        if os.path.exists(lecPath) :
            printError(f"{lecture} ê³¼ëª©ì€ ì´ë¯¸ ì¡´ì¬í•˜ê¸° ë•Œë¬¸ì— ìƒì„±í•  ìˆ˜ ì—†ìŠµë‹ˆë‹¤.")
            return False
        
        # ë””ë ‰í† ë¦¬ ìƒì„±
=======
        # ÀÌ¹Ì Á¸ÀçÇÏ¸é »ı¼º ºÒ°¡
        if os.path.exists(lecPath) :
            printError(f"{lecture} °ú¸ñÀº ÀÌ¹Ì Á¸ÀçÇÏ±â ¶§¹®¿¡ »ı¼ºÇÒ ¼ö ¾ø½À´Ï´Ù.")
            return False
        
        # µğ·ºÅä¸® »ı¼º
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
        os.makedirs(lecPath)
        os.makedirs(lecPath + r"\\RAW_DATA");
        os.makedirs(lecPath + r"\\TRAINING_DATA");
        os.makedirs(lecPath + r"\\MERGED_DATASET");
        
        
<<<<<<< HEAD
        # ìë£Œêµ¬ì¡°ì— ì €ì¥
        self.trainedTree[lecture] = list[str]();
        self.trainingTree[lecture] = list[str]();
        self.modelLib[lecture] = None;
        self.imageData[lecture] = dict[str, str];
        self.uploadingCount[lecture] = 0;
        
        # lecture_info.json ìƒì„±
        lectureData = {
            "modelName": None,
            "trainedList" : [],
            "imageData" : {}
=======
        # ÀÚ·á±¸Á¶¿¡ ÀúÀå
        self.trainedTree[lecture] = list[str]();
        self.trainingTree[lecture] = list[str]();
        self.modelLib[lecture] = None;
        
        # lecture_info.json »ı¼º
        lectureData = {
            "modelName": None,
            "trainedList" : []
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
        }
        
        with open(rf"{lecPath}\lecture_info.json", "w") as json_file:
            json.dump(lectureData, json_file)
            
<<<<<<< HEAD
        printSucceed(f"ì„±ê³µì ìœ¼ë¡œ '{lecture}'ë¥¼ ìƒì„±í•˜ëŠ”ë° ì„±ê³µí–ˆìŠµë‹ˆë‹¤.")
        return True;
    
    # ê¸°ì¡´ ê°•ì¢Œë¥¼ ì‚­ì œí•©ë‹ˆë‹¤.
=======
        printSucceed(f"¼º°øÀûÀ¸·Î '{lecture}'¸¦ »ı¼ºÇÏ´Âµ¥ ¼º°øÇß½À´Ï´Ù.")
        return True;
    
    # ±âÁ¸ °­ÁÂ¸¦ »èÁ¦ÇÕ´Ï´Ù.
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
    def LecturesDelete(self, lecture : str) :
        
        lecPath = self.__lectureToPath__(lecture=lecture)
        if not os.path.exists(lecPath):
<<<<<<< HEAD
            printError(f"ì¡´ì¬í•˜ì§€ ì•ŠëŠ” ê³¼ëª© '{lecPath}'ì„ ì‚­ì œí•˜ë ¤ê³  ì‹œë„í•˜ê³  ìˆìŠµë‹ˆë‹¤.")
            return False
            
        # ë””ë ‰í† ë¦¬ ì‚­ì œ(ë‚´ë¶€ì˜ íŒŒì¼ê¹Œì§€ ëª¨ë‘ ì‚­ì œí•¨)
=======
            printError(f"Á¸ÀçÇÏÁö ¾Ê´Â °ú¸ñ '{lecPath}'À» »èÁ¦ÇÏ·Á°í ½ÃµµÇÏ°í ÀÖ½À´Ï´Ù.")
            return False
            
        # µğ·ºÅä¸® »èÁ¦(³»ºÎÀÇ ÆÄÀÏ±îÁö ¸ğµÎ »èÁ¦ÇÔ)
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
        shutil.rmtree(lecPath)
        
        del self.trainingTree[lecture]
        del self.trainedTree[lecture]
        del self.modelLib[lecture]
<<<<<<< HEAD
        printSucceed(f"ì„±ê³µì ìœ¼ë¡œ '{lecture}'ë¥¼ ì‚­ì œí•˜ëŠ”ë° ì„±ê³µí–ˆìŠµë‹ˆë‹¤.")
        
        return True

    # ê°•ì˜ë“¤ ë¡œë“œ
    def LecturesLoad(self) : 
        try :
            # ì €ì¥ìë£Œ ì´ˆê¸°í™”
            self.trainingTree : dict[str,  list[str]] = {}
            self.trainedTree : dict[str,  list[str]] = {}
            self.modelLib : dict[str,  str] = {}
            self.imageData :dict[str, dict[str, str]] = {};
            self.uploadingCount : dict[str, int] = {};
        
            # ëª¨ë“  ê³¼ëª© ë””ë ‰í† ë¦¬ì— ì ‘ê·¼
=======
        printSucceed(f"¼º°øÀûÀ¸·Î '{lecture}'¸¦ »èÁ¦ÇÏ´Âµ¥ ¼º°øÇß½À´Ï´Ù.")
        
        return True

    # °­ÀÇµé ·Îµå
    def LecturesLoad(self) : 
        try :
            # ÀúÀåÀÚ·á ÃÊ±âÈ­
            self.trainingTree : dict[str,  list[str]] = {}
            self.trainedTree : dict[str,  list[str]] = {}
            self.modelLib : dict[str,  str] = {}
        
            # ¸ğµç °ú¸ñ µğ·ºÅä¸®¿¡ Á¢±Ù

>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
            tPath = self.rootPath;
            directories = [item for item in os.listdir(tPath) if os.path.isdir(os.path.join(tPath, item))]

            for lecture in directories:
                full_path = os.path.join(self.rootPath, lecture)
                
<<<<<<< HEAD
                # lecture_infoë¥¼ ì½ì–´ì˜¤ê¸°
=======
                # lecture_info¸¦ ÀĞ¾î¿À±â
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
                with open(rf"{full_path}\lecture_info.json", "r") as json_file:
                    data = json.load(json_file)
                    
                    self.modelLib[lecture] = data["modelName"];
                    self.trainedTree[lecture] = data["trainedList"]
<<<<<<< HEAD
                    self.uploadingCount[lecture] = 0
                    
                    if "imageData" in data :
                        self.imageData[lecture] = data["imageData"]
                    else : 
                        self.imageData[lecture] = {}
                        
=======
                    
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
                    self.trainingTree[lecture] = list[str]()

                ttPath = full_path + "\\TRAINING_DATA";
                files = [item for item in os.listdir(ttPath) if os.path.isfile(os.path.join(ttPath, item))]                

<<<<<<< HEAD
                # lecture TRAINING_DATAë¥¼ ì½ì–´ì˜¤ê¸°
                for file_path in files:
                        
                    # MERGED_DATASETì€ ì˜ˆì™¸
                    if self.trainingTree[lecture].__contains__(file_path) : continue;
                        
                    # ì°¾ì€ íŠ¸ë ˆì´ë‹ ë°ì´í„° ê²½ë¡œë¥¼ ì €ì¥
                    self.trainingTree[lecture].append(file_path)
                            
            printSucceed(f"ê³¼ëª© ì •ë³´ ë¡œë“œì— ì„±ê³µí–ˆìŠµë‹ˆë‹¤. \ní•™ìŠµ ì˜ˆì • ìë£Œ : \n{self.trainingTree}\ní•™ìŠµ ì™„ë£Œ ìë£Œ : \n{self.trainedTree}\nëª¨ë¸ : \n{self.modelLib}")
            return True;
    
        except Exception as ex :
            printError(f"ê³¼ëª© ë¡œë“œê°€ ì‹¤íŒ¨í–ˆìŠµë‹ˆë‹¤. ìƒì„¸ ì •ë³´ : {ex}")
            input("ë” ì´ìƒì˜ ì§„í–‰ì€ ìœ„í—˜í•˜ë¯€ë¡œ, í”„ë¡œì„¸ìŠ¤ë¥¼ ì •ì§€í•©ë‹ˆë‹¤.")
=======
                # lecture TRAINING_DATA¸¦ ÀĞ¾î¿À±â
                for file_path in files:
                        
                    # MERGED_DATASETÀº ¿¹¿Ü
                    if self.trainingTree[lecture].__contains__(file_path) : continue;
                        
                    # Ã£Àº Æ®·¹ÀÌ´× µ¥ÀÌÅÍ °æ·Î¸¦ ÀúÀå
                    self.trainingTree[lecture].append(file_path)
                            
            printSucceed(f"°ú¸ñ Á¤º¸ ·Îµå¿¡ ¼º°øÇß½À´Ï´Ù. \nÇĞ½À ¿¹Á¤ ÀÚ·á : \n{self.trainingTree}\nÇĞ½À ¿Ï·á ÀÚ·á : \n{self.trainedTree}\n¸ğµ¨ : \n{self.modelLib}")
            return True;
    
        except Exception as ex :
            printError(f"°ú¸ñ ·Îµå°¡ ½ÇÆĞÇß½À´Ï´Ù. »ó¼¼ Á¤º¸ : {ex}")
            input("´õ ÀÌ»óÀÇ ÁøÇàÀº À§ÇèÇÏ¹Ç·Î, ÇÁ·Î¼¼½º¸¦ Á¤ÁöÇÕ´Ï´Ù.")
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
            exit()
            
            return False;
    
<<<<<<< HEAD
    # ê°•ì˜ë“¤ ì €ì¥
=======
    # °­ÀÇµé ÀúÀå
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
    def LecturesSave(self) : 
        tPath = self.rootPath;
        directories = [item for item in os.listdir(tPath) if os.path.isdir(os.path.join(tPath, item))]

        for lecture in directories:
            full_path = os.path.join(self.rootPath, lecture)
                    
            lectureData = {
<<<<<<< HEAD
                "modelName"   : self.modelLib[lecture],
                "trainedList" : self.trainedTree[lecture],
                "imageData"   : self.imageData[lecture]
            }
                    
            # lecture_infoë¥¼ ì½ì–´ì˜¤ê¸°
            with open(rf"{full_path}\lecture_info.json", "w") as json_file:
                json.dump(lectureData, json_file)
    
    # ê°•ì˜ë“¤ ë¦¬ìŠ¤íŠ¸
=======
                "modelName": self.modelLib[lecture],
                "trainedList" : self.trainedTree[lecture]
            }
                    
            # lecture_info¸¦ ÀĞ¾î¿À±â
            with open(rf"{full_path}\lecture_info.json", "w") as json_file:
                json.dump(lectureData, json_file)
    
    # °­ÀÇµé ¸®½ºÆ®
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
    def LecturesList(self) : 
        return list(self.modelLib.keys())


<<<<<<< HEAD
    # ëª¨ë¸ ê°’ì„ ê°€ì ¸ì˜¤ê¸°
=======
    # ¸ğµ¨ °ªÀ» °¡Á®¿À±â
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
    def GetModel(self, lecture : str) : 
        try :
            modelName : str = self.modelLib[lecture]
        except KeyError as ex :
<<<<<<< HEAD
            printWarning(f"{lecture}ê³¼ëª©ì€ ì¡´ì¬í•˜ì§€ ì•ŠìŠµë‹ˆë‹¤.")
            return "(ìœ íš¨í•˜ì§€ ì•Šì€ ê³¼ëª©)"
        
        if modelName == None or modelName == "" :
            printWarning(f"{lecture}ì€ íŒŒì¸íŠœë‹ ëª¨ë¸ì´ ì¡´ì¬í•˜ì§€ ì•ŠìŠµë‹ˆë‹¤. ë‹¤ì‹œ í•œë²ˆ í™•ì¸í•´ì£¼ì‹­ì‹œì˜¤.")
            return "gpt-3.5-turbo-1106"
        
        printSucceed(f"{lecture}ì˜ íŒŒì¸íŠœë‹ ëª¨ë¸({modelName})ì„ ì°¾ì•˜ìŠµë‹ˆë‹¤.")
        return modelName


    # íŒŒì¸íŠœë‹ ê´€ë¦¬ ìŠ¤ë ˆë“œ ì‹œì‘
=======
            printWarning(f"{lecture}°ú¸ñÀº Á¸ÀçÇÏÁö ¾Ê½À´Ï´Ù.")
            return "(À¯È¿ÇÏÁö ¾ÊÀº °ú¸ñ)"
        
        if modelName == None or modelName == "" :
            printWarning(f"{lecture}Àº ÆÄÀÎÆ©´× ¸ğµ¨ÀÌ Á¸ÀçÇÏÁö ¾Ê½À´Ï´Ù. ´Ù½Ã ÇÑ¹ø È®ÀÎÇØÁÖ½Ê½Ã¿À.")
            return "gpt-3.5-turbo-1106"
        
        printSucceed(f"{lecture}ÀÇ ÆÄÀÎÆ©´× ¸ğµ¨({modelName})À» Ã£¾Ò½À´Ï´Ù.")
        return modelName


    # ÆÄÀÎÆ©´× °ü¸® ½º·¹µå ½ÃÀÛ
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
    def StartFineTuneChecker(self) :
        thread_unit = threading.Thread(target=self.__threadFineTuneChecker__, args=[30.]);
        thread_unit.start()
    
<<<<<<< HEAD
    # íŒŒì¸íŠœë‹ ê´€ë¦¬ ìŠ¤ë ˆíŠ¸
=======
    # ÆÄÀÎÆ©´× °ü¸® ½º·¹Æ®
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
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
<<<<<<< HEAD
        msg = f"<íŒŒì¸íŠœë‹ ëª¨ë¸ ì‘ì—… ëª©ë¡ : {len(ftJobs)}ê°œ>\n"
=======
        msg = f"<ÆÄÀÎÆ©´× ¸ğµ¨ ÀÛ¾÷ ¸ñ·Ï : {len(ftJobs)}°³>\n"
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
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
                
<<<<<<< HEAD
        msg += f"<í•™ìŠµ íŒŒì¼ ëª©ë¡ : {len(ftFiles)}ê°œ>\n"        
=======
        msg += f"<ÇĞ½À ÆÄÀÏ ¸ñ·Ï : {len(ftFiles)}°³>\n"        
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
        for file in ftFiles :
            startTime = datetime.fromtimestamp(file.created_at)
                        
            timeFormat = "%Y-%m-%d %H:%M:%S" 
                        
            if (file.status in ["uploaded"]) :
                msg += f"[ UPLOAD] [{startTime.strftime(timeFormat)}] [{file.id}] FileName : {file.filename}({file.bytes}) \n"
                            
            elif (job.status in ["error"]) :
                msg += f"[FAILURE] [{startTime.strftime(timeFormat)}] [{file.id}] FileName : {file.filename}({file.bytes}) \n"
                            
            else :
                msg += f"[DEFAULT] [{startTime.strftime(timeFormat)}] [{file.id}] FileName : {file.filename}({file.bytes}) \n"
                            
<<<<<<< HEAD
        msg += "<ëª©ë¡ ë>\n"
        print(msg)


    # íŒŒì¸íŠœë‹ ì‹œì‘
    def StartFineTuneJob(self, lectureName : str) :

        try :
            if self.finetuneSteady[lectureName] == True:
                    printError(f"'{lectureName}' ê³¼ëª©ì˜ ì´ë¯¸ ì§„í–‰ì¤‘ì¸ íŒŒì¸íŠœë‹ ìŠ¤ë ˆë“œê°€ ìˆìŠµë‹ˆë‹¤. ìŠ¤ë ˆë“œë¥¼ ì²˜ë¶„í•©ë‹ˆë‹¤.")
                    return

            self.finetuneSteady[lectureName] = True;

            printProcess(f"'{lectureName}' ê³¼ëª©ì˜ ìê°€ í•™ìŠµì„ ì¤€ë¹„ ì¤‘ì…ë‹ˆë‹¤...")
            
            if self.__CheckFineTuneAvailable__(lectureName) == False : 
                printError(f"'{lectureName}' ê³¼ëª©ì˜ ì´ë¯¸ ì§„í–‰ì¤‘ì¸ íŒŒì¸íŠœë‹ ì‘ì—…ì´ ìˆì–´ íŒŒì¸íŠœë‹ì„ ì‹œì‘í•˜ì§€ ëª»í–ˆìŠµë‹ˆë‹¤.")
                return
            
            while self.uploadingCount(lectureName) != 0 :
                printError(f"'{lectureName}' ê³¼ëª©ì— ì•„ì§ ì§„í–‰ ì¤‘ì¸ ì—…ë¡œë“œ ì‘ì—…ì´ ìˆì–´ íŒŒì¸íŠœë‹ì„ ì‹œì‘í•˜ì§€ ëª»í–ˆìŠµë‹ˆë‹¤. 10ì´ˆ í›„ ì¬ì‹œë„í•©ë‹ˆë‹¤...")
                sleep(10);


            # ë¯¸ì²˜ ëë‚˜ì§€ ì•Šì€ ë°ì´í„°ì…‹ ì •ì œì‘ì—…ì„ ë§ˆì¹œë‹¤.
            self.__MakeDataSetWhole__(lectureName);

            # ë¨¸ì§€ë°ì´í„° ìƒì„± 
            self.__MergeDataSet__(lectureName)
        
            # ë¨¸ì§€ë°ì´í„° ì—…ë¡œë“œ
            fo : FileObject = self.pm.api.UploadFile(lectureName)
                
            # íŒŒì¸íŠœë‹ ì‹œì‘
            ftj : FineTuningJob = openai.fine_tuning.jobs.create(model = "gpt-3.5-turbo-1106", training_file = fo.id)
        
            # íŒŒì¸íŠœë‹ ì‘ì—… ì¶”ì  ìŠ¤ë ˆë“œ ìƒì„±
            thread_unit : threading.Thread = threading.Thread(target = self.__threadFineTuneJob__, args = (lectureName, ftj,  self.__FineTuneJobCallback__))
            thread_unit.start()
            printProcess(f"'{lectureName}' ê³¼ëª©ì˜ ìê°€ í•™ìŠµì„ ì‹œì‘í•©ë‹ˆë‹¤.")
        
            # íŒŒì¸íŠœë‹ ì‘ì—… ì„¸ì´ë¸Œí¬ì¸íŠ¸ ìƒì„±
            self.__MakeFineTuneCheckPoint__(lecture=lectureName, ft= ftj)
            
            return True
        
        except :
            return False
        
        finally :
            self.finetuneSteady[lectureName] = False;
        
    # íŒŒì¸íŠœë‹ ìŠ¤ë ˆë“œ
    def __threadFineTuneJob__(self, lectureName : str, ftJobData : FineTuningJob,  callback) : 
        
        printProcess(f"'{lectureName}' ê³¼ëª©ì˜ íŒŒì¸íŠœë‹ ìŠ¤ë ˆë“œê°€ ìƒì„±ëìŠµë‹ˆë‹¤.")
        
        ft : FineTuningJob
        
        from _240102_OpenAI_API._240102_OpenAI_API.AiProcessSources.ProcessManager import p1, p2
        while True :
            try :
                
                # íŒŒì¸íŠœë‹ ê³¼ì • ì¤‘ ì •ë³´ë¥¼ ê°€ì ¸ì˜¨ë‹¤.
                ft = openai.fine_tuning.jobs.retrieve(ftJobData.id)
            
                #ì‹œì‘ ì‹œê°„, ê²½ê³¼ëœ ì´ˆë¥¼ ì–»ëŠ”ë‹¤.
=======
        msg += "<¸ñ·Ï ³¡>\n"
        print(msg)


    # ÆÄÀÎÆ©´× ½ÃÀÛ
    def StartFineTuneJob(self, lectureName : str) :
        try :
            printProcess(f"'{lectureName}' °ú¸ñÀÇ ÀÚ°¡ ÇĞ½ÀÀ» ÁØºñ ÁßÀÔ´Ï´Ù...")
        
            #¸ÓÁöµ¥ÀÌÅÍ »ı¼º 
            self.__MergeDataSet__("C# ÇÁ·Î±×·¡¹Ö")
        
            #¸ÓÁöµ¥ÀÌÅÍ ¾÷·Îµå
            fo : FileObject = self.pm.api.UploadFile("C# ÇÁ·Î±×·¡¹Ö")
         
            #ÆÄÀÎÆ©´× ½ÃÀÛ
            ftj : FineTuningJob = openai.fine_tuning.jobs.create(model = "gpt-3.5-turbo-1106", training_file = fo.id)
        
            # Äİ¹é Á¤ÀÇ
       
        
            #ÆÄÀÎÆ©´× ÀÛ¾÷ ÃßÀû ½º·¹µå »ı¼º
            thread_unit : threading.Thread = threading.Thread(target = self.__threadFineTuneJob__, args = (lectureName, ftj,  self.__FineTuneJobCallback__))
            thread_unit.start()
            printProcess(f"'{lectureName}' °ú¸ñÀÇ ÀÚ°¡ ÇĞ½ÀÀ» ½ÃÀÛÇÕ´Ï´Ù.")
        

            # ÆÄÀÎÆ©´× ÀÛ¾÷ ¼¼ÀÌºêÆ÷ÀÎÆ® »ı¼º
            self.__MakeFineTuneCheckPoint__(lecture=lectureName, ft= ftj)
            
            return True
        except :
            return False
        
    # ÆÄÀÎÆ©´× ½º·¹µå
    def __threadFineTuneJob__(self, lectureName : str, ftJobData : FineTuningJob,  callback) : 
        
        ft : FineTuningJob
        
        while True :
            from _240102_OpenAI_API._240102_OpenAI_API.AiProcessSources.ProcessManager import p1, p2
            try :
                printProcess(f"'{lectureName}' °ú¸ñÀÇ ÀÚ°¡ ÇĞ½ÀÀÌ ÁøÇà ÁßÀÔ´Ï´Ù.")
            
                # ÆÄÀÎÆ©´× °úÁ¤ Áß Á¤º¸¸¦ °¡Á®¿Â´Ù.
                ft = openai.fine_tuning.jobs.retrieve(ftJobData.id)
            
                #½ÃÀÛ ½Ã°£, °æ°úµÈ ÃÊ¸¦ ¾ò´Â´Ù.
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
                startTime = datetime.fromtimestamp(ft.created_at)
                pastTick = int(time.time()) - ft.created_at
                jobStatus = ft.status       

<<<<<<< HEAD
                printProcess(f"ìê°€í•™ìŠµ ì“°ë ˆë“œ - ê³¼ëª© ëª… : {lectureName}\t ì‹œì‘ ì‹œê°„ : {startTime}\t ê²½ê³¼ ì‹œê°„ : {pastTick}ì´ˆ\t ì§„í–‰ ìƒíƒœ : {jobStatus}")
                
                #í•´ì¹˜ì› ë‚˜?
                if(jobStatus in ["succeeded"]) :
                    printSucceed(f"ì„±ê³µì ìœ¼ë¡œ ìê°€í•™ìŠµì´ ì™„ë£Œë˜ì—ˆìŠµë‹ˆë‹¤. ì™„ì„±ëœ AIì˜ ëª¨ë¸ í‚¤ : {ft.fine_tuned_model}")
                    printSucceed(f"ê³¼ëª© ëª… : {lectureName}\t ì‹œì‘ ì‹œê°„ : {startTime}\t ê²½ê³¼ ì‹œê°„ : {ft.finished_at - ft.created_at}ì´ˆ\t ì¢…ë£Œ ì‹œê°„ : {datetime.fromtimestamp(ft.finished_at)}")
                    callback(lectureName, ft.fine_tuned_model)
                    break
                
                #ë§í–ˆë‚˜?
                elif (jobStatus in ["failed", "cancelled"]) :
                    printError(f"ìê°€í•™ìŠµì— ì‹¤íŒ¨í–ˆìŠµë‹ˆë‹¤! state : {jobStatus}")
                    printError(f"ê³¼ëª© ëª… : {lectureName}\t ì‹œì‘ ì‹œê°„ : {startTime}\t ê²½ê³¼ ì‹œê°„ : {pastTick}ì´ˆ\t ì¢…ë£Œ ì‹œê°„ : {pastTick}")
                    
                    #ì¹˜ëª…ì ì¸ ì˜¤ë¥˜ì— ëŒ€í•œ ì²˜ë¦¬
=======
                printProcess(f"ÀÚ°¡ÇĞ½À ¾²·¹µå - °ú¸ñ ¸í : {lectureName}\t ½ÃÀÛ ½Ã°£ : {startTime}\t °æ°ú ½Ã°£ : {pastTick}ÃÊ\t ÁøÇà »óÅÂ : {jobStatus}")
                
                #ÇØÄ¡¿ü³ª?
                if(jobStatus in ["succeeded"]) :
                    printSucceed(f"¼º°øÀûÀ¸·Î ÀÚ°¡ÇĞ½ÀÀÌ ¿Ï·áµÇ¾ú½À´Ï´Ù. ¿Ï¼ºµÈ AIÀÇ ¸ğµ¨ Å° : {ft.fine_tuned_model}")
                    printSucceed(f"°ú¸ñ ¸í : {lectureName}\t ½ÃÀÛ ½Ã°£ : {startTime}\t °æ°ú ½Ã°£ : {ft.finished_at - ft.created_at}ÃÊ\t Á¾·á ½Ã°£ : {datetime.fromtimestamp(ft.finished_at)}")
                    callback(lectureName, ft.fine_tuned_model)
                    break
                
                #¸ÁÇß³ª?
                elif (jobStatus in ["failed", "cancelled"]) :
                    printError(f"ÀÚ°¡ÇĞ½À¿¡ ½ÇÆĞÇß½À´Ï´Ù! state : {jobStatus}")
                    printError(f"°ú¸ñ ¸í : {lectureName}\t ½ÃÀÛ ½Ã°£ : {startTime}\t °æ°ú ½Ã°£ : {pastTick}ÃÊ\t Á¾·á ½Ã°£ : {pastTick}")
                    
                    #Ä¡¸íÀûÀÎ ¿À·ù¿¡ ´ëÇÑ Ã³¸®
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
                    self.pm.client.Send(f"FineTuneEnd{p1}{str(False)}{p2}{lectureName}")
                    return
                
            except Exception as e: 
<<<<<<< HEAD
                printError(f"__threadFineTuneJob__ ì—ëŸ¬ : {e}\n{e.with_traceback.format_exc()}")
                
                #ì¹˜ëª…ì ì¸ ì˜¤ë¥˜ì— ëŒ€í•œ ì²˜ë¦¬
                self.pm.client.Send(f"FineTuneEnd{p1}{str(False)}{p2}{lectureName}")
                return 
              
            #ì•„ë‹ˆì•¼? ê·¸ëŸ¼ ë°˜ë³µ  
            sleep(10.)
        
        # ê²°ê³¼ ë°˜í™˜
        callback(lectureName, ft.fine_tuned_model)
    
    # íŒŒì¸íŠœë‹ ìŠ¤ë ˆë“œ ì½œë°±
    def __FineTuneJobCallback__ (self, lectureName, modelName) : 
        from _240102_OpenAI_API._240102_OpenAI_API.AiProcessSources.ProcessManager import p1, p2
        try :
            # ì´ë¯¸ ê°™ì€ ê°’ì´ ìˆì„ ì‹œ ìŠ¤í‚µ.
            if(self.modelLib[lectureName] == modelName) : return;
        
            # ê¸°ì¡´ ëª¨ë¸ì€ ì‚­ì œ
            printProcess(f"{lectureName}ì˜ ëª¨ë¸ì„ {modelName}ë¡œ êµì²´í•©ë‹ˆë‹¤.")
            if(self.modelLib[lectureName] != None) :
                printProcess(f"ê¸°ì¡´ ëª¨ë¸ {self.modelLib[lectureName]}ì„ ì œê±°í•©ë‹ˆë‹¤...")
                self.pm.api.DeleteFineTuneModel(self.modelLib[lectureName])
                
            #ìƒˆë¡œìš´ ëª¨ë¸ ë³µë¶™
            printProcess(f"ìƒˆë¡œìš´ ëª¨ë¸ {modelName}ì„ ë°°ì¹˜í•©ë‹ˆë‹¤.")
=======
                printError(f"__threadFineTuneJob__ ¿¡·¯ : {e}\n{e.with_traceback.format_exc()}")
                
                #Ä¡¸íÀûÀÎ ¿À·ù¿¡ ´ëÇÑ Ã³¸®
                self.pm.client.Send(f"FineTuneEnd{p1}{str(False)}{p2}{lectureName}")
                return 
              
            #¾Æ´Ï¾ß? ±×·³ ¹İº¹  
            sleep(10.)
        
        # °á°ú ¹İÈ¯
        callback(ft.fine_tuned_model, lectureName)
    
    # ÆÄÀÎÆ©´× ½º·¹µå Äİ¹é
    def __FineTuneJobCallback__ (self, lectureName, modelName) : 
        from _240102_OpenAI_API._240102_OpenAI_API.AiProcessSources.ProcessManager import p1, p2
        try :
            # ÀÌ¹Ì °°Àº °ªÀÌ ÀÖÀ» ½Ã ½ºÅµ.
            if(self.modelLib[lectureName] == modelName) : return;
        
            # ±âÁ¸ ¸ğµ¨Àº »èÁ¦
            printProcess(f"{lectureName}ÀÇ ¸ğµ¨À» {modelName}·Î ±³Ã¼ÇÕ´Ï´Ù.")
            if(self.modelLib[lectureName] != None) :
                printProcess(f"±âÁ¸ ¸ğµ¨ {self.modelLib[lectureName]}À» Á¦°ÅÇÕ´Ï´Ù...")
                self.pm.api.DeleteFineTuneModel(self.modelLib[lectureName])
                
            #»õ·Î¿î ¸ğµ¨ º¹ºÙ
            printProcess(f"»õ·Î¿î ¸ğµ¨ {modelName}À» ¹èÄ¡ÇÕ´Ï´Ù.")
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
            self.modelLib[lectureName] = modelName
            self.trainedTree[lectureName] = self.trainingTree[lectureName]
            
            self.LecturesSave()
        
<<<<<<< HEAD
            # ëë‚¬ìœ¼ë‹ˆ ì •ìƒì ì¸ ì¢…ë£Œ ë°˜ì‘ ë³´ì´ê¸°
            self.pm.client.Send(f"FineTuneEnd{p1}{str(True)}{p2}{lectureName}")
            
        except Exception as ex:
            # ë¹„ì •ìƒì ì¸ ì¢…ë£Œì— ëŒ€í•´ ë°˜ì‘ ë³´ì´ê¸°
            printError(f"íŒŒì¸íŠœë‹ ì½œë°±ì—ì„œ ì˜¤ë¥˜ ë°œìƒ : {ex}\n{ex.with_traceback.format_exc()}")
            self.pm.client.Send(f"FineTuneEnd{p1}{str(False)}{p2}{lectureName}")


    # ë¡œìš° ë°ì´í„°ë¥¼ íŒ¨ì“°ë¥¼ í†µí•´ ë³µì‚¬í•´ ì˜µë‹ˆë‹¤. txt > txt
    def AddRawData(self, lecture : str, txtFilePath : str) : 
        self.uploadingCount[lecture] += 1;

        try:
            # í…ìŠ¤íŠ¸ íŒŒì¼ì˜ ë‚´ìš© ì½ì–´ì˜¤ê¸°
            with open(txtFilePath, "r", encoding ="utf-8") as source_file:
                file_content = source_file.read()

            # ìƒˆë¡œìš´ ë””ë ‰í† ë¦¬ì— í…ìŠ¤íŠ¸ íŒŒì¼ ìƒì„±í•˜ê³  ë‚´ìš© ë³µì‚¬
=======
            # ³¡³µÀ¸´Ï Á¤»óÀûÀÎ Á¾·á ¹İÀÀ º¸ÀÌ±â
            self.pm.client.Send(f"FineTuneEnd{p1}{str(True)}{p2}{lectureName}")
            
        except Exception as ex:
            # ºñÁ¤»óÀûÀÎ Á¾·á¿¡ ´ëÇØ ¹İÀÀ º¸ÀÌ±â
            printError(f"ÆÄÀÎÆ©´× Äİ¹é¿¡¼­ ¿À·ù ¹ß»ı : {ex}\n{ex.with_traceback.format_exc()}")
            self.pm.client.Send(f"FineTuneEnd{p1}{str(False)}{p2}{lectureName}")


    # ·Î¿ì µ¥ÀÌÅÍ¸¦ ÆĞ¾²¸¦ ÅëÇØ º¹»çÇØ ¿É´Ï´Ù. txt > txt
    def AddRawData(self, lecture : str, txtFilePath : str) : 
        try:
            # ÅØ½ºÆ® ÆÄÀÏÀÇ ³»¿ë ÀĞ¾î¿À±â
            with open(txtFilePath, "r", encoding ="utf-8") as source_file:
                file_content = source_file.read()

            # »õ·Î¿î µğ·ºÅä¸®¿¡ ÅØ½ºÆ® ÆÄÀÏ »ı¼ºÇÏ°í ³»¿ë º¹»ç
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
            file_name = os.path.basename(txtFilePath)
            destination_path = rf"{self.__lectureToPath__(lecture)}\RAW_DATA\{file_name}"

            with open(destination_path, "w", encoding ="utf-8") as destination_file:
                destination_file.write(file_content)
            
            if not self.trainingTree[lecture].__contains__(file_name) :
                self.trainingTree[lecture].append(file_name);
            self.LecturesSave();
            
<<<<<<< HEAD
            printSucceed(f"ë¡œìš° ë°ì´í„°ë¥¼ ì¶”ê°€ ì™„ë£Œ: {destination_path}")
            return True;
    
        except FileNotFoundError:
            printError(f"ë¡œìš° ë°ì´í„°ë¥¼ ì¶”ê°€í•˜ì§€ ëª»Â™ìŠµë‹ˆë‹¤. í•´ë‹¹ íŒŒì¼ì„ ì°¾ì„ ìˆ˜ ì—†ìŠµë‹ˆë‹¤. {txtFilePath}")
            return False;
        
        except Exception as e:
            printError(f"ë¡œìš° ë°ì´í„° ì¶”ê°€ ì¤‘, ì˜¤ë¥˜ ë°œìƒ: <{txtFilePath}> {e}")
            return False;
        finally :
            self.uploadingCount[lecture] -= 1;

    # pdf > txt
    def AddPdfData(self, lecture : str, pdfFilePath : str) : 
        self.uploadingCount[lecture] += 1;

        try:
            
            # ìƒˆë¡œìš´ ë””ë ‰í† ë¦¬ì— í…ìŠ¤íŠ¸ íŒŒì¼ ìƒì„±í•˜ê³  ë‚´ìš© ë³µì‚¬
=======
            printSucceed(f"·Î¿ì µ¥ÀÌÅÍ¸¦ Ãß°¡ ¿Ï·á: {destination_path}")
            return True;
    
        except FileNotFoundError:
            printError(f"·Î¿ì µ¥ÀÌÅÍ¸¦ Ãß°¡ÇÏÁö ¸øÁ™½À´Ï´Ù. ÇØ´ç ÆÄÀÏÀ» Ã£À» ¼ö ¾ø½À´Ï´Ù. {txtFilePath}")
            return False;
        
        except Exception as e:
            printError(f"·Î¿ì µ¥ÀÌÅÍ Ãß°¡ Áß, ¿À·ù ¹ß»ı: <{txtFilePath}> {e}")
            return False;

    # pdf > txt
    def AddPdfData(self, lecture : str, pdfFilePath : str) : 
        try:
            
            # »õ·Î¿î µğ·ºÅä¸®¿¡ ÅØ½ºÆ® ÆÄÀÏ »ı¼ºÇÏ°í ³»¿ë º¹»ç
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
            file_name = os.path.basename(pdfFilePath).replace('.pdf','')
            destination_path = rf"{self.__lectureToPath__(lecture)}\RAW_DATA\{file_name}.txt"

            pdfCon = Pdf2TextConverter();
            pdfCon.convert(pdfFilePath, destination_path)
            
            if not self.trainingTree[lecture].__contains__(file_name) :
                self.trainingTree[lecture].append(file_name);
            self.LecturesSave();
            
<<<<<<< HEAD
            printSucceed(f"ë¡œìš° ë°ì´í„°ë¥¼ ì¶”ê°€ ì™„ë£Œ: {destination_path}")
            return True;
    
        except FileNotFoundError:
            printError(f"ë¡œìš° ë°ì´í„°ë¥¼ ì¶”ê°€í•˜ì§€ ëª»í–ˆìŠµë‹ˆë‹¤. í•´ë‹¹ íŒŒì¼ì„ ì°¾ì„ ìˆ˜ ì—†ìŠµë‹ˆë‹¤. {pdfFilePath}")
            return False;
        
        except Exception as e:
            printError(f"ë¡œìš° ë°ì´í„° ì¶”ê°€ ì¤‘, ì˜¤ë¥˜ ë°œìƒ: {pdfFilePath} - {e}")
            return False;
        finally :
            self.uploadingCount[lecture] -= 1;
        
    # wav > txt
    def AddWavData(self, lecture : str, wavFilePath : str) : 
        self.uploadingCount[lecture] += 1;

        try:
            # ìƒˆë¡œìš´ ë””ë ‰í† ë¦¬ì— í…ìŠ¤íŠ¸ íŒŒì¼ ìƒì„±í•˜ê³  ë‚´ìš© ë³µì‚¬
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
            
            printSucceed(f"ë¡œìš° ë°ì´í„°ë¥¼ ì¶”ê°€ ì™„ë£Œ: {destination_path}")
            return True;
    
        except FileNotFoundError:
            printError(f"ë¡œìš° ë°ì´í„°ë¥¼ ì¶”ê°€í•˜ì§€ ëª»í—€ìŠµë‹ˆë‹¤. í•´ë‹¹ íŒŒì¼ì„ ì°¾ì„ ìˆ˜ ì—†ìŠµë‹ˆë‹¤. {wavFilePath}")
            return False;
        
        except Exception as e:
            printError(f"ë¡œìš° ë°ì´í„° ì¶”ê°€ ì¤‘, ì˜¤ë¥˜ ë°œìƒ: {wavFilePath} - {e}")
            return False;
        finally :
            self.uploadingCount[lecture] -= 1;
  
    # ppt > root, txt
    def AddPptData(self, lecture : str, pptFilePath : str) :
        self.uploadingCount[lecture] += 1;
        import Addon.PptImageConverter as pptImage;
        import Addon.PptTextConverter as pptText;
        
        rawDic : dict[str, str] = {}
        
        tDir = self.__lectureToPath__(lecture) + r"\Image";
        if not os.path.exists(tDir):
            try:
                os.makedirs(tDir)
                print(f"ë””ë ‰í† ë¦¬ '{tDir}'ë¥¼ ìƒì„±í–ˆìŠµë‹ˆë‹¤.")
            except OSError as e:
                print(f"ë””ë ‰í† ë¦¬ ìƒì„± ì‹¤íŒ¨: {e}")

        imgList = pptImage.PptToImage(pptFilePath, tDir);
        descList = pptText.PptToText(pptFilePath);
        
        for i in range(len(imgList)):
            rawDic.update({ imgList[i] : descList[i] })

        retDic : dict[str, str] = self.pm.api.InitPptLabeling(lecture, rawDic);
        
        for pair in retDic.items():
            key = pair[0];
            value = pair[1];
            self.imageData[lecture].update({key : value})
        
        self.LecturesSave();
        
        self.uploadingCount[lecture] -= 1;
        
    # ê³¼ëª©ì„ ì£¼ì œë¡œ ì§ˆë¬¸ê³¼ ê°€ì¥ ìœ ì‚¬í•œ ì´ë¯¸ì§€ ì„¤ëª…ì— í•´ë‹¹í•˜ëŠ” ì´ë¯¸ì§€ë¥¼ ë°˜í™˜
    def FindSimilarity(self, lecture : str, question : str) :
        import Addon.SentenceSimiralityChecker as similarity      

        ret : str = None;
        nowValue  = 999;
        
        printProcess(rf"{len(self.imageData[lecture].items())}ê°œì˜ ì´ë¯¸ì§€ ì¤‘ ìœ ì‚¬ë„ ë†’ì€ ì´ë¯¸ì§€ë¥¼ ì°¾ìŠµë‹ˆë‹¤...")
        
        for pair in self.imageData[lecture].items() :
            imgRoot = pair[0]
            description = pair[1]
            
            simValue = similarity.CheckSimilarity(question, description);
            
            if (nowValue > simValue) :
                nowValue = simValue;
                ret = imgRoot;
    
        if ret != None :
            printError(rf"ì í•©í•œ ì´ë¯¸ì§€ë¥¼ ì°¾ì•˜ìŠµë‹ˆë‹¤! ìœ ì‚¬ë„ : {nowValue} / ê²½ë¡œ : {ret}")
        else : 
            printError(rf"ìœ ì‚¬ë„ ë†’ì€ ì´ë¯¸ì§€ë¥¼ ì°¾ì§€ ëª» í–ˆìŠµë‹ˆë‹¤...")
            
        return ret;
            
    # ê°€ì ¸ì˜¨ ë¡œìš° ë°ì´í„°ë¡œ GPT ë¥¼ ì‚¬ìš©í•´ í•™ìŠµ ë°ì´í„°ë¡œ ë§Œë“­ë‹ˆë‹¤. txt > json
    def __MakeDataSet__(self, lecture : str, txtFilePath : str) : 
        
        printProcess(f"ë¡œìš° ë°ì´í„°ì—ì„œ GPTë¥¼ ì´ìš©í•´ í•™ìŠµ ë°ì´í„°ë¥¼ ì¶”ì¶œí•©ë‹ˆë‹¤...  ëŒ€ìƒ íŒŒì¼ : {txtFilePath}...")
        
        api = self.pm.api;
        #í•™ìŠµ ë‚´ìš© ì¶”ì¶œ
        dataSet : list = api.InitDataSet(lecture, txtFilePath);
        
        # ì €ì¥í•  í…ìŠ¤íŠ¸ jsonl
        txtFileName = os.path.basename(txtFilePath).replace(".txt", "")
        dataSetPath : str = fr"{self.__lectureToPath__(lecture)}\TRAINING_DATA\{txtFileName}.jsonl"
        
        printSucceed(f"ë¡œìš° ë°ì´í„°ì—ì„œ GPTë¥¼ ì´ìš©í•´ í•™ìŠµ ë°ì´í„°ë¥¼ ì¶”ì¶œí•˜ëŠ”ë° ì„±ê³µí–ˆìŠµë‹ˆë‹¤ ëŒ€ìƒ íŒŒì¼ : {dataSetPath}...")
=======
            printSucceed(f"·Î¿ì µ¥ÀÌÅÍ¸¦ Ãß°¡ ¿Ï·á: {destination_path}")
            return True;
    
        except FileNotFoundError:
            printError(f"·Î¿ì µ¥ÀÌÅÍ¸¦ Ãß°¡ÇÏÁö ¸øÁ™½À´Ï´Ù. ÇØ´ç ÆÄÀÏÀ» Ã£À» ¼ö ¾ø½À´Ï´Ù. {pdfFilePath}")
            return False;
        
        except Exception as e:
            printError(f"·Î¿ì µ¥ÀÌÅÍ Ãß°¡ Áß, ¿À·ù ¹ß»ı: {pdfFilePath} - {e}")
            return False;
        
  
         
    # °¡Á®¿Â ·Î¿ì µ¥ÀÌÅÍ·Î GPT ¸¦ »ç¿ëÇØ ÇĞ½À µ¥ÀÌÅÍ·Î ¸¸µì´Ï´Ù. txt > json
    def __MakeDataSet__(self, lecture : str, txtFilePath : str) : 
        
        printProcess(f"·Î¿ì µ¥ÀÌÅÍ¿¡¼­ GPT¸¦ ÀÌ¿ëÇØ ÇĞ½À µ¥ÀÌÅÍ¸¦ ÃßÃâÇÕ´Ï´Ù...  ´ë»ó ÆÄÀÏ : {txtFilePath}...")
        
        api = self.pm.api;
        #ÇĞ½À ³»¿ë ÃßÃâ
        dataSet : list = api.InitDataSet(lecture, txtFilePath);
        
        # ÀúÀåÇÒ ÅØ½ºÆ® jsonl
        txtFileName = os.path.basename(txtFilePath).replace(".txt", "")
        dataSetPath : str = fr"{self.__lectureToPath__(lecture)}\TRAINING_DATA\{txtFileName}.jsonl"
        
        printSucceed(f"·Î¿ì µ¥ÀÌÅÍ¿¡¼­ GPT¸¦ ÀÌ¿ëÇØ ÇĞ½À µ¥ÀÌÅÍ¸¦ ÃßÃâÇÏ´Âµ¥ ¼º°øÇß½À´Ï´Ù ´ë»ó ÆÄÀÏ : {dataSetPath}...")
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
        
        with open(dataSetPath, "w", encoding = "utf-8") as json_file:
            json_file.write(json.dumps(dataSet, ensure_ascii=False))
    
<<<<<<< HEAD
    # ê³¼ëª© ì•ˆì˜ ë¯¸ì²˜ ì™„ë£Œë˜ì§€ ì•Šì€ ëª¨ë“  ë¡œìš° ë°ì´í„°ë¥¼ ì •ì œí•œë‹¤.
    def __MakeDataSetWhole__(self, lecture : str) :
        printProcess("ë¯¸ì²˜ ì™„ë£Œë˜ì§€ ì•Šì€ ë¡œìš°ë°ì´í„°ë¥¼ ì°¾ìŠµë‹ˆë‹¤.")  
        
        resultList = []      
        
        try :
            lecPath = self.__lectureToPath__(lecture)
            rawPath = lecPath + r"\RAW_DATA"
            trainPath = lecPath + r"\TRAINING_DATA"
            
            rawList = []
            for filename in os.listdir(rawPath):
                if os.path.isfile(os.path.join(rawPath, filename)):
                    file_name_without_extension, _ = os.path.splitext(filename)
                    rawList.append(file_name_without_extension)
                    
            trainList = []
            for filename in os.listdir(trainPath):
                if os.path.isfile(os.path.join(trainPath, filename)):
                    file_name_without_extension, _ = os.path.splitext(filename)
                    trainList.append(file_name_without_extension)

            tempList = []
            for element in rawList:
                if element not in trainList:
                    tempList.append(element)
                    
            for fileName in tempList :
                resultList.append(f"{rawPath}\{fileName}.txt")
                
        except Exception as  ex:
            print(ex);
            

        try : 
            print("[result]" + str(resultList))
            
            for txtFile in resultList :
                self.__MakeDataSet__(lecture, txtFile)
                
        except Exception as ex :
            print(ex);

    # í•´ë‹¹ ê°•ì¢Œì˜ ëª¨ë“  ë°ì´í„°ì…‹ì„ í•˜ë‚˜ë¡œ í•©ì³ ì—…ë¡œë“œë¥¼ ì¤€ë¹„í•©ë‹ˆë‹¤. json, json... > jsonl
    def __MergeDataSet__(self, lecture : str) : 
        
        printProcess(f"'{lecture}'ê³¼ëª©ì˜ í†µí•© ë°ì´í„° ìƒì„±ì„ ì‹œì‘í•©ë‹ˆë‹¤... ")
=======
    # ÇØ´ç °­ÁÂÀÇ ¸ğµç µ¥ÀÌÅÍ¼ÂÀ» ÇÏ³ª·Î ÇÕÃÄ ¾÷·Îµå¸¦ ÁØºñÇÕ´Ï´Ù. json, json... > jsonl
    def __MergeDataSet__(self, lecture : str) : 
        
        printProcess(f"'{lecture}'°ú¸ñÀÇ ÅëÇÕ µ¥ÀÌÅÍ »ı¼ºÀ» ½ÃÀÛÇÕ´Ï´Ù... ")
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
        
        lecPath = self.__lectureToPath__(lecture);        
        trainingFileDir = rf"{lecPath}\TRAINING_DATA"

        jsonl_contents = []

<<<<<<< HEAD
        # ë””ë ‰í† ë¦¬ ë‚´ë¶€ì˜ íŒŒì¼ë“¤ ê°€ì ¸ì˜¤ê¸°
        files = [f for f in os.listdir(trainingFileDir) if os.path.isfile(os.path.join(trainingFileDir, f))]

        # JSONL íŒŒì¼ë“¤ì— ëŒ€í•´ ë°˜ë³µ
=======
        # µğ·ºÅä¸® ³»ºÎÀÇ ÆÄÀÏµé °¡Á®¿À±â
        files = [f for f in os.listdir(trainingFileDir) if os.path.isfile(os.path.join(trainingFileDir, f))]

        # JSONL ÆÄÀÏµé¿¡ ´ëÇØ ¹İº¹
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
        for file_name in files: 
            if file_name.endswith('.jsonl'):
                jsonlPath = os.path.join(trainingFileDir, file_name)
                with open(jsonlPath, 'r', encoding='utf-8') as jsonl_file:
<<<<<<< HEAD
                    # íŒŒì¼ ë‚´ìš© ì½ì–´ì˜¤ê¸°
=======
                    # ÆÄÀÏ ³»¿ë ÀĞ¾î¿À±â
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
                    file_content = jsonl_file.read()
                    dataList = json.loads(file_content)
                    jsonl_contents.extend([data for data in dataList])

        
        dataSetPath : str = fr"{self.__lectureToPath__(lecture)}\MERGED_DATASET\{lecture}_MERGED.jsonl"

        with open(dataSetPath, "w", encoding="utf-8") as json_file:
            
            for item in jsonl_contents:
                json_file.write(json.dumps(item, ensure_ascii=False) + '\n')
            
<<<<<<< HEAD
        printSucceed(f"'{lecture}'ê³¼ëª©ì˜ í†µí•© ë°ì´í„°ë¥¼ ìƒì„±í•˜ëŠ”ë°ì— ì„±ê³µí–ˆìŠµë‹ˆë‹¤. ê²½ë¡œ : {dataSetPath}")
    
    # ê³¼ëª© ì´ë¦„ìœ¼ë¡œ ë¹ ë¥¸ ê²½ë¡œ ì°¾ê¸°
=======
        printSucceed(f"'{lecture}'°ú¸ñÀÇ ÅëÇÕ µ¥ÀÌÅÍ¸¦ »ı¼ºÇÏ´Âµ¥¿¡ ¼º°øÇß½À´Ï´Ù. °æ·Î : {dataSetPath}")
    
    # °ú¸ñ ÀÌ¸§À¸·Î ºü¸¥ °æ·Î Ã£±â
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
    def __lectureToPath__(self, lecture : str) :
        filePath : str = f"{self.rootPath}\\{lecture}"
        return filePath 
    
    
<<<<<<< HEAD
    # íŒŒì¸íŠœë‹ ì¡ ì„¸ì´ë¸Œí¬ì¸íŠ¸ ìƒì„±
=======
    # ÆÄÀÎÆ©´× Àâ ¼¼ÀÌºêÆ÷ÀÎÆ® »ı¼º
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
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
            
<<<<<<< HEAD
        printSucceed(f"'{lecture}' ê³¼ëª©ì˜ ìê°€ í•™ìŠµ ì„¸ì´ë¸Œí¬ì¸íŠ¸ë¥¼ ì €ì¥í—€ìŠµë‹ˆë‹¤!")
        
    # íŒŒì¸íŠœë‹ ì¡ ì„¸ì´ë¸Œ í¬ì¸íŠ¸ ë¡œë“œ. ì í•©í•œ íŒŒì¸íŠœë‹ ì¡ì´ ìˆì„ ì‹œ, ìŠ¤ë ˆë“œ ì¬ìƒì„±
=======
        printSucceed(f"'{lecture}' °ú¸ñÀÇ ÀÚ°¡ ÇĞ½À ¼¼ÀÌºêÆ÷ÀÎÆ®¸¦ ÀúÀåÁ™½À´Ï´Ù!")
        
    # ÆÄÀÎÆ©´× Àâ ¼¼ÀÌºê Æ÷ÀÎÆ® ·Îµå. ÀûÇÕÇÑ ÆÄÀÎÆ©´× ÀâÀÌ ÀÖÀ» ½Ã, ½º·¹µå Àç»ı¼º
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
    def __LoadFineTuneCheckPoint__(self) : 
        try : 
            user_documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
            saveDirectory = "WB38"
            cpPath = f"{user_documents_path}\\{saveDirectory}\\finetune_checkpoint.json"
            
<<<<<<< HEAD
            # ì„¸ì´ë¸Œ í¬ì¸íŠ¸ ë¡œë“œ
=======
            # ¼¼ÀÌºê Æ÷ÀÎÆ® ·Îµå
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
            dataPre : list
            with open(cpPath, "r", encoding="utf-8") as jsonFile :
                dataPre = json.load(jsonFile)
        
<<<<<<< HEAD
            # APIì˜ ì§„í–‰ì¤‘ì¸ ì¡ë“¤ì„ ë¡œë“œ
=======
            # APIÀÇ ÁøÇàÁßÀÎ ÀâµéÀ» ·Îµå
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
            from ApiManager import OpenAiManagerV2 
            api : OpenAiManagerV2 = self.pm.api;
            ftData, files = api.GetFineTuneData()
            ftJobs : list[FineTuningJob] = ftData.data
    
<<<<<<< HEAD
            # ì„¸ì´ë¸Œ í¬ì¸íŠ¸ë“¤ì„ ìˆœíšŒí•˜ë©° ì§„í–‰ì¤‘ì¸ ì¡ë“¤ì„ í™•ì¸

            for data in  dataPre : # ì„¸ì´ë¸Œí¬ì¸íŠ¸ ìˆœíšŒ
            
                lecture : str = data["lecture"]
                ftId : str = data["fineTuneJob"] 
                
                for ftJob in ftJobs : # íŒŒì¸íŠœë‹ ì¡ ìˆœíšŒ
                    if(ftJob.id == ftId) :  # ì„¸ì´ë¸Œí¬ì¸íŠ¸ì™€ ì¼ì¹˜
                        if(ftJob.status in ["failed", "cancelled", "succeeded"]) : #ìœ íš¨í•˜ì§€ ì•Šì€ íŒŒì¸íŠœë‹ ì¡
                            break;
        
                        #íŒŒì¸íŠœë‹ ì‘ì—… ì¶”ì  ìŠ¤ë ˆë“œ ìƒì„±
                        thread_unit : threading.Thread = threading.Thread(target = self.__threadFineTuneJob__, args = (lecture, ftJob, self.__FineTuneJobCallback__))
                        thread_unit.start()
                        printSucceed(f"'{lecture}' ê³¼ëª©ì˜ ìê°€ í•™ìŠµ ì„¸ì´ë¸Œí¬ì¸íŠ¸ë¥¼ ë¶ˆëŸ¬ì™”ìŠµë‹ˆë‹¤!")
                        
        except FileNotFoundError as ex :
            printWarning(f" finetune_checkpoint.json íŒŒì¼ì´ ì¡´ì¬í•˜ì§€ ì•ŠìŠµë‹ˆë‹¤. ìƒˆë¡œ ìƒì„±í•©ë‹ˆë‹¤. ")
            with open(cpPath, "w", encoding="utf-8") as jsonFile :
                json.dump([], jsonFile, ensure_ascii=False)
            
        except Exception as ex : 
            printError(f"__LoadFineTuneCheckPoint__ ì‹¤í–‰ ì¤‘ ì˜¤ë¥˜ë°œìƒ. {ex}\n{ex.with_traceback.format_exc()}")
               
    # íŒŒì¸íŠœë‹ ê°€ëŠ¥í•œì§€ ì²´í¬
    def __CheckFineTuneAvailable__(self, lectureName : str) :
        try : 
            user_documents_path = os.path.join(os.path.expanduser('~'), 'Documents')
            saveDirectory = "WB38"
            cpPath = f"{user_documents_path}\\{saveDirectory}\\finetune_checkpoint.json"
            
            # ì„¸ì´ë¸Œ í¬ì¸íŠ¸ ë¡œë“œ
            cpList : list
            with open(cpPath, "r", encoding="utf-8") as jsonFile :
                cpList = json.load(jsonFile)
        
            # APIì˜ ì§„í–‰ì¤‘ì¸ ì¡ë“¤ì„ ë¡œë“œ
            from ApiManager import OpenAiManagerV2 
            api : OpenAiManagerV2 = self.pm.api;
            ftData, files = api.GetFineTuneData()
            ftJobs : list[FineTuningJob] = ftData.data
    
            # ì„¸ì´ë¸Œ í¬ì¸íŠ¸ë“¤ì„ ìˆœíšŒí•˜ë©° ì§„í–‰ì¤‘ì¸ ì¡ë“¤ì„ í™•ì¸

            for cp in  cpList : # ì„¸ì´ë¸Œí¬ì¸íŠ¸ ìˆœíšŒ
            
                cpLecture : str = cp["lecture"]
                cpId : str = cp["fineTuneJob"]
            
                for ftJob in ftJobs : # íŒŒì¸íŠœë‹ ì¡ ìˆœíšŒ
                    if(ftJob.id == cpId and lectureName == cpLecture) :  # ì„¸ì´ë¸Œí¬ì¸íŠ¸ì— ì €ì¥ëœ ê³¼ëª©ê³¼ ë‚´ ê³¼ëª©ì´ ì¼ì¹˜
                        if ftJob.status in ["validating_files", "queued", "running"] : #ì§„í–‰ì¤‘ì´ë¼ë©´ 
                            return False;
            
            return True
        
        except FileNotFoundError as ex :
            printWarning(f" finetune_checkpoint.json íŒŒì¼ì´ ì¡´ì¬í•˜ì§€ ì•ŠìŠµë‹ˆë‹¤. ìƒˆë¡œ ìƒì„±í•©ë‹ˆë‹¤. ")
            with open(cpPath, "w", encoding="utf-8") as jsonFile :
                json.dump([], jsonFile, ensure_ascii=False)
            
        except Exception as ex : 
            printError(f"__CheckFineTuneAvailable__ ì‹¤í–‰ ì¤‘ ì˜¤ë¥˜ë°œìƒ. {ex}\n{ex.with_traceback.format_exc()}")
                
=======
            # ¼¼ÀÌºê Æ÷ÀÎÆ®µéÀ» ¼øÈ¸ÇÏ¸ç ÁøÇàÁßÀÎ ÀâµéÀ» È®ÀÎ

            for data in  dataPre : # ¼¼ÀÌºêÆ÷ÀÎÆ® ¼øÈ¸
            
                lecture : str = data["lecture"]
                ftId : str = data["fineTuneJob"]
            
                for ftJob in ftJobs : # ÆÄÀÎÆ©´× Àâ ¼øÈ¸
                    if(ftJob.id == ftId) :  # ¼¼ÀÌºêÆ÷ÀÎÆ®¿Í ÀÏÄ¡
                        if(ftJob.status in ["failed", "cancelled"]) : #À¯È¿ÇÏÁö ¾ÊÀº ÆÄÀÎÆ©´× Àâ
                            printError(f"'{lecture}' °ú¸ñÀÇ ¼¼ÀÌºêÆ÷ÀÎÆ®¸¦ ºÒ·¯¿À´Âµ¥ ½ÇÆĞÇß½À´Ï´Ù. state : {ftJob.status}")
                            break;
        
                        #ÆÄÀÎÆ©´× ÀÛ¾÷ ÃßÀû ½º·¹µå »ı¼º
                        thread_unit : threading.Thread = threading.Thread(target = self.__threadFineTuneJob__, args = (lecture, ftJob, self.__FineTuneJobCallback__))
                        thread_unit.start()
                        printSucceed(f"'{lecture}' °ú¸ñÀÇ ÀÚ°¡ ÇĞ½À ¼¼ÀÌºêÆ÷ÀÎÆ®¸¦ ºÒ·¯¿Ô½À´Ï´Ù!")
            
            with open(cpPath, "w", encoding="utf-8") as jsonFile :
                json.dump([], jsonFile, ensure_ascii=False)
                
        except FileNotFoundError as ex :
            printWarning(f" finetune_checkpoint.json ÆÄÀÏÀÌ Á¸ÀçÇÏÁö ¾Ê½À´Ï´Ù. »õ·Î »ı¼ºÇÕ´Ï´Ù. ")
            with open(cpPath, "w", encoding="utf-8") as jsonFile :
                json.dump([], jsonFile, ensure_ascii=False)
            
        except Exception as ex : 
            printError(f"__LoadFineTuneCheckPoint__ ½ÇÇà Áß ¿À·ù¹ß»ı. {ex}\n{ex.with_traceback.format_exc()}")
               
>>>>>>> d94f2c40e5cb315f1f1f5786c865b0c286ea70c2
