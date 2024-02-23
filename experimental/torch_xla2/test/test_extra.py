import unittest
import torch
import torch.nn.functional as F
import jax
import torch_xla2
from torch_xla2 import tensor, extra


class ExtraTest(unittest.TestCase):

  def setUp(self):
    torch.manual_seed(0)

  def test_fori_loop(self):
    a = tensor.move_to_device(torch.ones((10, 10)))

    def body(i, c):
      return c + a[i]

    init_val = tensor.move_to_device(torch.zeros(10))
    res = extra.fori_loop(0, 10, body, init_val)

    expect = torch.ones(10) * 10

    self.assertTrue(torch.allclose(tensor.j2t(res._elem), expect))


if __name__ == '__main__':
  unittest.main()
