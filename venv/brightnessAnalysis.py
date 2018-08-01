import math
from PIL import Image
from PIL import ImageStat
from PIL import ImageSequence
from PIL import GifImagePlugin

forestImage = Image.open("images/forest.jpg")
urbanImage = Image.open("images/urban.jpg")

blackImage = Image.open("images/black.jpg")
whiteImage = Image.open("images/white.jpg")

"""
        ================
        IMAGE BRIGHTNESS
        ================
"""
def averagePixelBrightness(image):
    """
    Converts image to greyscale, return average pixel brightness.
    Based on code posted here: https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python

    Parameters
    ----------
    image : Image

    Returns
    -------
        Average pixel brightness.
    """
    im = image.convert('L')
    stat = ImageStat.Stat(im)
    return stat.mean[0]


def RMSPixelBrightness(image):
    """
    Converts image to greyscale, return root-mean-square pixel brightness.
    Based on code posted here: https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python

    Parameters
    ----------
    image : Image

    Returns
    -------
        Root-mean-square pixel brightness.
    """
    im = image.convert('L')
    stat = ImageStat.Stat(im)
    return stat.rms[0]


def perceivedBrightnessRMS(image):
    """
    Averages pixels, then transforms to "perceived brightness".
    Based on code posted here: https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python

    Parameters
    ----------
    image : Image

    Returns
    -------
        Perceived brightness.
    """
    im = image
    stat = ImageStat.Stat(im)
    r, g, b = stat.mean

    return math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2))


def perceivedBrightnessAverage(image):
    """
    Finds root-mean-squared of pixels, then transforms to "perceived brightness".
    Based on code posted here: https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python

    Parameters
    ----------
    image : Image

    Returns
    -------
        Perceived brightness.
   """
    im = image
    stat = ImageStat.Stat(im)
    r, g, b = stat.rms
    return math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2))


def brightness(image):
    """
    Calculates "perceived brightness" of pixels, then returns average.
    Based on code posted here: https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python

    Parameters
    ----------
    image : Image

    Returns
    -------
        Average perceived brightness of pixels.
   """
    im = image
    stat = ImageStat.Stat(im)
    gs = (math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2))
          for r, g, b in im.getdata())
    return sum(gs) / stat.count[0]


def printImageBrightness(image):
    """
     Prints image brightness calculations for a given image using the functions from the
     code posted here: https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python

     Parameters
     ----------
     image : Image
    """
    print "***IMAGE BRIGHTNESS***"
    print "Average Pixel Brightness : {0}".format(averagePixelBrightness(image))
    print "RMS Pixel Brightness : {0}".format(RMSPixelBrightness(image))
    print "Perceived Brightness RMS : {0}".format(perceivedBrightnessRMS(image))
    print "Perceived Brightness Average : {0}".format(perceivedBrightnessAverage(image))
    print "Perceived Brightness of pixels, averaged : {0}".format(brightness(image))

    print ""


"""
        =========================
        IMAGE SEQUENCE BRIGHTNESS
        =========================
"""
def gifAveragePixelBrightness(gifFile):
    """
    Converts sequence of images to greyscale, return average pixel brightness of each frame.
    Based on code posted here: https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python

    Parameters
    ----------
     gifFile : String
         Location of file to analyse.

    Returns
    -------
         Array of average pixel brightness of each frame of the gif.
    """
    im = Image.open(gifFile)
    results = []
    try:
        while 1:
            im.seek(im.tell() + 1)
            image = im.convert('L')
            stat = ImageStat.Stat(image)
            results.append(stat.mean[0])
    except EOFError:
        pass  # end of sequence
    return results


