image logo blue = "logosolid.png"
image magic = "magic.png"

image pos:
    "target1.png"
    block:
        rotate 0
        linear 2.0 rotate 360.0
        repeat

image anchor:
    "target2.png"
    block:
        rotate 360.0
        linear 2.0 rotate 0.0
        repeat
        

#begin atl_image
image eileen animated:
    "eileen_vhappy.png"
    pause .5
    "eileen_happy.png"
    pause .5
    repeat
#end atl_image

#begin atl_image1
image eileen animated twice:
    "eileen_vhappy.png"
    pause .5
    "eileen_happy.png"
    pause .5
    repeat 2
#end atl_image1

#begin atl_image2
image eileen animated once:
    "eileen_vhappy.png"
    pause .5
    "eileen_happy.png"
#end atl_image2

#begin atl_with
image bg atl transitions:
    "bg washington" with dissolve
    pause 1.0
    "bg whitehouse" with dissolve
    pause 1.0
    repeat
#end atl_with

    
#begin atl_transform
transform topright:
    xalign 1.0 yalign 0.0
#end atl_transform
    

#begin atl_transform1
transform move_jump:
    xalign 1.0 yalign 0.0
    pause 1.0
    xalign 0.0
    pause 1.0
    repeat
#end atl_transform1

#begin atl_transform2
transform move_slide:
    xalign 1.0 yalign 0.0
    linear 3.0 xalign 0.0
    pause 1.0
    repeat
#end atl_transform2    

transform reset:
    xalign 0.5 yalign 0.5
    zoom 1.0 xzoom 1.0 yzoom 1.0
    crop None size None
    alpha 1.0
    rotate None
    
