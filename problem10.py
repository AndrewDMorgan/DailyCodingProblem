import time

def WaitThenCall(function, timeMilliseconds) -> None:
    time.sleep(timeMilliseconds*0.001)
    function()

WaitThenCall(lambda : print("hello world"), 1000)
