

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.

For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. 

_Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

### To start the semester, you will need:
1. Read about Git [here](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).
2. Set up your own Github "Lab Hub" repository to keep all you work in record by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md).
3. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how to](https://guides.github.com/features/mastering-markdown/) organize and post links to your submissions on your README.md so we can find them easily.


### For this lab, you will need:
1. Paper
2. Markers/ Pens
3. Scissors
4. Smart Phone -- The main required feature is that the phone needs to have a browser and display a webpage.
5. Computer -- We will use your computer to host a webpage which also features controls.
6. Found objects and materials -- You will have to costume your phone so that it looks like some other devices. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case, etc. Be creative!

### Deliverables for this lab are: 
1. 7 Storyboards
1. 3 Sketches/photos of costumed devices
1. Any reflections you have on the process
1. Video sketch of 3 prototyped interactions
1. Submit the items above in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same from each person in the group.

### The Report
This README.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above). Following the format below, you can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in your README.md for the lab.

## Lab Overview
For this assignment, you are going to:

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

To stage an interaction with your interactive device, think about:

_Setting:_ Where is this interaction happening? (e.g., a jungle, the kitchen) When is it happening?

_Players:_ Who is involved in the interaction? Who else is there? If you reflect on the design of current day interactive devices like the Amazon Alexa, it’s clear they didn’t take into account people who had roommates, or the presence of children. Think through all the people who are in the setting.

_Activity:_ What is happening between the actors?

_Goals:_ What are the goals of each player? (e.g., jumping to a tree, opening the fridge). 

The interactive device can be anything *except* a computer, a tablet computer or a smart phone, but the main way it interacts needs to be using light.

\*\***Describe your setting, players, activity and goals here.**\*\*

_Setting:_ In the recycling station/room

_Players:_ People who are confused about recycling 

_Activity:_ The players show their recycling/trash to the sensor of the interactive device, and the device tell the player how to throw their recycling/trash through lights of different colors.

_Goals:_ Make recycling faster and successful

