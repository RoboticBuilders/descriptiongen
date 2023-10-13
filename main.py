from bardapi import Bard

bard = Bard(token='ADD API KEY HERE') # get the bard api key
image = open('image.png', 'rb').read() # get the image locally
bard_answer = bard.ask_about_image('What is in the image?', image) # send the prompt to bard
print(bard_answer['content']) # print the answer
