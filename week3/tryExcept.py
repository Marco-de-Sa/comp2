x = "hello"
try :
    # This will raise an error , if x is not an integer
    int(x)
except:
    # This will be printed if x is not an integer
    print ("An error occurred")
else:
    # This will be printed if x is in fact an integer
    print("No error occurred")
finally:
    print("This will always be printed")