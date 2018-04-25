class sleep_till_future():

    def sleep_till_future(f_year,f_month,f_day,f_hour,f_minute,f_seconds):
        import datetime
        import time
        #The function takes the current time, and calculates for how many seconds should sleep until a user provided minute in the future.

        t = datetime.datetime.today()
        future = datetime.datetime.strftime(f_year,f_month,f_day,f_hour,f_minute,f_seconds)
        seconds_till_future = (future - t).total_seconds()

        assert future > t, 'ERROR! Enter a valid minute in the future.'

        print("Current date (MMDDYYYY): " + str(t.month)+"."+str(t.day)+"."+str(t.year)+" "+str(t.hour)+":"+str(t.minute))
        print("Sleep until (MMDDYYYY):  " + str(future.month)+"."+str(future.day)+"."+str(future.year)+" "+ str(future.hour)+":"+str(future.minute))
        print("I will sleep " + str(seconds_till_future) + " seconds.")

        time.sleep(seconds_till_future)
        print("I slept for "+str(seconds_till_future)+" seconds!")