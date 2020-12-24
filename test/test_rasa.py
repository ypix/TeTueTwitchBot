from rasa.nlu.model import Interpreter
import tarfile
from  os import path, listdir

def test_call(message, folder):
    interpreter = Interpreter.load(f"{folder}/nlu")
    result = interpreter.parse(message, only_output_properties=False)
    return result

def unpack_latest(target_dir):
    # find the lates update of the models
    all_tgz = [f"{target_dir}/{d}" for d in listdir(target_dir) if d.endswith(".tar.gz") and (path.isfile(f"{target_dir}/{d}"))]
    fname = max(all_tgz, key=path.getmtime)
    # print(fname)

    if fname.endswith("tar.gz"):
        # tar = tarfile.open(fname, "r:")
        tar = tarfile.open(fname, "r:gz")
        tar.extractall(path=target_dir)
        tar.close()
    return target_dir

if __name__ == '__main__':
    folder=f"{path.dirname(__file__)}/../rasa/models"
    target_dir=unpack_latest(f"{folder}")
    print(test_call("Du blödes Arsch", target_dir))
