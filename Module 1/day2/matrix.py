import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=mpimg.imread("img1.jpg")  
print(type(img))
print(img.shape)
print(img.dtype,"\n","\n")

plt.imshow(img)
plt.title("Original Image")
plt.axis('off')
plt.show()

img_gray=np.mean(img,axis=2) 
print("shape of grayscale image:",img_gray.shape,"\n")

plt.imshow(img_gray,cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()



bright=img+50
bright_img=np.clip(bright,0,255)

plt.imshow(bright_img.astype(np.uint8))
plt.title("bright image")
plt.axis('off')
plt.show()

dark=img-50
dark_img=np.clip(dark,0,255) 

plt.imshow(dark_img.astype(np.uint8))
plt.title("dark image")
plt.axis('off')
plt.show()

H_flip=img[:,::-1]

plt.imshow(H_flip)
plt.title("Horizontal fliped image")
plt.axis('off')
plt.show()


V_flip=img[::-1,:]

plt.imshow(V_flip)
plt.title("Vertical fliped image")
plt.axis('off')
plt.show()

crop_img=img[100:400,50:100] 

plt.imshow(crop_img)
plt.title("cropped image")
plt.axis('off')
plt.show()

plt.figure(figsize=(15,10))

plt.subplot(2,3,1)
plt.imshow(img) 
plt.title("Original")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(img_gray,cmap="gray") 
plt.title("Gray")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(bright.astype(np.uint8)) 
plt.title("Bright")
plt.axis("off")

plt.subplot(2,3,4)
plt.imshow(dark.astype(np.uint8)) 
plt.title("Dark")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(H_flip) 
plt.title("H Flip")
plt.axis("off")

plt.subplot(2,3,6)
plt.imshow(crop_img) 
plt.title("Crop")
plt.axis("off")

plt.tight_layout()
plt.show() 



blur = (
    img[:-2, :-2] + img[1:-1, :-2] + img[2:, :-2] + ## Top-Left      Top       Top-Right
    img[:-2, 1:-1] + img[1:-1, 1:-1] + img[2:, 1:-1] + ## Left          Center    Right
      img[:-2, 2:] + img[1:-1, 2:] + img[2:, 2:] ## Bottom-Left   Bottom    Bottom-Right
) / 9

plt.imshow(blur.astype(np.uint8))
plt.title("Blur Image")
plt.axis("off")
plt.show()