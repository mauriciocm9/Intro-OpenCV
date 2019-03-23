from canny import *


def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
            
    return line_image


img = cv2.imread('lanes.jpg')
edges = canny(img)
lines = cv2.HoughLinesP(edges, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
line_image = display_lines(img, lines)
w_lines = cv2.addWeighted(img, 0.8, line_image, 1, 1)
cv2.imshow('Hough', w_lines)
cv2.waitKey(0)
cv2.destroyAllWindows()
