#use this module to check which Instagram usernames you are following who aren't following you back, and vice versa. enter the folder that contains this script in terminal and run insta_check.py

raw_input("Welcome! [PRESS ENTER]")
raw_input("First, log in to instagram on your web browser. Go to your profile and click \"Followers\". Scroll all the way to the bottom of the list so all elements are generated. \nRight click on the page and click 'Inspect'. Inside these developer tools, ctrl+f for the word \"Followers\" and find the line \"<div class = ...>Followers</div>\". \ncopy the line BELOW that using \"Copy element\". Paste and save this in a text file. [PRESS ENTER]")
raw_input("Follow the same procedure, but from your profile click on \"Following\", copy the line after <div class...>Following</div> and paste and save into a separate text file. [PRESS ENTER]")

#find difference between followers and following lists
def find_diff(file_1, file_2):
    #make a list of follower usernames
    followers = make_list(file_1)

    #make a list of following usernames
    following = make_list(file_2)

    #create a set of the difference
    diff = list(set(followers) ^ set(following))
    write_to = open("insta_diff.txt", "w")
    write_to.write(' '.join(diff))

def make_list(file_name):
    text = open(file_name, 'r').read()
    usernames = []
    beg = text.find("href")
    while beg != -1:
        end = text.find("/", beg + 7)
        usernames.append(text[beg+7:end])
        beg = text.find("href", beg + 7)
        beg = text.find("href", beg + 7)
    return usernames

followers = raw_input("Enter file name of followers: ")
following = raw_input("Enter file name of following: ")
find_diff(followers, following)

print "Nice! The usernames of the difference have been written in a file called insta_diff.txt in your folder."
