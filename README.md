# coinOCR
This is work in progress attempt to create a system to document coins by reading the text off the coins by Optical Character Recognition. A handy tool for hobby numismats.

The project at its current point is divided into three parts:
1. OpenCV is used to identify all the coins from a large image of all the coins together and then save each coin's image seperately
2. The logPolar function is used to make the circular edges of the coins linear for better OCR readability.
3. Various image transformations are done on the resultant image
4. PyTesseract OCR is used to read the text from the previous step.

The first 3 steps are functioning as desired, however step 4 does not give the desired output. This is believed to be because the surface of the coins give very noisy images that the  OCR finds difficuly to read.
Futher study needs to be done to make a noise-tolerant OCR manually through LSTMs, etc.
