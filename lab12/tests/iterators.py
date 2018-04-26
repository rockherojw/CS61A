test = {
  'name': 'Iterators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [1, [2, [3, [4]]]]
          >>> t = iter(s)
          >>> next(t)
          f313ff1ce5644f8b5465a3f45b4f19a4
          # locked
          >>> next(iter(next(t)))
          b764c5386326cd8ae89e4efe0c923e84
          # locked
          >>> list(t)
          51aeb8a2421466b190e142710b05b9b7
          # locked
          >>> next(map(lambda x: x * x, filter(lambda y: y > 4, range(10))))
          bfdc51fa90d1fa734913a175c022e92a
          # locked
          >>> tuple(map(abs, reversed(range(-6, -4))))
          682858d173a314422106935922aab666
          # locked
          >>> r = reversed(range(10000))
          >>> next(r) - next(r)
          f313ff1ce5644f8b5465a3f45b4f19a4
          # locked
          >>> xs = [2, 3, 4, 5]
          >>> y, z = iter(xs), iter(xs)
          >>> next(zip(y, z))
          cb99954a20b7bbed4d0df262150b5aa6
          # locked
          >>> next(zip(y, y))
          d659b1e0fdf3ed3faff3cedfff1270e4
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
