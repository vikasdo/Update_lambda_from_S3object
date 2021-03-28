
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
    response=event
    response["decrement"]=event["square"]-1
    return response