label tutorial_positions:

    e "In this tutorial, I'll teach you how Ren'Py positions things on the screen. But before that, let's learn a little bit about how Python handles numbers."

    e "There are two main kinds of numbers in Python: integers and floating point numbers. An integer consists entirely of digits, while a floating point number has a decimal point."

    e "For example, 100 is an integer, while 0.5 is a floating point number, or float for short. In this system, there are two zeros: 0 is an integer, and 0.0 is a float."

    e "Ren'Py uses integers to represent absolute coordinates, and floats to represent fractions of an area with known size."

    e "When we're positioning something, the area is usually the entire screen."

    e "Let me get out of the way, and I'll show you where some positions are."

    hide eileen
    with moveoutright
    
    show pos:
       xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
       subpixel True
       
    with dissolve
    
    show pos:
        linear .5 xpos 0.0 ypos 0.0
        
    e "The origin is the upper-left corner of the screen. That's where the x position (xpos) and the y position (ypos) are 0."

    show pos:
        ypos 0.0
        linear .5 xpos 0.5
        
    e "When we increase xpos, we move to the right. So here's an xpos of .5, meaning half the width across the screen."

    show pos:
        linear .5 xpos 1.0

    e "Increasing xpos to 1.0 moves us to the right-hand border of the screen."

    show pos:
        xpos 800
        linear .5 xpos 400

    e "We can also use an absolute xpos, which is given in an absolute number of pixels from the left side of the screen. For example, since this window is 800 pixels across, using an xpos of 400 will return the target to the center of the top row."

    e "The y-axis position, or ypos works the same way. Right now, we have a ypos of 0.0."

    show pos:
        xpos 400
        linear .5 ypos .5
    
    e "Here's a ypos of 0.5."

    show pos:
        linear .5 ypos 1.0

    e "A ypos of 1.0 specifies a position at the bottom of the screen. If you look carefully, you can see the position indicator spinning below the text window."

    e "Like xpos, ypos can also be an integer. In this case, ypos would give the total number of pixels from the top of the screen."

    show pos:
        linear .5 xpos .75 ypos .25
    

    menu:

        e "Can you guess where this position is, relative to the screen?"

        "xpos 1.0 ypos .5":

            e "Sorry, that's wrong. The xpos is .75, and the ypos is .25."

            e "In other words, it's 75%% of the way from the left side, and 25%% of the way from the top." 

        "xpos .75 ypos .25":

            e "Good job! You got that position right."

        "xpos .25 ypos .33":

            e "Sorry, that's wrong. The xpos is .75, and the ypos is .25."

            e "In other words, it's 75%% of the way from the left side, and 25%% of the way from the top." 

    hide pos

    show logo blue:
        xpos 300 ypos 100
        
    show anchor:
        xanchor 0.5 yanchor 0.5
        xpos 300 ypos 100

    with dissolve

    
    e "The second position we care about is the anchor. The anchor is a spot on the thing being positioned."

    e "For example, here we have an xanchor of 0.0 and a yanchor of 0.0. It's in the upper-left corner of the logo image."

    show anchor:
        linear .5 xpos 500
    
    e "When we increase the xanchor to 1.0, the anchor moves to the right corner of the image."

    show anchor:
        linear .5 ypos 400

    e "Similarly, when both xanchor and yanchor are 1.0, the anchor is the bottom-right corner."


    show pos:
        xanchor .5 yanchor .5
        xpos 600 ypos 400
        
    
    e "To place an image on the screen, we need both the position and the anchor."
    
    show logo blue:
        linear .5 xpos 400 ypos 100
        
    show anchor:
        linear .5 xpos 600 ypos 400
        
    e "We then line them up, so that both the position an anchor are at the same point on the screen."


    show anchor:
        linear .5 xpos 0 ypos 0
    show pos:
        linear .5 xpos 0 ypos 0
    show logo blue:
        linear .5 xpos 0 ypos 0
        
    e "When we place the both in the upper-left corner, the image moves to the upper-left corner of the screen."    

    show anchor:
        linear .5 xpos 0.5 ypos 0.5
    show pos:
        linear .5 xpos 0.5 ypos 0.5
    show logo blue:
        linear .5 xalign 0.5 yalign 0.5

    e "With the right combination of position and anchor, any place on the screen can be specified, without even knowing the size of the image."

    show logo blue:
        linear .5 yalign .3

    with None
        
    hide anchor
    hide pos
    
    with dissolve
        
    e "It's often useful to set xpos and xanchor to the same value. We call that xalign, and it gives a fractional position on the screen."

    show logo blue:
        linear .5 xalign 0.0
    
    e "For example, when we set xalign to 0.0, things are aligned to the left side of the screen."

    show logo blue:
        linear .5 xalign 1.0

    e "When we set it to 1.0, then we're aligned to the right side of the screen."
    
    show logo blue:
        linear .5 xalign .5

    e "And when we set it to 0.5, we're back to the center of the screen."

    e "Setting yalign is similar, except along the y-axis."

    e "Remember that xalign is just setting xpos and xanchor to the same value, and yalign is just setting ypos and yanchor to the same value."

    hide logo
    with dissolve
    show eileen happy
    with moveinright

    e "Once you understand positions, you can use transformations to move things around the Ren'Py screen."
    
    return

       
