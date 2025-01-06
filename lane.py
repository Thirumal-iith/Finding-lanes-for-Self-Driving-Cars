import cv2
import numpy as np
import matplotlib.pyplot as plt

def make_coordinates(image,line_parameters):
    slope,intercept=line_parameters
    y1=image.shape[0]
    y2=int(y1*(3/5))
    x1=int((y1-intercept)/slope)
    x2=int((y2-intercept)/slope)
    return np.array([x1,y1,x2,y2])

def averaged_slope_intercept(image,lines):
    left_fit=[]
    right_fit=[]
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        parameters=np.polyfit((x1,x2),(y1,y2),1)
        slope=parameters[0]
        intercept=parameters[1]
        if slope<0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    left_fit_average=np.average(left_fit,axis=0)
    right_fit_average=np.average(right_fit,axis=0)
    left_line=make_coordinates(image,left_fit_average)
    right_line=make_coordinates(image,right_fit_average)
    return np.array([left_line,right_line])

# edge detection :  identifying sharp changes in intensity in adjacent pixels
# gradient : measure of change in brightness over adjacent pixels
# strong gradient : 0---255, small gradient : 0---15
# for color image : each pixe in the image is a combination of three intensities // 3 channels : BGR
#  grayscale image : only one channel is faster than processing a three channel image

# 1)converting to Gray
# Gray=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
# 2) reduce noise by using gaussian blurr
# blur=cv2.GaussianBlur(gray,(5,5),0)
# Canny method for edge detection strong gradient indicates a deep change and small gradient indicates shallow change
# canny function does is perform a derivative on both x and y directions
#  a small derivative is small change in pixel ,large derivative is a large change in pixel
# gradient in all directions of our blurred image
# using a low high threshold ratio of one to three 1:3
# canny=cv2.Canny(blur,50,150)
def canny(image):
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    can=cv2.Canny(blur,50,150)
    return can


# displaying lines on black image
def display_lines(image,lines):
    line_image=np.zeros_like(image)
    if lines is not None:
        for x1,y1,x2,y2 in lines:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    return line_image


# 3)Region of interest
# bitwise --- and
#it takes the bitwise & of each homologous pixel in both arrays
def region_of_interest(image):
    height=image.shape[0]
    polygons=np.array([
        [(200,height),(1100,height),(550,250)]
    ])
    mask= np.zeros_like(image)
    cv2.fillPoly(mask,polygons,255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

#  HOUGH TRANSFORM
# detect straight lines in image and thus identify lane lines
# straight line y=mx+c  represent this line in parametric space which will call hough space
# m=slope change in x and y , c=intercept , this entire line can be plotted as a single point hough space
# instead of line we have a coordinates(x,y) , have a line that crosses that with m and c ,infinite amount of lines that
# can cross this point , note that : a single point in x&y(image) space is represented by a line in hough space
# whenever you see a series of points and we are told that these points are connected by some line
# there are many possible lines that can cross each point individually ,each line with diff slope and y-intercept values
# there is one line that is consistent with both points
# determine that by looking at the point of intersection in hough space(graph with "x" collide intersection)
# that point is consistent with crossing both of our points
# split our hough space into grid each bin inside of our corresponding to the slope and y-intercept
# inside of bin that it belongs to the bin with maximum number of votes thats gonna be your line

# for vertical lines
# there is a chance of change in y /change in x(slope) -->infinity
# line with cartesian coordinate system m&c well instead express it in polar coordinate system
# rho= xcostheta + ysintheta -->eqn of line in polar coordinates
# for this in hough space we get sinusoidal lines or curves--> points intersect
#threshold : minimum number of votes needed to accept a candidate line



# image=cv2.imread('test_image.jpg')
# lane_image= np.copy(image)
# canny_image=canny(lane_image)
# cropped_image=region_of_interest(canny_image)
# lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
# averaged_lines= averaged_slope_intercept(lane_image,lines)
# line_image=display_lines(lane_image,averaged_lines)
# combo_image=cv2.addWeighted(lane_image,0.8,line_image,1,1)
# cv2.imshow("result",combo_image)
# cv2.waitKey(0)

# plt.imshow(canny)
# plt.show()

cap=cv2.VideoCapture("test2.mp4")
while(cap.isOpened()):
    _,frame =cap.read()
    canny_image=canny(frame)
    cropped_image = region_of_interest(canny_image)
    lines=cv2.HoughLinesP(cropped_image,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
    averaged_lines= averaged_slope_intercept(frame,lines)
    line_image=display_lines(frame,averaged_lines)
    combo_image=cv2.addWeighted(frame,0.8,line_image,1,1)
    cv2.imshow("result",combo_image)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()