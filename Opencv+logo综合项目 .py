import cv2
# 1 读取len03原图,为lena
lena = cv2.imread('../images/lena03.png')
# 2 读取OpenCV-logo.png原图，为logo
logo = cv2.imread('../images/OpenCV-logo.png')
# 3. 从lena03图中提取右下角ROI
h1, w1 = lena.shape[:2]
h2, w2 = logo.shape[:2]
roi = lena[h1-h2:h1,w1-w2:w1]
cv2.imshow('roi',roi)
# 4. 把logo转为灰度图gray
gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
cv2.imshow('roi_gray',gray)
# 5. 通过二值化获取抛弃logo前图的掩码图mask1，阈值设为220,并显示
_, mask1 = cv2.threshold(gray,220,255,cv2.THRESH_BINARY)
cv2.imshow('mask1',mask1)
# 6. 通过按位与操作获得只有大图背景而logo前景挖空的局部图fig1，并显示
fig1 = cv2.bitwise_and(roi,roi,None,mask=mask1)
cv2.imshow('fig1',fig1)
# 7. 通过二值化获取保留logo前景的掩码图mask2，阈值设为220,并显示
_,mask2 = cv2.threshold(gray,220,255,cv2.THRESH_BINARY_INV)
cv2.imshow('mask2',mask2)
# 8. 通过按位与操作获得只有logo前景而背景挖空的局部图fig2，并显示
fig2 = cv2.bitwise_and(logo,logo,None,mask = mask2)
cv2.imshow('fig2',fig2)
# 9. 通过cv2.add()函数把两个局部图fig1和fig2相加，相加结果去更新ROI，并显示
roi[:] = cv2.add(fig1,fig2)
lena_new = cv2.resize(lena,(512,512))
cv2.imshow('lena_new',lena_new)
cv2.waitKey()