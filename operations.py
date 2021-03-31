from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


def increment(event,context):
    '''
    increment operation
    '''
    response={}
    response["increment"]=event["num"]+1

    return response

def square(event,context):
    response=event
    response["square"]=event["increment"]*event["increment"]
    return response
def decrement(event,context):
    data = load_breast_cancer()
    label_names = data['target_names']
    response=event
    response["decrement"]=event["square"]-1
    response["label_names"]=label_names[0]
    return response

