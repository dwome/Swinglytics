
import multiprocessing as mp


# Camera stuff
CAMERA_RESOLUTION = (1024, 768)
CAMERA_FRAMERATE = 30
ending = "h264"
CAMERA_FILENAMES = ("rpi/vid/cap1." + ending, 
             "rpi/vid/cap2." + ending,
             "rpi/vid/cap3." + ending,
             "rpi/vid/cap4." + ending)
CAMERA_FILENAMES_TS = mp.Array("d", [-1, -1, -1, -1]) 
CAMERA_CAP_LEN = 10 # how long should each capture be

CAMERA_MOTION_THRESHOLD = 60
CAMERA_MIN_NUMBER_MOTION_VECTORS = 20

CAMERA_TRIGGER_MOTION = mp.Value("d", -1) # saves a shared timestamp when the last motion detection occured

CAMERA_SETUP = 2 # 1 for PiCamera, 2 for USB Camera, and 3 for both

# Sound stuff
SOUND_THRESHOLD = 150 # how loud does the noise have to be

SOUND_TRIGGER_SOUND = mp.Value("d", -1)



# Handler stuff
HANDLER_MIN_SWING_DELAY = 1