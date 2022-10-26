
eng = open("jounaittxt.txt","r")
print(eng.readable())
#print(eng.read())
#لايمكن استخدام تعليمتين قراءة بذات الوقت لانو اللست تكون فارغة بعد نعليمةقراءة واحدة
print(eng.readlines()[0])
#هون اخدا ك list


eng.close()