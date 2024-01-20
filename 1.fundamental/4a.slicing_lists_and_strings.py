"""
    Slicing is a way of extracting certain elements from lists and strings
    list[start: end: step]
    step allows us to skip a certain number of values
"""

MY_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Get value from 1 to 4: ", MY_LIST[:5])
print("Get value from 3 to 7: ", MY_LIST[3:8])
print("Get value from 3 to 7 using negative index: ", MY_LIST[-7:-2])
print("Get value from 1 to 7 using positive negative index: ", MY_LIST[1:-2])
print("Get value from 1 to end of the list by leaving the end index: ", MY_LIST[1:])
print(
    "Get value from 1 to 8 by leaving the front index and using negative index: ",
    MY_LIST[:-1],
)
print("Get value from the entire list by leaving the indexex: ", MY_LIST[:])
print("Get value from 1 to 8 and every 2nd values : ", MY_LIST[2:-1:2])
print("Get value from 9 to 3 in reserve : ", MY_LIST[-1:2:-1])
print("Get value from 9 to 3 in reserve and every 2nd values: ", MY_LIST[-1:2:-2])
print("Get value from the entire list in reserve: ", MY_LIST[::-1])

#################################################################
#           Slicing in String
#################################################################
SAMPLE_URL = "http://coreyms.com"
print("Curent URL", SAMPLE_URL)
print("Reverse the URL", SAMPLE_URL[::-1])
print("Get the topic level domain: ", SAMPLE_URL[-4:])
print("Get the URL without the http://: ", SAMPLE_URL[7:])
print("Get the URL without the http:// and the topic level domain: ", SAMPLE_URL[7:-4])
