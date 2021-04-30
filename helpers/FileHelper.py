import json


def load(path):
    with open(path) as fpr:
        fdata = json.load(fpr)
        fpr.close()
    return fdata


def dump(path, data):
    with open(path, 'w', encoding='utf-8') as fpw:
        json.dump(data, fpw, ensure_ascii=False, indent=4)
        fpw.close()