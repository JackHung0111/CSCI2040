# 1155108381 1155110154 
# lab 3 p3

import pickle as pkl
filename = "followers.pydata"

# (a)
def load_data(file):
    f1 = open(file,"rb")
    result = pkl.load(f1)
    f1.close()
    return result

# (b)
def query_following(user_name):
    dict1 = load_data(filename)
    result = 0
    for name in dict1:
        for follower in dict1[name]:
            if(follower == user_name):
                result += 1
    return result

# (c)
def update():
    dict2 = load_data(filename)
    ### add a new follower Lorna Carrico to the user William Smith
    dict2["William Smith"].append("Lorna Carrico")
    ### add a new user Anne Smelcer with followers Christine Phillips, Charles Mason and Tim Lathrop
    dict2["Anne Smelcer"] = ["Christine Phillips", "Charles Mason", "Tim Lathrop"]
    ### use pickle to save the updated dictionary to the same directory hierarchy as your script for this exercise as file followers-updated.pydata
    f2 = open("followers-updated.pydata","wb")
    pkl.dump(dict2,f2)

# (d)
def get_num_of_followers():
    update()
    f3 = open("followers-updated.pydata","rb")
    dict3 = pkl.load(f3)
    f3.close()
    result = {}
    for name in dict3:
        result[name] = len(dict3[name])
    return result

