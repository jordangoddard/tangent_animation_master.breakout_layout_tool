import bpy
import breakout_layout_tool
from bpy.app.handlers import persistent
from imp import reload
reload(breakout_layout_tool)

import time
import re


br = breakout_layout_tool.BreakOut()

try:
        file_read = open('C:\\Temp\\pass_temp.txt','r').readlines()
except:
    print("\n\nFailure\n\n")
else:
    line_one = file_read[0]
    match = re.match(r'(\d+\.\d+)', line_one)
    scene_name = match.group(1)
    line_two =  file_read[1]
    match_again = re.match("(\S+)", line_two)
    file_path = match_again.group(1)
    

def first_scene_update_callback(scene):

    # self-removal, only run once
    bpy.app.handlers.scene_update_pre.remove(first_scene_update_callback)
   
    br.lock_items()
    bpy.ops.wm.save_as_mainfile(filepath= 'T:\\Development\\tools\\breakout_layout_tool\\data\\return\\test_publish.blend')
    
    #Quit this process
    time.sleep(10)
    quit()

def _save(scene_name): #hilaire
    temp_scene_name = scene_name
    bpy.ops.wm.save_as_mainfile(filepath= 'T:\\Development\\tools\\breakout_layout_tool\\data\\return\\%s_publish.blend'%temp_scene_name) #Save file here
    
    bpy.app.handlers.load_post.append(load_post_callback) #Setting delay
    bpy.ops.wm.revert_mainfile() #Reload file
   
@persistent
def load_post_callback(dummy):

    # self-removal, so it isn't called again
    bpy.app.handlers.load_post.remove(load_post_callback)

    # use a scene update handler to delay execution of code
    bpy.app.handlers.scene_update_pre.append(first_scene_update_callback)

if __name__ == "__main__":
    br.execute()
    _save(scene_name)
    #_save()    This doesnt work but we need to save and reloade again somehow....
    
    