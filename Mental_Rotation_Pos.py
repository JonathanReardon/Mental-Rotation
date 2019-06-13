from psychopy import visual, core, gui, event
import glob, os
import random
import time
import csv
from psychopy.data import getDateStr

''' Mental Rotation / Emotional Valence task - High Valence '''

# create window
window = visual.Window([600,600],fullscr=False,color=("black"), allowGUI=True, monitor='testMonitor', units='deg')

# instructions
main_instruction = glob.glob(os.path.join('C:\Users\Jon\Documents\Sara_and_Molly\Day_1\Instructions','*.jpg'))
main_ins = [visual.ImageStim(window, img, name='main' + img) for img in main_instruction[:]]

main_page1 = main_ins[0]
main_page2 = main_ins[1]
main_page3 = main_ins[2]
main_page4 = main_ins[3]
thanks     = main_ins[4]

def main():
    main_page1.draw() 
    window.flip()
    event.waitKeys()
    main_page2.draw()
    window.flip()
    event.waitKeys()
    main_page3.draw()
    window.flip()
    event.waitKeys()
    
def after_practice_page():
    main_page4.draw()
    window.flip()
    event.waitKeys()
    
def thank_you():
    dataFile.close()
    thanks.draw()
    window.flip()
    event.waitKeys()
    window.close()
    core.quit()
    
class Fixation1(object):
    def __init__(self):
        self.fixation = visual.GratingStim(window, tex='sin', mask='cross', units="deg",size=(1,1), sf=(0), color="white")
        
        self.components = [self.fixation]
        
    def draw(self):
        [component.draw() for component in self.components]
        
fix = Fixation1()
    
# datafile
current_time = getDateStr()
dataFile = open(current_time +'.csv', 'w') 
writer = csv.writer(dataFile)
writer.writerow(['block','valence','stim_time','keyTime','reaction_time','correct (1=yes)','angle (1=0,2=50,3=150)','IAP image','mental_rot_image'])

##### Import Stimuli #####

# practice stimuli
practice_correct = glob.glob(os.path.join('.. Day_1\Practice\Correct','*.jpg'))
practice_incorrect = glob.glob(os.path.join('..Day_1\Practice\Incorrect','*.jpg'))

practice_corr = [visual.ImageStim(window, img, name='prac_corr' + img) for img in practice_correct[:]]
practice_incorr = [visual.ImageStim(window, img, name='prac_incorr' + img) for img in practice_incorrect[:]]

# import block1 mental rotation stimuli
block1_correct = glob.glob(os.path.join('.. Day_1\First_block_x20_Day_1\Correct','*.jpg'))
block1_incorrect = glob.glob(os.path.join('.. Day_1\First_block_x20_Day_1\Incorrect','*.jpg'))

block1_corr = [visual.ImageStim(window, img, name='block1_corr' + img) for img in block1_correct[:]]
block1_incorr = [visual.ImageStim(window, img, name='block1_incorr' + img) for img in block1_incorrect[:]]

random.shuffle(block1_corr)
random.shuffle(block1_incorr)

# import block2 mental rotation stimuli
block2_correct = glob.glob(os.path.join('.. Day_1\Second_block_x20_Day_1\Correct','*.jpg'))
block2_incorrect = glob.glob(os.path.join('.. Day_1\Second_block_x20_Day_1\Incorrect','*.jpg'))

block2_corr = [visual.ImageStim(window, img, name='block2_corr' + img) for img in block2_correct[:]]
block2_incorr = [visual.ImageStim(window, img, name='block2_incorr' + img) for img in block2_incorrect[:]]

random.shuffle(block2_corr)
random.shuffle(block2_incorr)

# import block3 mental rotation stimuli
block3_correct = glob.glob(os.path.join('.. Day_1\Third_block_x20_Day_1\Correct','*.jpg'))
block3_incorrect = glob.glob(os.path.join('.. Day_1\Third_block_x20_Day_1\Incorrect','*.jpg'))

