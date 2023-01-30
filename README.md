# ImageFilters

ImageFilters is a small Python script that utilizes the Python Imaging Library to apply filters to images. 

Every filter can be applied individually using arguments when running the program, and each one was programmed without using pre-existing functions from libraries, other than PIL to load the image pixel data.

### Using the program

To get started, run the script with your python installation by typing `python imageFilters.py`. This will show a help menu with a list of the usable filters.

To apply filters to an image, run the program with your image argument and then filters. Multiple filters can be used at once.  `python imageFilters.py <filename> 'filter()' 'filter()'`. 

The filter arguments must have apostrophes `'` or quotation marks `"` around them, and be closed with paretheses `()` at the end, with a value if necessary.

For example, to invert the included bird.jpg and then apply noise with a value of 50 to the result, you could type `python imageFilters.py bird.jpg 'invert()' 'noise(50)'`.

Files are output next to the original input file, and will named `<filename>_edit.<extension>`. So for the bird.jpg example, the output would be called bird_edit.jpg.

### Filters (* represents optional argument)

`grayscale()`: Converts the image to grayscale, removing all color.

`invert()`: Inverts the colors of the image.

`contrast(ratio)`: Changes the contrast of the image, using the contrast ratio given. 1 is default contrast ratio. Values above 1 are more contrast, values below 1 are less contrast.

`noise(amount)`: Puts random noise grain pattern on the image. 0 is no extra noise, and a value of 1000 would make the image almost purely noise. A value of about 50 gives the image noticable noise while still leaving the image clear to see.

`pixelize(size)`: Pixelizes the image into `size x size` chunks. A value of 20 would turn the image into a pixelized image with each new "pixel" being a 20x20 block of the original image. If the pixel size doesn't perfectly factor into the image resolution, the extra bit will be cropped off. 

`edgeDetect(threshold, *pxldif)`: This uses a basic edge detection algorithm that uses a grayscale version of your image to find color differences above a given threshold. Typically values for `threshold` yield best results between 10 and 80 depending on the image. `pxldif` is an optional argument that changes which pixels are looked at to calculate the threshold. By default this is 1 as it looks for the nearest neighboring pixel, but values of 2 or 3 will look at pixels slightly farther away.

`colorEdgeDetect(threshold, *pxldif, *debug): This uses a slightly more advanced edge detection algorithm which utilizes colors. It may give better results in certain cases where images are very colorful. `threshold` and `pxldif` are similar to the ones used in edgeDetect() above. `debug` is an optional argument that by default is 0 (disabled), but if set to 1 will highlight the corresponding colors that it found to be different. This means that instead of the edge detected image being fully black and white, there will be some colors in certain areas where colored edges were found. 

`deepfry()`: Deepfry takes whatever pixel color is highest and maxes it out. This results in the result image being entirely made of bright red, green, and blue pixels. Deepfry isn't really meant to be a useful setting.
