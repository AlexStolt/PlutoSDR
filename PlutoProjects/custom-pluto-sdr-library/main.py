from classes import FM
import numpy as np
import matplotlib.pyplot as plt

rx = {
  'sample_rate': 1e6, # Hz
  'center_frequency': 915e6, # Hz
  'gain_mode': 'manual', # "slow_attack" or "fast_attack"
  'gain': 0.0, #dB
  'total_samples': 100000,
  'iterations': 10
}

tx = {
  'sample_rate': 1e6, # Hz
  'center_frequency': 915e6, # Hz
  'gain': -50, #dB
  'samples': None, 
  # 'iterations': 10
}


if __name__ == "__main__":
  fm = FM()
  
  num_symbols = 1000
  x_int = np.random.randint(0, 4, num_symbols) # 0 to 3
  x_degrees = x_int*360/4.0 + 45 # 45, 135, 225, 315 degrees
  x_radians = x_degrees*np.pi/180.0 # sin() and cos() takes in radians
  x_symbols = np.cos(x_radians) + 1j*np.sin(x_radians) # this produces our QPSK complex symbols
  samples = np.repeat(x_symbols, 16) # 16 samples per symbol (rectangular pulses)
  samples *= 2**14 # The PlutoSDR expects samples to be between -2^14 and +2^14, not -1 and +1 like some SDRs
  tx['samples'] = samples
  
  fm.tx_start(**tx)


  rx_samples = fm.rx(**rx)

  fm.tx_stop()
  print(rx_samples)


  plt.figure(0)
  plt.plot(np.real(rx_samples[::100]))
  plt.plot(np.imag(rx_samples[::100]))
  plt.xlabel("Time")

  plt.figure(1)
  plt.plot(np.real(samples[::100]))
  plt.plot(np.imag(samples[::100]))
  plt.xlabel("Time")
  plt.show()




print('hello')