block3_corr = [visual.ImageStim(window, img, name='block3_corr' + img) for img in block3_correct[:]]
block3_incorr = [visual.ImageStim(window, img, name='block3_incorr' + img) for img in block3_incorrect[:]]

random.shuffle(block3_corr)
random.shuffle(block3_incorr)

# import neutral arousal stimuli
global neutral_stimlist
neutral_stim = glob.glob(os.path.join('.. Day_1\Neutral','*.jpg'))
neutral_stimlist = [visual.ImageStim(window, img, name='neutral' + img) for img in neutral_stim[:]]
random.shuffle(neutral_stimlist)

# import low positive arousal stimuli
global lowpositive_stimlist
lowpositive_stim = glob.glob(os.path.join('.. Day_1\Positive\low_positive','*.png'))
lowpositive_stimlist = [visual.ImageStim(window, img, name='low_pos' + img) for img in lowpositive_stim[:]]
random.shuffle(lowpositive_stimlist)

# import high positive arousal stimuli
global highpositive_stimlist
highpositive_stim = glob.glob(os.path.join('.. Day_1\Positive\high_positive','*.png'))
highpositive_stimlist = [visual.ImageStim(window, img, name = 'high_pos' + img) for img in highpositive_stim[:]]
random.shuffle(highpositive_stimlist)

# set refresh rate & stim display times
refresh_rate = 60.0
stim_dur = 60       # duration for mental rotation images (set as 60, but switches on keypress)
arous_image_dur = .1 # 3 sec duration for arousal images
fixation_dur = .2      # 1 sec duration for fixation cross

stim_Frame = stim_dur * refresh_rate
stim_Frame = int(stim_Frame) 

arous_image_frames = arous_image_dur * refresh_rate
arous_image_frames = int(arous_image_frames)

fixation = fixation_dur * refresh_rate
fixation = int(fixation)

practice_meanRT     = []
block1_meanRTlist   = []
block2_meanRTlist   = []
block3_meanRTlist   = []

## make trial functions

