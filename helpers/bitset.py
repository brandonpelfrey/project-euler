class Bitset:
  def __init__(self, maxn, bucketSize=32):
    self.maxn = maxn
    self.bucket_bits = bucketSize
    self.bits = [0] * ( (maxn // bucketSize) + 1)

  def get(self, i):
    m = i // self.bucket_bits
    bucket_index = i - m * self.bucket_bits
    B = self.bits[ m ]
    return (B >> bucket_index) & 1

  def set(self, i):
    m = i // self.bucket_bits
    bucket_index = i - m * self.bucket_bits
    self.bits[m] |= (1 <<bucket_index)
