import threading 

def do_this():
    print("this os our thread!")

def main():
    #threading.Thread(target=function)
    our_thread = threading.Thread(target=do_this,name=our_thread) #def name is thread-n < n is number of thread
    our_thread.start()#seperate procress

    print(threading.active_count()) #1
    print(threading.enumerate())#show all thread actually running  
    print(threading.current_thread())#show current thread is running

    #thread is like a procress
    #enumerate display different case 1 [thread1,thread2] case 2 [thread1] case3 [thread2]
    #sometime can do function do_this sometime not do function do_this
    #**if some thread is end, the all thread is stop .for example maybe thread 1 end first and thread 2 is stop! in that time
if(__name__=="__main__"):
    main()