Storyboards are a tool for visually exploring a users interaction with a device. They are a fast and cheap method to understand user flow, and iterate on a design before attempting to build on it. Take some time to read through this explanation of [storyboarding in UX design](https://www.smashingmagazine.com/2017/10/storyboarding-ux-design/). Sketch seven storyboards of the interactions you are planning. **It does not need to be perfect**, but must get across the behavior of the interactive device and the other characters in the scene. 

\*\***Include pictures of your storyboards here**\*\*

![plot](https://github.com/peter2520/Interactive-Lab-Hub/blob/3cff70b726cb61ed2979016596eb199d983065f1/Lab%201/Storyboard1.jpg)
![plot](https://github.com/peter2520/Interactive-Lab-Hub/blob/3cff70b726cb61ed2979016596eb199d983065f1/Lab%201/Storyboard2.jpg)


Present your ideas to the other people in your breakout room (or in small groups). You can just get feedback from one another or you can work together on the other parts of the lab.

\*\***Summarize feedback you got here.**\*\*
After presenting my ideas to my friend Hau Chu and Alan Hsieh, they thought the idea of recycling sensor and hiking device are the most creative ones. I think the recycling sensor is more useful for more people in daily life.

Developing prototype devices with color lights are sufficient. However, adding sounds or vibration can make the interaction/instruction more explicit in further steps.

## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

\*\***Are there things that seemed better on paper than acted out?**\*\*

The color showed on the screen show the recycling type of our detected recycling and which recycling bins should the each recycling throw in. I think storyboard can showed exactly what I assume the device work, and I can depict how the device behave in much more scenarios. On the other hand, it’s hard to act out and show every behavior I assume while some scenarios are hard to build in reality.

\*\***Are there new ideas that occur to you or your collaborators that come up from the acting?**\*\*

The new ideas that occur to me are that I can use different colored lights to indicate the users to help the device to recognize the recycling better. A recycling may have different part of recycling, so we might separate them and show the recycling to our device respectively.

## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.

\*\***Give us feedback on Tinkerbelle.**\*\*
It is easy to use in developing prototypes. Adding features like changing colors automatically by user setting may be more useful in various scenarios.

## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

\*\***Include your first attempts at recording the set-up video here.**\*\*

[![Watch the video](https://github.com/peter2520/Interactive-Lab-Hub/blob/Fall2022/Lab%201/setup.png)](https://youtube.com/shorts/uEX6nYRbGEo)


Now, hange the goal within the same setting, and update the interaction with the paper prototype. 

\*\***Show the follow-up work here.**\*\*

[![Watch the video](https://github.com/peter2520/Interactive-Lab-Hub/blob/Fall2022/Lab%201/test.png)](https://youtube.com/shorts/1nGx4omL2bo)

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop three costumes so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

\*\***Include sketches of what your devices might look like here.**\*\*

![plot](https://github.com/peter2520/Interactive-Lab-Hub/blob/d98ee104c9d7490a278303887116bf41958637c6/Lab%201/Sketch.jpg)

\*\***What concerns or opportunitities are influencing the way you've designed the device to look?**\*\*

The device should be waterproof for wet garbage.
The color from our device should match the color of each recycling bins respectively so it will be easier to throw the trash.
If the device is built in a new recycling station, we can build more features. 

Ex. After detecting the items, the recycling station opens the hole of specific trash bin, so users won’t throw to the wrong recycling bins.


## Part F. Record

\*\***Take a video of your prototyped interaction.**\*\*

Storyboard (4)
[![Watch the video](https://github.com/peter2520/Interactive-Lab-Hub/blob/Fall2022/Lab%201/video_1.png)](https://youtube.com/shorts/3B4ziGFixR8)

Storyboard (5)+(6)
[![Watch the video](https://github.com/peter2520/Interactive-Lab-Hub/blob/Fall2022/Lab%201/video_2.png)](https://youtube.com/shorts/vzk2bl4GZhU)

Storyboard (7)
[![Watch the video](https://github.com/peter2520/Interactive-Lab-Hub/blob/Fall2022/Lab%201/video_3.png)](https://youtube.com/shorts/NZrWgEVi0Dg)

\*\***Please indicate anyone you collaborated with on this Lab.**\*\*
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

Thank Jonathan Tan and Alan Hsieh for helping me record the video.



# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

\*\***Summarize feedback from your partners here.**\*\*

Heuisu Judy Kim:
This is a great idea! Thinking back to the framework and scenarios, how would this work with multiple items on the "sensor"? What would the color be and would the user understand which item the light was informing?

Yi-Ru Pei:
It is a great idea. It helps us categorize trash and recycle stuff easily. And the idea of the color signs pairing with the colors on trash cans is very clear and user-friendly to users of all ages. If the designer can change the start button to a sensor one would be better since sometimes people would not wash their hands before touching the button.

Calvin Tirrell:
Good storyboard and the videos follow the storyboard well! Consider giving the phone a costume so it looks less like a phone but good job!

Samuel Willenson:
I really like the idea of this device. I think the storyboard is clear and it has a good moral goal. Maybe you can implement an audio alert along with the red light when someone throws their trash into the wrong pin. This way they have no excuse as to why they ignored the red light, and can help shame them/peer pressure into righting their wrong if other people are around.

My thoughts:
I will add some sound affect and audio alert to the device to give more instructions to the users.
Consider the sensor, I think integrate deep learning model to multiple sensors may help the sensor detect items.

## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors! Again, be creative! Feel free to fork and modify the tinkerbell code! 
3) We will be grading with an emphasis on creativity. 

\*\***Document everything here. (Particularly, we would like to see the storyboard and video, although photos of the prototype are also great.)**\*\*

## Part A. Plan 


\*\***Describe your setting, players, activity and goals here.**\*\*

_Setting:_ In the recycling station/room.

_Players:_ People who are confused about recycling.

_Activity:_ The players show their recycling/trash to the sensor of the interactive device, and the device tell the player how to throw their recycling/trash through lights of different colors.

_Goals:_ Make recycling faster and successful.


\*\***Include pictures of your storyboards here**\*\*

Initial Brainstorming 7 storyboards
1. Hiking Device: Detect users physical conditions during hiking, if emergency happens the device flash red which will let his/her friends know.
2. Recycling station: Sense the items and display the match color, so users can throw the trash to correct recycling bin.  
3. Driver Detection: If the device detect the driver is sleepy or drunk the device will flash red and remind the car behind to stay away from this car.
4. Work Detection: Working for a long period, remind users to take a rest/take a walk/drink a water.

![plot](https://github.com/peter2520/Interactive-Lab-Hub/blob/b146a29bb6d4230087c7e860679be8513b9335fb/Lab%201/Storyboard1_part1.jpg)

5. Display color to remind users the extreme weather occurs: Cold -> Blue. Hot -> Red. Storm -> Black.
6. Cooking Alarm: If the food is not ok -> display blue, ok -> display green, overcooked -> display red
7. Real time density detection in a room, station, mall. Low density -> green. Medium density -> yellow. High Density -> red. 

![plot](https://github.com/peter2520/Interactive-Lab-Hub/blob/b146a29bb6d4230087c7e860679be8513b9335fb/Lab%201/Storyboard2_part1.jpg)


After brainstorming, I decide to extend idea of the recycling station. Thus, I draw 7 storyboards for my recycling station idea.

1. Recycling/Trash on the floor, people feel confused about doing recycling.
2. The device will show instruction of how to use the device from the speaker and the touch screen.
3. Show the recycling to the sensor of the device, The device will display the color of the recycling which match to the correct recycling bin.
4. If anyone throw the recycling to the wrong bin, the device will display red and sound the alarm. If anyone throw the recycling to the correct bin, the device will display "Great" and make a "cheerful" sound effect.

![plot](https://github.com/peter2520/Interactive-Lab-Hub/blob/b146a29bb6d4230087c7e860679be8513b9335fb/Lab%201/Storyboard1_part2.jpg)

5. Display Yellow -> This item has more than one recycling type. Users need to separate them and sense again
6. If successfully recycle the trash more than a weight, the device will give cash back. Users can enter their membership information or bank account information through the touch screen.
7. After all done, The device remind users to clean their hands with sanitizer

![plot](https://github.com/peter2520/Interactive-Lab-Hub/blob/b146a29bb6d4230087c7e860679be8513b9335fb/Lab%201/Storyboard2_part2.jpg)

**Summarize feedback you got here.**

After presenting my ideas to my friend Hau Chu and Alan Hsieh, they thought the idea of recycling sensor and hiking device are the most creative ones. I think the recycling sensor is more useful for more people in daily life.
Developing prototype devices with color lights are sufficient. However, adding sounds or vibration can make the interaction/instruction more explicit in further steps.

## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

\*\***Are there things that seemed better on paper than acted out?**\*\*

The color showed on the screen show the recycling type of our detected recycling and which recycling bins should the each recycling throw in. I think storyboard can showed exactly what I assume the device work, and I can depict how the device behave in much more scenarios. On the other hand, it’s hard to act out and show every behavior I assume while some scenarios are hard to build in reality.

\*\***Are there new ideas that occur to you or your collaborators that come up from the acting?**\*\*

The new ideas that occur to me are that I can use different colored lights to indicate the users to help the device to recognize the recycling better. A recycling may have different part of recycling, so we might separate them and show the recycling to our device respectively.

## Part C. Prototype the device

\*\***Give us feedback on Tinkerbelle.**\*\*

It is easy to use in developing prototypes. Adding features like changing colors automatically by user setting may be more useful in various scenarios.

## Part D. Wizard the device

Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

\*\***Include your first attempts at recording the set-up video here.**\*\*

[![Watch the video](https://github.com/peter2520/Interactive-Lab-Hub/blob/Fall2022/Lab%201/setup.png)](https://youtube.com/shorts/uEX6nYRbGEo)


Now, change the goal within the same setting, and update the interaction with the paper prototype. 

\*\***Show the follow-up work here.**\*\*

[![Watch the video](https://github.com/peter2520/Interactive-Lab-Hub/blob/Fall2022/Lab%201/test.png)](https://youtube.com/shorts/1nGx4omL2bo)

## Part E. Costume the device


\*\***Include sketches of what your devices might look like here.**\*\*

All devices are waterproof since the garbage may be wet.

Sensor: Built-in Deep learning model, so the items can be detected correctly.

Speaker: Give instructions to the users.

Interactive screen: Display the color of sense items, so users know throw the trash to match bins. Display other 
information (Ex. "The trash bin is full!" "Total cash back" "Pleae wash your hands.")

Touch screen: Press button to sense the items. Enter bank account information for cash back service. 

Trash bins: Open the hole of match trash bin, so users can only throw the trash to that specific bin.

![plot](https://github.com/peter2520/Interactive-Lab-Hub/blob/b146a29bb6d4230087c7e860679be8513b9335fb/Lab%201/Sketch_revised.jpg)

\*\***What concerns or opportunitities are influencing the way you've designed the device to look?**\*\*

The device should be waterproof for wet garbage.
The color from our device should match the color of each recycling bins respectively so it will be easier to throw the trash.
If the device is built in a new recycling station, we can build more features. 

Ex. After detecting the items, the recycling station opens the hole of specific trash bin, so users won’t throw to the wrong recycling bins.

## Part F. Record

\*\***Take a video of your prototyped interaction.**\*\*

Show the recycling to the sensor of the device, The device show the color(green) of the recycling(Glass) which match to the correct recycling bin(green). (Storyboard (3))

[![Watch the video](https://github.com/peter2520/Interactive-Lab-Hub/blob/6284f5c1af0198ae9ed7ea690e6e33eb5bbcb475/Lab%201/video_1_part2.png)](https://youtube.com/shorts/HEuE1MrjG6s)

Display Yellow -> This item has more than one recycling type. Users need to separate them and sense again. (Storyboard (5))

[![Watch the video](https://github.com/peter2520/Interactive-Lab-Hub/blob/6284f5c1af0198ae9ed7ea690e6e33eb5bbcb475/Lab%201/video_2_part2.png)](https://youtube.com/shorts/Ndfd2ckYpXg)

If anyone throw the recycling to a wrong bin, the device display red and sound the alarm. This feature may give peer pressure to them if other people are around. (Storyboard (4))

[![Watch the video](https://github.com/peter2520/Interactive-Lab-Hub/blob/6284f5c1af0198ae9ed7ea690e6e33eb5bbcb475/Lab%201/video_3_part2.png)](https://youtube.com/shorts/dInppOFjti8)

\*\***Please indicate anyone you collaborated with on this Lab.**\*\*
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

Thank Jonathan Tan and Alan Hsieh for being the actor and assisting me record the video.
