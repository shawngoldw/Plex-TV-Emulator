# MOST IMPORTANT NOTE: BEFORE WRITING A CHANNEL, THERE MUST ALREADY BE A URL SERVICE FOR THE VIDEOS ON THE WEBSITE
# YOU WANT TO CREATE A CHANNEL FOR OR YOU WILL HAVE TO WRITE A URL SERVICE BEFORE YOU CAN WRITE THE CHANNEL. TO
# SEE IF A URL SERVICE ALREADY EXISTS, CHECK THE SERVICES BUNDLE IN THE PLEX PLUGIN FOLDER

# IMPORTANT NOTE: PYTHON IS VERY SENSITIVE TO PROPER INDENTIONS.  IF YOUR CHANNEL HAS IMPROPER INDENTIONS IT WILL
# NOT BE RECOGNIZED BY PLEX. I RUN THE PROGRAM THROUGH A CHECK MODULE ON A LOCAL VERSION OF PYTHON I HAVE LOADED
# PRIOR TO ACCESSING IT THROUGH PLEX TO MAKE SURE THERE ARE NO INDENTION ERRORS.

# You will need to decide how you want to set up your channel. If you want to have just one page that list all 
# the videos or if you want to break these videos down into subsections for different types of videos, individual shows, season, etc
# It is easiest to determine this system based on the structure of the website you are accessing. 

# You can hard code these choice in or pull the data from a web page or JSON data file and put it in a for loop to 
# automate the process. I created a basic example in the form of functions below to show the most common methods of 
# parsing data from different types of websites. When you want to produce results to the screen and have subpage come up # when they click on those results, you usually will use a
# DirectoryObject and include the name of the next function that will create that subpage called in the key.
# The key callback section sends your data to the next function that you will use to produce your next subpage.  Usually
# you will pass the value of the url onto your next function, but there are many attributes that can be sent.  It is good 
# to pass the title as well so it shows up at the top of the screen. Refer to the Framework Documentation to see the full
# list

# You will need a good working knowledge of xpath the parse the data properly.  Good sources for information related to 
# xpath are:
# 'http://devblog.plexapp.com/2012/11/14/xpath-for-channels-the-good-the-bad-and-the-fugly/'
# 'http://forums.plexapp.com/index.php/topic/49086-xpath-coding/'

# Here is a good article about working with Chrome Development Tools: 
# 'http://devblog.plexapp.com/2012/09/27/using-chromes-built-in-debugger-for-channel-development/'

# And here are a few pages that give you some pointers ON figuring out the basics of creating a channel
# 'http://devblog.plexapp.com/2011/11/16/a-beginners-guide-to-v2-1/'
# 'http://forums.plexapp.com/index.php/topic/28084-plex-plugin-development-walkthrough/'

# The title of your channel should be unique and as explanatory as possible.  The preifx is used for the channel
# store and shows you where the channel is executed in the log files

TITLE    = 'Channel Title'
PREFIX   = '/video/TVEmulator'

# The images below are the default graphic for your channel and should be saved or located in you Resources folder
# The art and icon should be a certain size for channel submission. The graphics should be good quality and not be blurry
# or pixelated. Icons must be 512x512 PNG files and be named, icon-default.png. The art must be 1280x720 JPG files and be
# named, art-default.jpg. The art shows up in the background of the PMC Client, so you want to make sure image you choose 
# is not too busy or distracting.  I tested out a few in PMC to figure out which one looked best.

ART      = 'art-default.jpg'
ICON     = 'icon-default.png'


###################################################################################################
# This (optional) function is initially called by the PMS framework to initialize the plug-in. This includes setting up
# the Plug-in static instance along with the displayed artwork. These setting below are pretty standard
# You first set up the containers and default for all possible objects.  You will probably mostly use Directory Objects
# and Videos Objects. But many of the other objects give you added entry fields you may want to use and set default thumb
# and art for. For a full list of objects and their parameters, refer to the Framework Documentation.
  
def Start():

# There are  few commands you may see appear in this section that are no longer needed.  Below is an explanation of them
# provided from a very helpful channel designer who was nice enough to explain their purpose to me:
#    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")
# This a left-over from when plugins had more control over how the contents were displayed. ViewGroups were defined to 
# tell the client how to display the contents of the directory. Now, most (if not all) clients have a fairly rigid model
# for what types of content get display in which way. Generally, it is best to remove it from a plugins when since it
# gets ignored anyways. 
#
#    HTTP.CacheTime = CACHE_1HOUR
# This setting a global cache time for all HTTP requests made by the plugin. This over-rides the framework's default 
# cache period which,
# I don't remember off the top of my head. It is entirely optional, but if you're going to use it, the idea is to pick a 
# cache-time that is reasonable. Ie. store data for a long enough time that you can realistically reduce the load on
# external servers as well as speed up the load-time for HTTP-requests, but not so long that changes/additions are not
# caught in a reasonable time frame. IMO, unless you specifically want/need a specific cache-length, I would remove that
# line and allow the framework to manage the cache with its default settings.
#
#   HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:18.0) Gecko/20100101 Firefox/18.0'
# This assigning a specific User-Agent header for all HTTP requests made by the plugin. Generally speaking, each time a
# plugin is started, a user-agent is randomly selected from a list to be used for all HTTP requests. In some cases, a
# plugin will perform better using a specific user-agent instead of a randomly assigned one. For example, some websites
# return different data for Safari on an iPad, then what they return for Chrome or Firefox on a PC. Again, if you don't
# have a specific need to set a specific user-agent, I would remove that code from your channel.

# You set up the default attributes for all you object containers and objects.  You will probably mostly use Directory
# Objects and Videos Objects but many of the other objects give you added entry fields you may want to use.  For a full 
# list of objects and their parameters, refer to the Framework Documentation.

# Important Note: (R stands for Resources folder) to tell the channel where these images are located.

  ObjectContainer.title1 = TITLE
  ObjectContainer.art = R(ART)


###################################################################################################
# This tells Plex how to list you in the available channels and what type of channels this is 
@handler(PREFIX, TITLE, art=ART, thumb=ICON)

# This function is the first and main menu for you channel.

 
def MainMenu():

# You have to open an object container to produce the icons you want to appear on this page. 
  oc = ObjectContainer()

  return oc