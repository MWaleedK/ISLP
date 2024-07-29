import os

class DatasetGrabber:
    def __init__(self):
        self.basePath = os.getcwd()
        try:
            self.basePath = os.path.join(self.basePath,'Datasets')
            if not os.path.isdir(self.basePath):
                raise Exception("Base path is wrong")
        except Exception as e:
            print(e)
    
    def getDatasetFilePath(self, fileName: str):
        try:
            self.datasetPath = os.path.join(self.basePath,fileName)
            if os.path.isfile(self.datasetPath): 
                return self.datasetPath
            else:
                raise Exception("The dataset does not exist")
        except Exception as ex: 
            print(ex)

    def getBasePath(self):
        return self.basePath 

    def __str__(self) -> str:
        return self.basePath

