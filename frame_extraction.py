import os

def mkdir_ifnotexists(dir):
    if os.path.exists(dir):
        return
    os.mkdir(dir)

vid_file = '/home/sdastani/projects/rrg-ebrahimi/sdastani/flownet2-pytorch/flownet2pytorch/video.mp4'
frame_pth = '/home/sdastani/projects/rrg-ebrahimi/sdastani/flownet2-pytorch/flownet2pytorch/frames'

mkdir_ifnotexists(frame_pth)
cmd = "ffmpeg -i %s -start_number 0 -vsync 0 %s/frame_%%06d.png" % (
            vid_file,
            frame_pth,
        )
os.system(cmd)