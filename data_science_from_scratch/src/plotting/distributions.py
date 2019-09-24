# standard libraries
import math

# non-standard libraries
import matplotlib.pyplot as plt


def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    """Calculates the probability distribution function for the normal distribution
    """
    
    return ( math.exp( -(x-mu)**2 / 2 / sigma**2) / (math.sqrt(2* math.pi)* sigma) )

def main():

    xs = [x / 10.0 for x in range(-50,50)]
    #fig, ax = plt.subplots()
    #ax.plot(xs, normal)
    plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
    plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
    plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
    plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
    plt.legend()
    plt.title("Various Normal pdfs")
    plt.savefig("normal_pdf.png")
    plt.show()



if __name__ == "__main__": main()


    

    # for some reason these won't plot for me... phew... one of those days... lol
    # update: I came back and figured it out. small mistake, but I wanted to leave the comment above because it cracks me up :) 