def gifRMSPixelBrightness(gifFile):
    """
    Converts sequence of images to greyscale, return root-mean-square pixel brightness of each frame.
    Based on code posted here: https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python

    Parameters
    ----------
     gifFile : String
         Location of file to analyse.

    Returns
    -------
         Array of root-mean-square pixel brightness of each frame of the gif.
    """
    im = Image.open(gifFile)
    results = []
    try:
        while 1:
            im.seek(im.tell() + 1)
            image = im.convert('L')
            stat = ImageStat.Stat(image)
            results.append(stat.rms[0])
    except EOFError:
        pass  # end of sequence
    return results


def gifPerceivedBrightnessRMS(gifFile):
    """
    Averages pixels of each frame of a gif, then transforms to "perceived brightness".
    Based on code posted here: https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python

     Parameters
     ----------
     gifFile : String
         Location of file to analyse.

    Returns
    -------
        Array of perceived brightness of each frame of the gif.

    """
    im = Image.open(gifFile)
    results = []
    try:
        while 1:
            im.seek(im.tell() + 1)
            image = im.convert('RGB')
            stat = ImageStat.Stat(image)
            r, g, b = stat.mean
            results.append(math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2)))
    except EOFError:
        pass  # end of sequence
    return results


def gifperceivedBrightnessAverage(gifFile):
    """
    Finds root-mean-squared of pixels of each frame of a gif, then transforms to "perceived brightness".
    Based on code posted here: https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python

    Parameters
    ----------
     gifFile : String
         Location of file to analyse.

    Returns
    -------
        Array of perceived brightness of each frame of the gif.
   """
    im = Image.open(gifFile)
    results = []
    try:
        while 1:
            im.seek(im.tell() + 1)
            image = im.convert('RGB')
            stat = ImageStat.Stat(image)
            r, g, b = stat.rms
            results.append(math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2)))
    except EOFError:
        pass  # end of sequence
    return results


def gifBrightness(gifFile):
    """
    Calculates "perceived brightness" of pixels in each frame of a gif, then returns average.
    Based on code posted here: https://stackoverflow.com/questions/3490727/what-are-some-methods-to-analyze-image-brightness-using-python

    Parameters
    ----------
    gifFile : String
         Location of file to analyse.

    Returns
    -------
        Average perceived brightness of pixels of each frame of the gif.
   """
    im = Image.open(gifFile)
    results = []
    try:
        while 1:
            im.seek(im.tell() + 1)
            image = im.convert('RGB')
            stat = ImageStat.Stat(image)
            gs = (math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2))
                  for r, g, b in image.getdata())
            results.append(sum(gs) / stat.count[0])
    except EOFError:
        pass  # end of sequence
    return results


def gifPrintBrightness(brightnessArray):
    for value in brightnessArray:
        print value




def main():

    print "All black test image"
    printImageBrightness(blackImage)
    print "All white test image"
    printImageBrightness(whiteImage)
    print "Forest image"
    printImageBrightness(forestImage)
    print "Urban image"
    printImageBrightness(urbanImage)

    #
    # print "*************************"
    # gifPrintBrightness(gifAveragePixelBrightness("images/forest.gif"))
    # print "*************************"
    # gifPrintBrightness(gifRMSPixelBrightness("images/forest.gif"))
    # print "*************************"
    # gifPrintBrightness(gifperceivedBrightnessAverage("images/forest.gif"))
    # print "*************************"
    # gifPrintBrightness(gifPerceivedBrightnessRMS("images/forest.gif"))
    # print "*************************"
    # gifPrintBrightness(gifBrightness("images/forest.gif"))
    #

    #
    # print "*************************"
    # gifPrintBrightness(gifAveragePixelBrightness("images/urban.gif"))
    # print "*************************"
    # gifPrintBrightness(gifRMSPixelBrightness("images/urban.gif"))
    # print "*************************"
    # gifPrintBrightness(gifperceivedBrightnessAverage("images/urban.gif"))
    # print "*************************"
    # gifPrintBrightness(gifPerceivedBrightnessRMS("images/urban.gif"))
    # print "*************************"
    # gifPrintBrightness(gifBrightness("images/urban.gif"))

main()
