#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading 


def do_this():
    global dead
    count = 0

    print("this os our thread!")
    while(not dead):
        count+=1
        print("count func",count)
        pass

def main():
    global dead
    dead = False

    #by raw main thread is not daemon = false
    our_thread = threading.Thread(target=do_this)
    our_thread.setDaemon(True)# true จะทำให้ loop while หยุดเมื่อ main thread ทำบรรทัด 28 เสร็จ
    our_thread.start()#seperate procress


    print("daemon ",our_thread.isDaemon())
    print("count ",threading.active_count())
    print("enumerate ",threading.enumerate())

    raw_input("hit enter to thread die:")

    print("last line stop deamon")

    # daemon จะถูก set เบื่องต้นเป็น false ทุก thread
    # daemon thread = true ตามกฏของ python python จะออกจากโปรแกรมก็ต่อเมื่อ non-daemon(main thread) ทำงานจบ


if(__name__=="__main__"):
    main()