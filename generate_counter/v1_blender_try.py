import bpy

def progStart():
    _inputValue = 0;
    while _inputValue != 4:
        if _inputValue == 0:
            print ('Willkommen! \n[1] Generiere Fortlaufend\n[2] Generiere spez. Intervall\n[3] Something\n[4] Beende Programm')
            _inputValue = input()
        elif int(_inputValue) == 1:
            _newSheetCount = int(input())
            generateOngoing(_newSheetCount)
            _inputValue = 0
        elif int(_inputValue) == 2: 
            _startOfRange = input("Beginn?\n")
            _endOfRange = input("Ende?\n")
            generateSpecific(_startOfRange, _endOfRange)
            _inputValue = 0
        elif int(_inputValue) == 3: 
            print("three works")
            _inputValue = 0
    print("left loop now");
        
def generateOngoing(_newSheetCount):
    i = 0;
    while i < _newSheetCount:
        _myStr = bpy.data.objects["Text.002"].data.body
        _myInt = int(_myStr) + 1
        if _myInt < 10: 
            _myStr = "00"+str(_myInt)+" "
        elif _myInt > 10 and _myInt < 100:     
            _myStr = "0"+str(_myInt)+" "
        elif _myInt > 100 and _myInt < 1000: 
            _myStr = str(_myInt)+" "
        else: _myStr = "9999"
        bpy.data.objects["Text.002"].data.body = _myStr
        i=i+1
        bpy.ops.render.render(write_still = 1)
    bpy.ops.wm.save_mainfile()
    print('done ongoing');
    
def generateSpecific(_startOfRange, _endOfRange):
    print('done specific');
progStart();
