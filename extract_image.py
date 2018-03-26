import cv2
import subprocess
import xlwt

""" Part 2 """

cmd ="ssocr -t 34 -d -1 dmm-100px.jpg"
cmd1 = "ssocr -T "
filename = "six_digits.png"
result = subprocess.Popen(cmd1+filename, shell=True,cwd="output",stdout=subprocess.PIPE)
result.wait()
tmp= result.stdout.read()
res = tmp.strip()
print res
num_images = 17
i = 0
wb = xlwt.Workbook()
ws = wb.add_sheet("My Result Sheet")
ws.write(0,0,"matrix size") # row-dynamic, col1-threads, col2-scale, col3-exec_time
#ws.write(0,1,"threads")
#ws.write(0,2,"scale")
#ws.write(0,3,"exec time in sec")

filename = "frame%d.jpg" % num_images
for k in range(1,num_images+1):
    i += 1
    filename = "frame%d.jpg" % k
    ws.write(i,0,filename)

wb.save("results/result_info.xls")

exit()
""" Part 1 """
# vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
vidcap = cv2.VideoCapture('input/meter.mp4')
fps = vidcap.get(cv2.cv.CV_CAP_PROP_FPS)

if fps <= 1:
    fps = 26
#success,image = vidcap.read()

print "Frames per second : {0}".format(fps)
count = 0
num_images = 0
success = True
while success:
    success,image = vidcap.read()
    #print 'Read a new frame: ', success
    if count % fps == 0 :
        num_images += 1
        cv2.imwrite("output/frame%d.jpg" % num_images, image)     # save frame as JPEG file
    count += 1
print "Number of Images : "+str(num_images)
vidcap.release()


