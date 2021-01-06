import matplotlib.pyplot as plot
import numpy as np
from scipy.fft import fft


class SquareFourier(object):
    def __init__(self):
        self.t = np.arange(0, 2 * np.pi, 0.001)
        self.y = [-1] * (len(self.t) // 2) + [1] * (len(self.t) // 2)
        self.yf = fft(self.y)
        self.freqs = np.fft.fftfreq(len(self.t), 0.001)
        self.recomb = np.zeros((len(self.t),))
        self.N = len(self.t)
        plot.ion()

    def equation(self, i):
        real_part = self.yf[i].real * np.cos(self.freqs[i] * 2 * np.pi * self.t)
        imag_part = self.yf[i].imag * np.sin(self.freqs[i] * 2 * np.pi * self.t)
        return 2 / self.N * (real_part - imag_part)

    def animate(self, i):
        plot.plot(self.t, self.y)
        self.recomb += self.equation(i)
        plot.plot(self.t, self.recomb)
        plot.draw()
        plot.pause(0.0001)
        plot.clf()

    def play(self, step=100):
        for i in range(step):
            self.animate(i)


if __name__ == '__main__':
    SquareFourier().play(1000)
