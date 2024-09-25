import cv2
import os

for root, _, filename in os.walk(os.path.join(os.getcwd(), 'images')):
    for file in filename:
        img = cv2.imread(os.path.join(root, file), cv2.IMREAD_UNCHANGED)
        output = cv2.resize(img,(610,440))
        cv2.imwrite(os.path.join(root, file), output)

