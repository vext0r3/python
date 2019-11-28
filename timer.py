import playsound
import time

def timer_normal():
    v=int(input('say:'))
    try:
        for j in range(1,4):
            time.sleep(1)
            print(j)
        for i in range(1,v+1):
            time.sleep(1)
            print(i,end=' ')
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        playsound.playsound('E:/notification_sound/Windows_Xp_Startup.mp3')
        print('\nfucking finish')

def timer_fanar():
    v=int(input('say:'))
    try:
        for i in range(v):
            for j in range(1,4):
                time.sleep(1)
                print(j)
            for i in range(1,21):
                time.sleep(1)
                print(i,end=' ')
            print('\nrest time')
            for z in range(1,8):
                time.sleep(1)
                print(z,end=' ')
            print('\nready...')
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        playsound.playsound('E:/notification_sound/Windows_Xp_Startup.mp3')
        print('\nfucking finish')
