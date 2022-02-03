from loader.OriginalDataProcessor import OriginalDataProcessor
from loader.ScrapedDataProcessor import ScrapedDataProcessor
from fuzzymatcher.PhonebookMatcher import PhoneBookMatcher

if __name__ == '__main__':

    originalDataProcessor = OriginalDataProcessor()
    scrapedDataProcessor = ScrapedDataProcessor()
    phonebookMatcher = PhoneBookMatcher()
    print('hola')

    oldDf = originalDataProcessor.load("./resources/original_data.xlsx")

    newDf = scrapedDataProcessor.load("./resources/ua_constitucional.json")
    
    phonebookMatcher.fuzzyMerge(oldDf, newDf)