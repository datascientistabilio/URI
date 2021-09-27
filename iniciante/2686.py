# ERRO ERRO 2686 FIX
while True: 
    try: 
        minut9o = float(input())
        if minuto == 360 or minuto >=0 and minuto<= 105:
            print("Bom Dia!!")
            if minuto == 0 or minuto == 360:
                  print("06:00:00")
            if minuto >0 and minuto <=15:
                
                resp = minuto-0
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("06:0"+str(minuto)+":00")
                else:
                  print("06:"+str(minuto)+":00")
            elif minuto >15 and minuto <=30:
                resp = minuto-15
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("07:0"+str(minuto)+":00")
                else:
                  print("07:"+str(minuto)+":00")
            elif minuto >30 and minuto <=45:
                resp = minuto-30
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("08:0"+str(minuto)+":00")
                else:
                  print("08:"+str(minuto)+":00")
            elif minuto >45 and minuto <=60:
                resp = minuto-45
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("09:0"+str(minuto)+":00")
                else:
                  print("09:"+str(minuto)+":00")
            elif minuto >60 and minuto <=75:
                resp = minuto-60
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("10:0"+str(minuto)+":00")
                else:
                  print("10:"+str(minuto)+":00")
            elif minuto >75 and minuto <90:
                resp = minuto-75
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("11:0"+str(minuto)+":00")
                else:
                  print("11:"+str(minuto)+":00")
            elif minuto >90 and minuto <=105:
                resp = minuto-90
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("12:0"+str(minuto)+":00")
                else:
                  print("12:"+str(minuto)+":00")
        elif minuto >105 and minuto<=195:
            print("Boa Tarde!!")
            if minuto >105 and minuto <=120:
                resp = minuto-105
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("13:0"+str(minuto)+":00")
                else:
                  print("13:"+str(minuto)+":00")
            elif minuto >120 and minuto <=135:
                resp = minuto-120
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("14:0"+str(minuto)+":00")
                else:
                  print("14:"+str(minuto)+":00")
            elif minuto >135 and minuto <=150:
                resp = minuto-135
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("15:0"+str(minuto)+":00")
                else:
                  print("15:"+str(minuto)+":00")
            elif minuto >150 and minuto <=165:
                resp = minuto-150
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("16:0"+str(minuto)+":00")
                else:
                  print("16:"+str(minuto)+":00")
            elif minuto >165 and minuto <=180:
                resp = minuto-165
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("17:0"+str(minuto)+":00")
                else:
                  print("17:"+str(minuto)+":00")
            elif minuto >180 and minuto <=195:
                resp = minuto-180
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("18:0"+str(minuto)+":00")
                else:
                  print("18:"+str(minuto)+":00")
        elif minuto >195 and minuto<=285:
            print("Boa Noite!!")
            if minuto >195 and minuto <=210:
                resp = minuto-195
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("19:0"+str(minuto)+":00")
                else:
                  print("19:"+str(minuto)+":00")
            elif minuto >210 and minuto <=225:
                resp = minuto-210
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("20:0"+str(minuto)+":00")
                else:
                  print("20:"+str(minuto)+":00")
            elif minuto >225 and minuto <=240:
                resp = minuto-225
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("21:0"+str(minuto)+":00")
                else:
                  print("21:"+str(minuto)+":00")
            elif minuto >240 and minuto <=255:
                resp = minuto-240
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("22:0"+str(minuto)+":00")
                else:
                  print("22:"+str(minuto)+":00")
            elif minuto >255 and minuto <=270:
                resp = minuto-255
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("23:0"+str(minuto)+":00")
                else:
                  print("23:"+str(minuto)+":00")
            elif minuto >270 and minuto <=285:
                resp = minuto-270
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("00:0"+str(minuto)+":00")
                else:
                  print("00:"+str(minuto)+":00")
        elif minuto >285 and minuto<=360:
            print("De Madrugada!!")
            if minuto >285 and minuto <=299:
                resp = minuto-285
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("01:0"+str(minuto)+":00")
                else:
                  print("01:"+str(minuto)+":00")
            elif minuto >=300 and minuto <=315:
                resp = minuto-300
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("02:0"+str(minuto)+":00")
                else:
                  print("02:"+str(minuto)+":00")
            elif minuto >315 and minuto <=330:
                resp = minuto-315
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("03:0"+str(minuto)+":00")
                else:
                  print("03:"+str(minuto)+":00")
            elif minuto >330 and minuto <=345:
                resp = minuto-330
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("04:0"+str(minuto)+":00")
                else:
                  print("04:"+str(minuto)+":00")
            elif minuto >345 and minuto <=359:
                resp = minuto-345
                resp = int(resp*4)
                minuto = resp
                if resp >=0 and resp <= 9:
                  print("05:0"+str(minuto)+":00")
                else:
                  print("05:"+str(minuto)+":00")
    except EOFError:
                break