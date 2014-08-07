#===============================================================================
# #!/usr/bin/python
# 
# import Queue
# import threading
# import time
# 
# exitFlag = 0
# 
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, q):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.q = q
#     def run(self):
#         print "Starting " + self.name
#         process_data(self.name, self.q)
#         print "Exiting " + self.name
# 
# def process_data(threadName, q):
#     while not exitFlag:
#         queueLock.acquire()
#         if not workQueue.empty():
#             data = q.get()
#             queueLock.release()
#             print "%s processing %s" % (threadName, data)
#         else:
#             queueLock.release()
#         time.sleep(1)
# 
# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = Queue.Queue(10)
# threads = []
# threadID = 1
# 
# # Create new threads
# for tName in threadList:
#     thread = myThread(threadID, tName, workQueue)
#     thread.start()
#     threads.append(thread)
#     threadID += 1
# 
# # Fill the queue
# queueLock.acquire()
# for word in nameList:
#     workQueue.put(word)
# queueLock.release()
# 
# # Wait for queue to empty
# while not workQueue.empty():
#     pass
# 
# # Notify threads it's time to exit
# exitFlag = 1
# 
# # Wait for all threads to complete
# for t in threads:
#     t.join()
# print "Exiting Main Thread"
#===============================================================================

#===============================================================================
# import time
# print "One"
# print "Two"
# time.sleep(4)
# print "Three"
#===============================================================================

#===============================================================================
# import time
# s = "4:34.234"
# hours, minutes, seconds = (["0", "0"] + s.split(":"))[-3:]
# hours = int(hours)
# minutes = int(minutes)
# seconds = float(seconds)
# miliseconds = int(3600000 * hours + 60000 * minutes + 1000 * seconds)
# print miliseconds
#===============================================================================
#===============================================================================
# import time
# from threading import Timer
# def print_time():
#     print "From print_time", time.time()
#   
# def print_some_times():
#     print time.time()
#     Timer(5, print_time, ()).start()
#     Timer(10, print_time, ()).start()
#     time.sleep(11)  # sleep while time-delay events execute
#     print time.time()
#   
# print_some_times()
#===============================================================================

#===============================================================================
# import sched, time
# s = sched.scheduler(time.time, time.sleep)
# def print_time(): print "From print_time", time.time()
# 
# def print_some_times():
#     print time.time()
#     s.enter(5, 1, print_time, ())
#     s.enter(10, 1, print_time, ())
#     s.run()
#     print time.time()
# 
# print_some_times()
#===============================================================================

#===============================================================================
# import sqlite3
# import time
# conn = sqlite3.connect("database_for_time_manager_tool.sqlite3")
# cursor = conn.execute("SELECT NAME  from Login_Detail where USERNAME='asd'")
# conn.execute('DELETE  from Login_Detail where USERNAME="as"')
# conn.commit()
# # print cursor
# # print time.ctime(time.time())
# # for col in cursor:
# #     print col[0],"One"
# # cursor = conn.execute("SELECT NAME  from Login_Detail where USERNAME='asd'")
# # for col in cursor:
# #     print col[0],"Two"
#      
# a = "One"
# print a.__add__(" Two")
# print 
# #!/usr/bin/python
#===============================================================================
 
#===============================================================================
# import thread
# import time
#   
# # Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    while True:
#       time.sleep(delay)
#       count += 1
#       print "%s: %s" % ( threadName, time.ctime(time.time()) )
#   
# # Create two threads as follows
# try:
#    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print "Error: unable to start thread"
#   
# while 1:
#    pass
#===============================================================================
