import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import imageio
import os


def textEntropyExample(text):
    """
    Calculates entropy of a string and prints.
    Based on code posted here: https://www.hdm-stuttgart.de/~maucher/Python/MMCodecs/html/basicFunctions.html

    Parameters
    ----------
    text : String
    String of text to analyse

    Returns
    -------
    """
    text="""In agreeing to settle a case brought by 38 states involving the project, the search company for the first time is required to aggressively police its own employees on privacy issues and to explicitly tell the public how to fend off privacy violations like this one."""
    chars=list(text)
    length=len(chars)
    print "Number of characters in text string: %d"%(length)
    dec=[ord(c) for c in chars]
    decset=set(dec)
    freqdic={}
    for c in decset:
        freqdic[c]=dec.count(c)

    print "\nAscii \t Char \t Count \t inform."
    Entropy=0
    for c in decset:
        prop=freqdic[c]/(1.0*length) #propability of character
        informationContent=np.log2(1.0/prop) #infromation content of character
        Entropy+=prop*informationContent
        print "%5d \t %5s \t %5d \t %2.2f" %(c, chr(c),freqdic[c],informationContent)

    print "\nEntropy of text: %2.2f"%(Entropy)


def entropy(signal):
    """
    Returns entropy of a 1-D array 'signal'
    Based on code posted here: https://www.hdm-stuttgart.de/~maucher/Python/MMCodecs/html/basicFunctions.html

    Parameters
    ----------
    signal : 1-D numpy array

    Returns
    -------
    Entropy of signal array
    """
    lensig = signal.size
    symset = list(set(signal))
    numsym = len(symset)
    propab = [np.size(signal[signal == i]) / (1.0 * lensig) for i in symset]
    ent = np.sum([p * np.log2(1.0 / p) for p in propab])
    return ent


def imageEntropy(file):
    """
    Returns entropy of a 1-D array 'signal'
    Based on code posted here: https://www.hdm-stuttgart.de/~maucher/Python/MMCodecs/html/basicFunctions.html

    Parameters
    ----------
    signal : 1-D numpy array

    Returns
    -------
    Entropy of signal array
    """
    image = Image.open(file)
    # image is copied and converted to greyscale
    # the original and greyscale image are converted to numpy arrays
    greyIm = image.convert('L')
    image = np.array(image)
    greyIm = np.array(greyIm)

    # N is the size of the region within which the entropy will be calculated
    # N=5 the region contains 10*10=100 pixel-values
    N = 5
    # The region is extracted and flattened into a 1-D numpy array
    # This region array is passed to the entropy function and inserted into entropy array
    S = greyIm.shape
    entropyArray = np.array(greyIm)
    for row in range(S[0]):
        for col in range(S[1]):
            Lx = np.max([0, col - N])
            Ux = np.min([S[1], col + N])
            Ly = np.max([0, row - N])
            Uy = np.min([S[0], row + N])
            region = greyIm[Ly:Uy, Lx:Ux].flatten()
            entropyArray[row, col] = entropy(region)

    # The original image and the greyscale image are plotted and displayed
    plt.subplot(1, 3, 1)
    plt.imshow(image)

    plt.subplot(1, 3, 2)
    plt.imshow(greyIm, cmap=plt.cm.gray)

    plt.subplot(1, 3, 3)
    plt.imshow(entropyArray, cmap=plt.cm.jet)
    plt.xlabel('Entropy in 10x10 neighbourhood')
    plt.colorbar()

    plt.savefig(file +"FIG.png")
    plt.clf()


def imageEntropyGif(gifFile):

    image = Image.open(gifFile)
    results = []
    try:
        while 1:
            image.seek(image.tell() + 1)
            frameNumber = image.tell()
            # image is copied and converted to greyscale
            # the original and greyscale image are converted to numpy arrays
            greyIm = image.convert('L')
            im = np.array(image)
            greyIm = np.array(greyIm)

            # N is the size of the region within which the entropy will be calculated
            # N=5 the region contains 10*10=100 pixel-values
            N = 5
            # The region is extracted and flattened into a 1-D numpy array
            # This region array is passed to the entropy function and inserted into entropy array
            S = greyIm.shape
            entropyArray = np.array(greyIm)
            for row in range(S[0]):
                for col in range(S[1]):
                    Lx = np.max([0, col - N])
                    Ux = np.min([S[1], col + N])
                    Ly = np.max([0, row - N])
                    Uy = np.min([S[0], row + N])
                    region = greyIm[Ly:Uy, Lx:Ux].flatten()
                    entropyArray[row, col] = entropy(region)

            # The original image and the greyscale image are plotted and displayed
            plt.subplot(1, 3, 1)
            plt.imshow(im)

            plt.subplot(1, 3, 2)
            plt.imshow(greyIm, cmap=plt.cm.gray)

            plt.subplot(1, 3, 3)
            plt.imshow(entropyArray, cmap=plt.cm.jet)
            plt.xlabel('Entropy in 10x10 neighbourhood')
            plt.colorbar()

            frame = str(frameNumber).zfill(3)
            plt.savefig(str(frame) + ".png")
            plt.clf()
    except EOFError:
        pass  # end of sequence


def createGif():
    file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.png'))) #sort files
    print file_names
    with imageio.get_writer('newGif.gif', mode='I', duration=0.05) as writer:
        for filename in file_names:
            image = imageio.imread(filename)
            writer.append_data(image)
    writer.close()

# imageEntropyGif("/Users/Sarah/Desktop/imageProcessing/venv/images/forest.gif")
# imageEntropy("/Users/Sarah/Desktop/imageProcessing/venv/images/forest.jpg")
# imageEntropy("/Users/Sarah/Desktop/imageProcessing/venv/images/urban.jpg")


createGif()


