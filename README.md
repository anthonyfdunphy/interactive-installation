# TouchDesigner Project - Interactive Installation

<p align="center">
  <img src="https://i.imgur.com/ndP9gsL.jpg" width=100%> 
</p>

The interactive installation is a dynamic, immersive experience that combines movement, light, and sound. The installation features a series of platforms equipped with sensors that respond to audience movements by triggering a variety of sound and light effects. During the installation, visitors use sensors to control the sound of the organ and make the church ring. In the concert, the three live musicians take up the organ sound and develop an expansive, immersive sound experience in many variations with the special mixture of guitar, organ, clarinet and electronics.

<p align="center">
  <img src="https://i.imgur.com/KbgPCPz.jpg" width=50%> 
</p>

# Key Concepts 

### MIDI Communication
<div align="center">
  <video src="https://user-images.githubusercontent.com/93882580/231468636-9ad7fb56-0740-45aa-a0b9-ae544de05454.mp4" width="400" />
</div>
<br>
One of the most important features of TouchDesigner show file is the ability to automate the show's running order. This means that once the show is set up and running, it can run smoothly without any intervention. This is achieved by using the MIDI trigger notes in the Ableton session, which are mapped to functions and actions within TouchDesigner. This allows the show to be fully controlled and executed through the MIDI track, freeing up the performer to focus on other aspects of the production. This allows a certain level of flexibility for this production as much of the musical sections are freeflowing and expansive with some not clearly defined start and end points. This allows the performer/ableton operator the ability to jump around the Ableton session file without worrying about the context. The lighting scene transitions and strobe effects changes are achieved by using specific MIDI notes that are triggered at key points in the show. These notes are mapped to lighting cues within TouchDesigner, which then triggers the corresponding lighting effects. This not only creates a visually stunning show, but also ensures that the transitions between scenes are smooth and seamless.

### TD Ableton Component

The TouchDesigner session communications between Ableton and TouchDesigner with the TDAbleton component. This is achieved through the use of TD Ableton components, which enable the two software applications to communicate with each other in real-time. This allows the installation section of the show to be run through TouchDesigner, while still maintaining communication with Ableton. Using the TDAbleton component, it allow for extracting audio levels from the guitar and the clarinet which are then used to effect the light levels within various lighting scenes throughout the show which gives an overall more dynamic and immersive experience. Detection of MIDI note changes withing the Ableton session are tracked using a CHOP Execute within the TD Ableton component. Created was a dictionary in called note_to_index. note_to_index is a dictionary in Python. It maps integer keys to tuple values, where each tuple contains two elements: an integer index and a string name (or None if no name is available). When MIDI note 25 is played, a function is called which resets the fade, initalizes it and resets the index of the SWITCH CHOP to the first input to allow it to run again. This function is called twice within the show. A start function is called in both the installation and concert CHOP Execute to switch the "concert installation" switch CHOP depending on which part is running. The code structure for the CHOP Execute for the installation section is quite similar


<details>
  <summary>Expand code for concert</summary>
  

  ### CHOP Execute to change lighting scene in Switch CHOP (Concert)
  ```

def kneeplay():
	#this code is for initalizing the keeplay II scene and fading it as it starts
	parent(2).op('KNEEPLAY_II/fade_up').par.start.pulse()
	parent(2).op('KNEEPLAY_II/fade_up_scene_2').par.initialize.pulse()
	parent(2).op('KNEEPLAY_II/switch_scene').par.index = 0
	return
  
def start():
	parent(2).op('concert_installation').par.index = 0
	return

#midi notes associated with index values
note_to_index = {
	24: (0, None),
	25: (1, kneeplay),
	26: (2, None),
    27: (3, None),
    28: (4, None),
    29: (5, None),
    30: (6, None),
    31: (7, None),
    32: (8, None),
    33: (9, None),
    34: (10, None),
    35: (11, kneeplay),
    36: (12, None)
}

def onOffToOn(channel, sampleIndex, val, prev):
	if channel.name in [f"midi/t51/TdaMIDI/ch1/note_{note}" for note in note_to_index.keys()]:
		#midi note playing currently
		note_num = int(channel.name.split("_")[-1])
		
		#changes index value on lighting switch
		parent(2).op('concert_switcher').par.index = note_to_index[note_num][0]
		
		if note_to_index[note_num][1] is not None:
			#calls function in tuple
			note_to_index[note_num][1]()
	return


```
</details>


<details>
  <summary>Expand code for installation</summary>
  

  ### CHOP Execute to change lighting scene in Switch CHOP (Installation)
  ```
def start():
	parent(2).op('concert_installation').par.index = 1
	return

note_to_index = {
	54: (0, start),
	57: (1, None),
	56: (2, None),
	55: (3, None),
	58: (4, None),
}

def onOffToOn(channel, sampleIndex, val, prev):
	parent(2).op('TRANSITION_1/GO_BUTTON').click()
	
	if channel.name in [f"midi/t52/TdaMIDI/ch1/note_{note}" for note in note_to_index.keys()]:
		#midi note playing currently
		note_num = int(channel.name.split("_")[-1])
		
		#changes index value on lighting switch for the installation
		parent(2).op('switch_installation').par.index = note_to_index[note_num][0]
		
		if note_to_index[note_num][1] is not None:
			#calls function in tuple
			note_to_index[note_num][1]()
	return
  
```
</details>

# Berlin Shows and Installation
Kaiser Wilhelm Memorial Church             |  Zehlendorf
:-------------------------:|:-------------------------:
![](https://i.imgur.com/fdjwiAc.jpg)  |  ![](https://i.imgur.com/o3e63ed.jpg)
