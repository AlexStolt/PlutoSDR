
import adi




class FM:
  def __init__(self, ip='ip:192.168.3.1'):
    self.sdr = adi.Pluto(ip) 

  def rx(self, sample_rate:int, center_frequency:int, total_samples:int, gain_mode:str, gain:int, iterations:int):
    print(f'[RX]: Sample Rate[{sample_rate}], Center Frequency[{center_frequency}], Total Samples[{total_samples}], Gain[{gain}]]]')
    self.sdr.gain_control_mode_chan0 = gain_mode
    self.sdr.rx_hardwaregain_chan0 = gain
    self.sdr.rx_lo = int(center_frequency)
    self.sdr.sample_rate = int(sample_rate)
    self.sdr.rx_rf_bandwidth = int(sample_rate) 
    self.sdr.rx_buffer_size = total_samples

    # Clear RX Buffer
    for _ in range(iterations):
      self.sdr.rx()

    return self.sdr.rx()
  

  def tx_start(self, sample_rate:int, center_frequency:int, gain:int, samples:list):
    self.sdr.sample_rate = int(sample_rate)
    self.sdr.tx_rf_bandwidth = int(sample_rate)
    self.sdr.tx_lo = int(center_frequency)
    self.sdr.tx_hardwaregain_chan0 = gain
    self.sdr.tx_cyclic_buffer = True
    self.sdr.tx(samples)


  def tx_stop(self):
    self.sdr.tx_destroy_buffer()