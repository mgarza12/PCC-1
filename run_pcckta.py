import run_pcc
from run_pcc import *
import classifiers.PCCKTA
from classifiers.PCCKTA import *

if __name__ == "__main__":
		numpy.seterr(all='raise')
		logging.basicConfig(filename="./output/PCCKTAClassifier.log", level=logging.DEBUG)
		logf = logging.getLogger(__name__)
		
		if not os.path.exists("./output"): os.makedirs("./output")

		try:
			#logf.info("Started processing the scene dataset")
			#processDataset("../../data/scene/scene-train.csv", "../../data/scene/scene-test.csv", "./output/scene-train-pcckta.txt", "./output/scene-test-pcckta.txt", 294, 6)
			#logf.info("Finished processing the scene dataset")
			
			#logf.info("Started processing the yeast dataset")
			#processDataset("../../data/yeast/yeast-train.csv", "../../data/yeast/yeast-test.csv", "./output/yeast-train-pcckta.txt", "./output/yeast-test-pcckta.txt", 103, 14)
			#logf.info("Finished processing the yeast dataset")

			logf.info("Started processing the medical dataset")
			processDataset("../../data/medical/medical-train.csv", "../../data/medical/medical-test.csv", "./output/medical-train-pcckta.txt", "./output/medical-test-pcckta.txt", 1449, 45)
			logf.info("Finished processing the medical dataset")

			#logf.info("Started processing the genbase dataset")
			#processDataset("../../data/genbase/genbase-train.csv", "../../data/genbase/genbase-test.csv", "./output/genbase-train-pcckta.txt", "./output/genbase-test-pcckta.txt", 1186,26)
			#logf.info("Finished processing the genbase dataset")

			#logf.info("Started processing the enron dataset")
			#processDataset("../../data/enron/enron-train.csv", "../../data/enron/enron-test.csv", "./output/enron-train-pcckta.txt", "./output/enron-test-pcckta.txt", 1001,53)
			#logf.info("Finished processing the enron dataset")

			logf.info("Started processing the emotions dataset")
			processDataset("../../data/emotions/emotions-train.csv", "../../data/emotions/emotions-test.csv", "./output/emotions-train-pcckta.txt", "./output/emotions-test-pcckta.txt", 72,6)
			logf.info("Finished processing the emotion dataset")
		except Exception:
			traceback.print_exc(file=sys.stdout)
			pdb.set_trace()

