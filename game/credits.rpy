label credits:
    if not _in_replay:
        return
    $ quick_menu = False
    $ renpy.music.play(audio.happy, loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    $ credits_speed = 100
    scene black
    with dissolve
    show cred at Move((0.5, 1.0), (0.5, -17.0), credits_speed, repeat=False, bounce=False, xanchor=0.5, yanchor=0)
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return
    
init python:
    gui.credits = _p("""
{u}Story & Directed by:{/u}

Jun


{u}Project Manager:{/u}

Toffee


{u}Character Art:{/u}

Magukappu


{u}CG Art:{/u}

Magukappu


{u}Background Art:{/u}

ForD Nguyen/Baridel 


{u}UI Designer:{/u}

Baridel 


{u}Graphic Designer:{/u}

Riscent 


{u}Logo Designer:{/u}

Flynn


{u}Music/SFX Designer:{/u}

Belgerum


{u}Editor:{/u}

HGLt


{u}Programmer:{/u}

Proxyz


{u}Trailer Creator:{/u}

KokutouTapioca


{u}Play Tester:{/u}

Fox Sol Fricchione-Piery


{b}Special Thanks to our Kickstarter Backers:{/b}


{u}Executive Producer:{/u}

Issa Kabeer


{u}Producer:{/u}

Raze 

Grishster

Vulcan64


{u}Class President:{/u}

Jonathan Gutierrez


{u}Class Representative:{/u}

XYZ

Martin Pham

Matt Amatsu

Tyler Hussey

Shaun Donovan

Even Siverts Nybø

Tom

Sean Mercado

tenjoukai

Ben 

Jacob Copeland

Xavier

Marshall Perry Graham

Tony Luong

Brad Pavlacka

Jonathan P.

Kyle

Ramon Gonzalez

Halcyonic

Ahmed j alomar

David Austin Vick

CATALYS7

Dinasis

DJ GOLD3N 5HORT

Vectimus Prime

Ondrej Hybler

Matt

JaxTH

Heathcliffe Meler

Matt Grew

Dr Depravity

Shadwell

Savvy

Brad Boivin

Ross

Hipes

Brian Wan

Jashan

Paul A Foster

Earl Zimmerman

Edward Drummond

Stephanie Teunissen

Kevin Alive

dan

Dabes115

TheEndingNight

Reapersandapples

darrian gonzales

Gerald R. Peterson

Pettifogger

Joshua Plair

Kramer


{u}Popular Student:{/u}

Onion-Knight

zeghyu

RocK_M

Peter O'Neill

mattrack

TheLivingFro

gourry6

Christopher Holgate

J Playtis

Takane Shijou

Rhez

Freyjadour

EnigmaMerc

Sean Powers

Evan Harris

Juztify

donovan20055

MP

Crimson Jager

Daniel Isidro

Matthew Hyde

Neo

Michael Howell

Just Cruising By

Steven Lord

robert simms

Gregory Bevens

Andrew Tuesley

Mike C

Boyd Outlaw

MadChemist19

criptych

vsampedro

Sean Mullaney

James Hindman

Michael Hurdle

Michael Whitehead

Gregory

Deimos

Gerald

Brahim Benjamin

Jason Sherman

Ray

Matthew Buckley

kasper nieslen

John Walker

Frank Avila

Eric Tsai

Mauricio Adolphson

Negdopkill

Alan Daniel Ramirez

Felix Rosenberger

Lamberto

garkham

Brendan Barton

Stephen Patrick

Skandranna

Chamaemelum

oliver


{u}Art Student:{/u}

Poseidon

Jason Hopkins

WM-R

Alexander Schwegler

Kyle Tot

mystady.com

sonicny

Jason F

Ernesto Prieto Jr

Gilberto Rodriguez

Leonardo ortega

Dale Brown

Scott Hannah

Xanrus

Michael Brookbank

joshua cremosnik

Robert

Herr von Stein

Ronnie Borgquist

Muhammad Afiq Bin Salleh

Chris Vannarath

VGNomad

Cronosus

Niklas Wilcox

Luke Nambi

Molino Jean-Michel

Eero Leinonen

YangNerd

Thomas

Jahmel Gordon

Austin


{u}Special Thanks to our Beta Tester:{/u}

Issa Kabeer

Raze 

Grishster

Vulcan64

Jonathan Gutierrez

XYZ

Martin Pham

Matt Amatsu

Tyler Hussey

Shaun Donovan

Even Siverts Nybø

Tom

Sean Mercado

tenjoukai

Ben 

Jacob Copeland

Xavier

Marshall Perry Graham

Tony Luong

Brad Pavlacka

Jonathan P.

Kyle

Ramon Gonzalez

Halcyonic

Ahmed j alomar

David Austin Vick

CATALYS7

Dinasis

DJ GOLD3N 5HORT

Vectimus Prime

Ondrej Hybler

Matt

JaxTH

Heathcliffe Meler

Matt Grew

Dr Depravity

Shadwell

Savvy

Brad Boivin

Ross

Hipes

Brian Wan

Jashan

Paul A Foster

Earl Zimmerman

Edward Drummond

Stephanie Teunissen

Kevin Alive

dan

Dabes115

TheEndingNight

Reapersandapples

darrian gonzales

Gerald R. Peterson

Pettifogger

Joshua Plair

Kramer


{b}Special Thanks to the following brand:{/b}

Plexstorm

Kickstarter

itch.io


©2019 PUSH!. All Rights Reserved.
""")
    
init:
    image cred = Text(gui.credits, text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)