label tutorial_atl:

    e "While showing static images is often enough for most games, occasionally we'll want to change images, or move them around the screen."

    e "We call this a Transform, and it's what ATL, Ren'Py's Animation and Transformation Language, is for."

    # Gratuitous Rock concert.

    e "That was a lot of work, and before we can do that, we'll need to start with the basics of using ATL."

    e "There are currently three places where ATL can be used in Ren'Py."

    show example atl_image
    
    e "The first place ATL can be used is as part of an image statement. Instead of a displayable, an image may be defined as a block of ATL code."

    e "When used in this way, we have to be sure that ATL includes one or more displayables to actually show."

    show example atl_transform

    e "The second way is through the use of the transform statement. This assigns the ATL block to a python variable, allowing it to be used in at clauses and inside other transforms."

    # show example atl_show

    e "Finally, an ATL block can be used as part of a show statement, instead of the at clause."

    hide example

    e "The key to ATL is what we call composeability. ATL is made up of relatively simple commands, which can be combined together to create complicated transforms."
    
    e "Before I explain how ATL works, let me explain what animation and transformation are."

    show eileen animated:
        center
    
    e "Animation is when the displayable being shown changes. For example, right now I am changing my expression."

    show eileen happy

    show magic:
        yalign .5 subpixel True
        
        parallel:            
            xalign .5
            linear 3.0 xalign .75
            linear 6.0 xalign .25
            linear 3.0 xalign .5
            repeat

        parallel:
            alpha 1.0 zoom 1.0
            linear .75 alpha .5 zoom .9
            linear .75 alpha 1.0 zoom 1.0
            repeat

        parallel:
            rotate 0
            linear 5 rotate 360
            repeat

    with dissolve
                
    e "Transformation involves moving or distorting an image. This includes placing it on the screen, zooming it in and out, rotating it, and changing its opacity."

    hide magic
    with dissolve    

    show example atl_image
    show eileen animated
    
    e "To introduce ATL, let's start by looking at at a simple animation. Here's one that consists of five lines of ATL code, contained within an image statement."

    e "In ATL, to change a displayable, simply mention it on a line of ATL code. Here, we're switching back and forth between two images."

    e "Since we're defining an image, the first line of ATL has to name a displayable. Otherwise, there would be nothing to show."
    
    e "The second and fourth lines are pause statements, which cause ATL to wait half of a second each before continuing. That's how we give the delay between images."

    e "The final line is a repeat statement. This causes the current block of ATL to be restarted. You can only have one repeat statement per block."

    show example atl_image1
    show eileen animated twice
    
    e "If we were to write repeat 2 instead, the animation would loop twice, then stop."

    show example atl_image2
    show eileen animated once
    
    e "Omitting the repeat statement means that the animation stops once we reach the end of the block of ATL code."

    show bg atl transitions
    show example atl_with
    
    e "By default, displayables are replaced instantaneously. We can also use a with clause to give a transition between displayables."

    show bg whitehouse
    with dissolve
    
    hide example

    e "Now, let's move on to see how we can use ATL to transform an image. We'll start off by seeing what we can do to position images on the screen."

    show logo base behind eileen
    
    show logo base at topright
    with dissolve

    show example atl_transform
    
    e "Perhaps the simplest thing we can do is to position the images on the screen. This can be done by simply giving the names of the transform properties, each followed by the value."

    show example atl_transform1
    show logo base at move_jump
    
    e "With a few more statements, we can move things around on the screen."

    e "This code starts the image off at the top-right of the screen, and waits a second."

    e "It then moves it to the left side, waits another second, and repeats."

    e "The pause and repeat statements are the same statements we used in our animations. They work throughout ATL code."

    show example atl_transform2
    show logo base at move_slide

    e "Having the image jump around on the screen isn't all that useful. That's why ATL has the interpolation statement."

    e "The interpolation statement allows you to smoothly vary the value of a transform property, from an old to a new value."

    e "Here, we have an interpolation statement on the second ATL line. It starts off with the name of a time function, in this case linear."

    e "That's followed by an amount of time, in this case three seconds. It ends with a list of properties, each followed by its new value."

    e "The old value is the value of the transform property at the start of the statement. By interpolating the property over time, we can change things on the screen."
    
    hide example
    show eileen happy at right
    with move

    show logo base:
        alignaround (.5, .5)
        linear 2.0 xalign .5 yalign .5 clockwise circles 3

    e "ATL supports more complicated move types, like circle and spline motion. But I won't be showing those here."

    e "Next, let's take a look at some of the transform properties that we can change using ATL."

    show logo base at reset
    
    #begin atl_motion
    show logo base:
        xalign .3 yalign .7
        linear 1.0 xalign .7 yalign .3
        linear 1.0 xalign .3 yalign .7
        repeat    
    #end atl_motion
    with dissolve
        
    show example atl_motion
        
    e "We've already seen the position properties. Along with xalign and yalign, we also support the xpos, ypos, xanchor, and yanchor properties."

    show logo base at reset
    show example atl_zoom

    #begin atl_zoom
    show logo base:
        zoom 1.0
        linear 1.0 zoom 1.5
        linear 1.0 zoom 1.0
        repeat
    #end atl_zoom
    with dissolve

    e "The zoom property lets us scale the image by a factor, making it bigger and smaller. For best results, zoom should always be greater than 0.5."

    show logo base at reset
    show example atl_xyzoom

    #begin atl_xyzoom
    show logo base:
        xzoom .75 yzoom 1.25
        linear 1.0 xzoom 1.25 yzoom .75
        linear 1.0 xzoom .75 yzoom 1.25
        repeat
    #end atl_xyzoom
    with dissolve
    
    e "The xzoom and yzoom properties allow images to be scaled in the X and Y directions independently."

    "..."
    
    return