def practice_correct():
    
    block = 'practice'
    valence = '-'
    stim_tim = '-'
    keyTime = '-'
    thisResp = '-'
    image = '-'
    
    global practice_corr, prac_meanRT
    running = 1
    
    while running ==1:
        
        for frames in range(stim_Frame):
            practice_corr[0].draw()
            start = window.flip()
            if frames == 0:
                 stim_time = start
            allKeys = event.getKeys(keyList = ('f','h','escape'))
            for thisKey in allKeys:
                if thisKey == 'escape':
                    print("you quit")
                    dataFile.close()
                    window.close()
                    core.quit()
                if thisKey == 'f':
                    keyTime=core.getTime()
                    thisResp = 1      
                    
                elif thisKey == 'h':
                    keyTime=core.getTime()
                    thisResp = 0
                    
            if thisResp == 1 or thisResp == 0:
                break
                
        ment_rot_image = practice_corr[0].name
        
        ment_rot_angle = practice_corr[0].name.split("Correct")[1]
        angle = "-"
        
        if ment_rot_angle[1] == "2" and ment_rot_angle[2] == "_" or ment_rot_angle[1] == "4" and ment_rot_angle[2] == "_":
            angle = 1
        if ment_rot_angle[1] == "6" and ment_rot_angle[2] == "_" or ment_rot_angle[1] == "8" and ment_rot_angle[2] == "_":
            angle = 2
        elif ment_rot_angle[1] == "1" and ment_rot_angle[2] == "0" or ment_rot_angle[1] == "1" and ment_rot_angle[2] == "2":
            angle = 3
        running = 2
        
    window.flip()
    
    reaction_time = keyTime - stim_time
    practice_corr.pop(0)
    
    practice_meanRT.append(reaction_time)
    prac_meanRT = sum(practice_meanRT)/len(practice_meanRT)
    
    dataFile.write('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image, ment_rot_image)) #send results to datafile
    #print ('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image, ment_rot_image))
 
def practice_incorrect():
    
    block = 'practice'
    valence = '-'
    stim_tim = '-'
    keyTime = '-'
    thisResp = '-'
    image = '-'
    
    global practice_incorr, prac_meanRT
    running = 1
    
    while running ==1:

        for frames in range(stim_Frame):
            practice_incorr[0].draw()
            start = window.flip()
            if frames == 0:
                 stim_time = start

            allKeys = event.getKeys(keyList = ('f','h','escape'))
            for thisKey in allKeys:
                if thisKey == 'escape':
                    print("you quit")
                    dataFile.close()
                    window.close()
                    core.quit()
                if thisKey == 'f':
                    keyTime=core.getTime()
                    thisResp = 0      
                    
                elif thisKey == 'h':
                    keyTime=core.getTime()
                    thisResp = 1
                    
            if thisResp == 1 or thisResp == 0:
                break
                
        ment_rot_image = practice_incorr[0].name
        
        ment_rot_angle = practice_incorr[0].name.split("Incorrect")[1]
        angle="-"
        
        if ment_rot_angle[1] == "1" and ment_rot_angle[2] == "_" or ment_rot_angle[1] == "3" and ment_rot_angle[2] == "_":
            angle = 1
        if ment_rot_angle[1] == "5" and ment_rot_angle[2] == "_" or ment_rot_angle[1] == "7" and ment_rot_angle[2] == "_":
            angle = 2
        elif ment_rot_angle[1] == "9" and ment_rot_angle[2] == "_" or ment_rot_angle[1] == "1" and ment_rot_angle[2] == "1":
            angle = 3
        running = 2
        
    window.flip()
    
    reaction_time = keyTime - stim_time
    practice_incorr.pop(0)
    
    practice_meanRT.append(reaction_time)
    prac_meanRT = sum(practice_meanRT)/len(practice_meanRT)
    
    dataFile.write('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image, ment_rot_image)) #send results to datafile
    #print ('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image, ment_rot_image))

    
def block1_correct():
    
    block = '1'
    valence = 'neutral'
    stim_tim = '-'
    keyTime = '-'
    thisResp = '-'
    
    global block1_corr, neutral_stimlist, block1_meanRT
    running = 1
    
    while running ==1:
        
        for frames in range(arous_image_frames):
            neutral_stimlist[0].draw()
            window.flip()
            
        for frame in range(fixation):
            fix.draw()
            window.flip()
            
        event.clearEvents() 
        for frames in range(stim_Frame):
            block1_corr[0].draw()
            start = window.flip()
            if frames == 0:
                 stim_time = start

            allKeys = event.getKeys(keyList = ('f','h','escape'))
            for thisKey in allKeys:
                if thisKey == 'escape':
                    print("you quit")
                    window.close()
                    core.quit()
                if thisKey == 'f':
                    keyTime=core.getTime()
                    thisResp = 1      
                    
                elif thisKey == 'h':
                    keyTime=core.getTime()
                    thisResp = 0
                    
            if thisResp == 1 or thisResp == 0:
                break
                
        image = neutral_stimlist[0].name
        ment_rot_image = block1_corr[0].name
        ment_rot_angle = block1_corr[0].name.split("Correct")[1]
        
        if ment_rot_angle[1] == "1" and ment_rot_angle[2] == "3" or ment_rot_angle[1] == "1" and ment_rot_angle[2] == "5":
            angle = 1
        if ment_rot_angle[1] == "1" and ment_rot_angle[2] == "7" or ment_rot_angle[1] == "1" and ment_rot_angle[2] == "9" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "1" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "3":
            angle = 2
        elif ment_rot_angle[1] == "2" and ment_rot_angle[2] == "5" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "7" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "9" or ment_rot_angle[1] == "3" and ment_rot_angle[2] == "1":
            angle = 3

        running = 2
        
    window.flip()
    
    reaction_time = keyTime - stim_time
    block1_corr.pop(0)
    neutral_stimlist.pop(0)
    
    block1_meanRTlist.append(reaction_time)
    block1_meanRT = sum(block1_meanRTlist)/len(block1_meanRTlist)
    
    dataFile.write('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image, ment_rot_image)) #send results to datafile
    #print ('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image, ment_rot_image))
    
def block1_incorrect():
    
    block = '1'
    valence = 'neutral'
    stim_tim = '-'
    keyTime = '-'
    thisResp = '-'
    
    global block1_incorr, neutral_stimlist, block1_meanRT
    running = 1
    
    while running ==1:
        
        for frames in range(arous_image_frames):
            neutral_stimlist[0].draw()
            window.flip()
            
        for frame in range(fixation):
            fix.draw()
            window.flip()
        
        event.clearEvents() 
        for frames in range(stim_Frame):
            block1_incorr[0].draw()
            start = window.flip()
            if frames == 0:
                 stim_time = start
            
            allKeys = event.getKeys(keyList = ('f','h','escape'))
            for thisKey in allKeys:
                if thisKey == 'escape':
                    print("you quit")
                    window.close()
                    core.quit()
                if thisKey == 'f':
                    keyTime=core.getTime()
                    thisResp = 0      
                    
                elif thisKey == 'h':
                    keyTime=core.getTime()
                    thisResp = 1
                    
            if thisResp == 1 or thisResp == 0:
                break
        
        image = neutral_stimlist[0].name
        ment_rot_image = block1_incorr[0].name
        ment_rot_angle = block1_incorr[0].name.split("Incorrect")[1]
        
        if ment_rot_angle[1] == "1" and ment_rot_angle[2] == "4" or ment_rot_angle[1] == "1" and ment_rot_angle[2] == "6":
            angle = 1
        if ment_rot_angle[1] == "1" and ment_rot_angle[2] == "8" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "0" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "2" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "4":
            angle = 2
        elif ment_rot_angle[1] == "2" and ment_rot_angle[2] == "6" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "8" or ment_rot_angle[1] == "3" and ment_rot_angle[2] == "0" or ment_rot_angle[1] == "3" and ment_rot_angle[2] == "2":
            angle = 3
        
        running = 2
        
    window.flip()
    
    reaction_time = keyTime - stim_time
    block1_incorr.pop(0)
    neutral_stimlist.pop(0)
    
    block1_meanRTlist.append(reaction_time)
    block1_meanRT = sum(block1_meanRTlist)/len(block1_meanRTlist)
    
    dataFile.write('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp,angle, image, ment_rot_image)) #send results to datafile
    #print ('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle,image, ment_rot_image))
    
def block2_correct():
    
    block = '2'
    valence = 'low positive'
    stim_tim = '-'
    keyTime = '-'
    thisResp = '-'
    
    global block2_corr, lowpositive_stimlist, block2_meanRT
    running = 1
    
    while running ==1:
        
        for frames in range(arous_image_frames):
            lowpositive_stimlist[0].draw()
            window.flip()
            
        for frame in range(fixation):
            fix.draw()
            window.flip()
        
        event.clearEvents() 
        for frames in range(stim_Frame):
            block2_corr[0].draw()
            start = window.flip()
            if frames == 0:
                 stim_time = start

            allKeys = event.getKeys(keyList = ('f','h','escape'))
            for thisKey in allKeys:
                if thisKey == 'escape':
                    print("you quit")
                    window.close()
                    core.quit()
                if thisKey == 'f':
                    keyTime=core.getTime()
                    thisResp = 1      
                    
                elif thisKey == 'h':
                    keyTime=core.getTime()
                    thisResp = 0
                    
            if thisResp == 1 or thisResp == 0:
                break
                
        image = lowpositive_stimlist[0].name
        ment_rot_image = block2_corr[0].name
        ment_rot_angle = block2_corr[0].name.split("Correct")[1]
        
        if ment_rot_angle[1] == "1" and ment_rot_angle[2] == "3" or ment_rot_angle[1] == "1" or ment_rot_angle[2] == "5":
            angle = 1
        if ment_rot_angle[1] == "1" and ment_rot_angle[2] == "9" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "1"or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "3":
            angle = 2
        elif ment_rot_angle[1] == "2" and ment_rot_angle[2] == "5" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "7" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "9" or ment_rot_angle[1] == "3" and ment_rot_angle[2] == "1":
            angle = 3

        running = 2
        
    window.flip()
    
    reaction_time = keyTime - stim_time
    block2_corr.pop(0)
    lowpositive_stimlist.pop(0)
    
    block2_meanRTlist.append(reaction_time)
    block2_meanRT = sum(block2_meanRTlist)/len(block2_meanRTlist)
    
    dataFile.write('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image, ment_rot_image)) #send results to datafile
    #print ('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image, ment_rot_image))
    
def block2_incorrect():
    
    block = '2'
    valence = 'low positive'
    stim_tim = '-'
    keyTime = '-'
    thisResp = '-'
    
    global block2_incorr, lowpositive_stimlist, block2_meanRT
    running = 1
    
    while running ==1:
        
        for frames in range(arous_image_frames):
            lowpositive_stimlist[0].draw()
            window.flip()
            
        for frame in range(fixation):
            fix.draw()
            window.flip()
        
        event.clearEvents() 
        for frames in range(stim_Frame):
            block2_incorr[0].draw()
            start = window.flip()
            if frames == 0:
                 stim_time = start

            allKeys = event.getKeys(keyList = ('f','h','escape'))
            for thisKey in allKeys:
                if thisKey == 'escape':
                    print("you quit")
                    window.close()
                    core.quit()
                if thisKey == 'f':
                    keyTime=core.getTime()
                    thisResp = 0      
                    
                elif thisKey == 'h':
                    keyTime=core.getTime()
                    thisResp = 1
                    
            if thisResp == 1 or thisResp == 0:
                break
                
        image = lowpositive_stimlist[0].name
        ment_rot_image = block2_incorr[0].name
        
        ment_rot_angle = block2_incorr[0].name.split("Incorrect")[1]
        
        if ment_rot_angle[1] =="1" and ment_rot_angle[2] == "4" or ment_rot_angle[1] =="1" and ment_rot_angle[2] == "6":
            angle = 1
        if ment_rot_angle[1] =="1" and ment_rot_angle[2] == "8" or ment_rot_angle[1] =="2" and ment_rot_angle[2] == "0" or ment_rot_angle[1] =="2" and ment_rot_angle[2] == "2" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "4":
            angle = 2
        elif ment_rot_angle[1] =="2" and ment_rot_angle[2] == "6" or ment_rot_angle[1] =="2" and ment_rot_angle[2] == "8" or ment_rot_angle[1] =="3" and ment_rot_angle[2] == "0" or ment_rot_angle[1] == "3" and ment_rot_angle[2] == "2":
            angle = 3
        
        running = 2
        
    window.flip()
    
    reaction_time = keyTime - stim_time
    block2_incorr.pop(0)
    lowpositive_stimlist.pop(0)
    
    block2_meanRTlist.append(reaction_time)
    block2_meanRT = sum(block2_meanRTlist)/len(block2_meanRTlist)
    
    dataFile.write('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image,ment_rot_image)) #send results to datafile
    #print ('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image, ment_rot_image)) 
    
def block3_correct():
    
    block = '3'
    valence = 'high positive'
    stim_tim = '-'
    keyTime = '-'
    thisResp = '-'
    
    global block3_corr, highpositive_stimlist, block3_meanRT
    running = 1
    
    while running ==1:
        
        for frames in range(arous_image_frames):
            highpositive_stimlist[0].draw()
            window.flip()
            
        for frame in range(fixation):
            fix.draw()
            window.flip()
        
        event.clearEvents() 
        for frames in range(stim_Frame):
            block3_corr[0].draw()
            start = window.flip()
            if frames == 0:
                 stim_time = start

            allKeys = event.getKeys(keyList = ('f','h','escape'))
            for thisKey in allKeys:
                if thisKey == 'escape':
                    print("you quit")
                    window.close()
                    core.quit()
                if thisKey == 'f':
                    keyTime=core.getTime()
                    thisResp = 1      
                    
                elif thisKey == 'h':
                    keyTime=core.getTime()
                    thisResp = 0
                    
            if thisResp == 1 or thisResp == 0:
                break
                
        image = highpositive_stimlist[0].name
        ment_rot_image = block3_corr[0].name
        
        ment_rot_angle = block3_corr[0].name.split("Correct")[1]
        
        if ment_rot_angle[1] =="5" and ment_rot_angle[2] == "_" or ment_rot_angle[1] =="7" and ment_rot_angle[2] == "_":
            angle = 1
        if ment_rot_angle[1] =="9" and ment_rot_angle[2] == "_" or ment_rot_angle[1] =="1" and ment_rot_angle[2] == "1" or ment_rot_angle[1] =="1" and ment_rot_angle[2] == "3" or ment_rot_angle[1] == "1" and ment_rot_angle[2] == "5":
            angle = 2
        elif ment_rot_angle[1] =="1" and ment_rot_angle[2] == "7" or ment_rot_angle[1] =="1" and ment_rot_angle[2] == "9" or ment_rot_angle[1] =="2" and ment_rot_angle[2] == "1" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "3":
            angle = 3

        running = 2
        
    window.flip()
    
    reaction_time = keyTime - stim_time
    block3_corr.pop(0)
    highpositive_stimlist.pop(0)
    
    block3_meanRTlist.append(reaction_time)
    block3_meanRT = sum(block3_meanRTlist)/len(block3_meanRTlist)
    
    dataFile.write('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image, ment_rot_image)) #send results to datafile
    #print ('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image, ment_rot_image))
    
def block3_incorrect():
    
    block = '3'
    valence = 'high positive'
    stim_tim = '-'
    keyTime = '-'
    thisResp = '-'
    
    global block3_incorr, highpositive_stimlist, block3_meanRT
    running = 1
    
    while running ==1:
        
        for frames in range(arous_image_frames):
            highpositive_stimlist[0].draw()
            window.flip()
            
        for frame in range(fixation):
            fix.draw()
            window.flip()
        
        event.clearEvents() 
        for frames in range(stim_Frame):
            block3_incorr[0].draw()
            start = window.flip()
            if frames == 0:
                 stim_time = start

            allKeys = event.getKeys(keyList = ('f','h','escape'))
            for thisKey in allKeys:
                if thisKey == 'escape':
                    print("you quit")
                    window.close()
                    core.quit()
                if thisKey == 'f':
                    keyTime=core.getTime()
                    thisResp = 0      
                    
                elif thisKey == 'h':
                    keyTime=core.getTime()
                    thisResp = 1
                    
            if thisResp == 1 or thisResp == 0:
                break
                
        image = highpositive_stimlist[0].name
        ment_rot_image = block3_incorr[0].name
        
        ment_rot_angle = block3_incorr[0].name.split("Incorrect")[1]
        
        if ment_rot_angle[1] =="6" and ment_rot_angle[2] == "_" or ment_rot_angle[1] =="8" and ment_rot_angle[2] == "_":
            angle = 1
        if ment_rot_angle[1] =="1" and ment_rot_angle[2] == "0" or ment_rot_angle[1] =="1" and ment_rot_angle[2] == "2" or ment_rot_angle[1] =="1" and ment_rot_angle[2] == "4" or ment_rot_angle[1] == "1" and ment_rot_angle[2] == "6":
            angle = 2
        elif ment_rot_angle[1] =="1" and ment_rot_angle[2] == "8" or ment_rot_angle[1] =="2" and ment_rot_angle[2] == "0" or ment_rot_angle[1] =="2" and ment_rot_angle[2] == "2" or ment_rot_angle[1] == "2" and ment_rot_angle[2] == "4":
            angle = 3
            
        running = 2
        
    window.flip()
    
    reaction_time = keyTime - stim_time
    block3_incorr.pop(0)
    highpositive_stimlist.pop(0)
    
    block3_meanRTlist.append(reaction_time)
    block3_meanRT = sum(block3_meanRTlist)/len(block3_meanRTlist)
    
    dataFile.write('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image,ment_rot_image)) #send results to datafile
    #print ('%s,%s,%f,%f,%f,%i,%s,%s,%s\n'%(block, valence, stim_time, keyTime, reaction_time, thisResp, angle, image, ment_rot_image))
    
practice_trials = [practice_correct,practice_correct,practice_correct,practice_correct,practice_correct,practice_correct,
                    practice_incorrect,practice_incorrect,practice_incorrect,practice_incorrect,practice_incorrect,practice_incorrect]
random.shuffle(practice_trials)

block1_trials = [block1_correct,block1_correct, block1_correct, block1_correct, block1_correct, block1_correct, block1_correct, block1_correct, block1_correct, block1_correct, 
                 block1_incorrect,block1_incorrect,block1_incorrect,block1_incorrect,block1_incorrect,block1_incorrect,block1_incorrect,block1_incorrect,block1_incorrect,block1_incorrect,]
                 
random.shuffle(block1_trials)

block2_trials = [block2_correct, block2_correct, block2_correct, block2_correct, block2_correct, block2_correct, block2_correct, block2_correct, block2_correct, block2_correct,
                block2_incorrect,block2_incorrect,block2_incorrect,block2_incorrect,block2_incorrect,block2_incorrect,block2_incorrect,block2_incorrect,block2_incorrect,block2_incorrect]

random.shuffle(block2_trials)

block3_trials = [block3_correct, block3_correct, block3_correct, block3_correct, block3_correct, block3_correct, block3_correct, block3_correct, block3_correct, block3_correct,
                block3_incorrect,block3_incorrect,block3_incorrect,block3_incorrect,block3_incorrect,block3_incorrect,block3_incorrect,block3_incorrect,block3_incorrect,block3_incorrect]

random.shuffle(block3_trials)

## main routine
main()
fix.draw()
window.flip()
core.wait(.5)

running = 1
while running:
    
    global prac_meanRT, block1_meanRT, block2_meanRT, block3_meanRT
    
    for trial in practice_trials:
        trial()
    after_practice_page()

    for trial in block1_trials:
        trial()
        
    for trial in block2_trials:
        trial()
        
    for trial in block3_trials:
        trial()
    
    dataFile.write("\n")
    dataFile.write("\n")
    dataFile.write("Reaction Time Means\n")
    dataFile.write("Practice Mean RT: %f\n"%(prac_meanRT)) 
    dataFile.write("Neutral Mean RT:  %f\n"%(block1_meanRT)) 
    dataFile.write("Low Pos Mean RT: %f\n"%(block2_meanRT)) 
    dataFile.write("High Pos Mean RT:  %f\n"%(block3_meanRT)) 
    
    print "overall mean RT for practice: %f"  %(prac_meanRT)
    print "overall mean RT for neutral: %f"   %(block1_meanRT)
    print "overall mean RT for low pos: %f"   %(block2_meanRT)
    print "overall mean RT for high pos: %f"  %(block3_meanRT)
    
    thank_you()
    
    running = 2
    