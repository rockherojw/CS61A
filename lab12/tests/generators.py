test = {
  'name': 'Generators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def generator():
          ...     print("Starting here")
          ...     i = 0
          ...     while i < 6:
          ...         print("Before yield")
          ...         yield i
          ...         print("After yield")
          ...         i += 1
          >>> g = generator() # what type of object is this?
          >>> g == iter(g) # equivalent of g.__iter__()
          82c490a4e7f75417498f49c2f5b931e9
          # locked
          >>> next(g) # equivalent of g.__next__()
          9949da3a235d5b5324216c6a00e59408
          de0c21b02984c497e03f938faf87ada1
          9f1d47b7661f1fe12f3d6f8c0633a346
          # locked
          >>> next(g)
          3408c9bfa64e952d781b68b03e965d1b
          de0c21b02984c497e03f938faf87ada1
          f313ff1ce5644f8b5465a3f45b4f19a4
          # locked
          >>> next(g)
          3408c9bfa64e952d781b68b03e965d1b
          de0c21b02984c497e03f938faf87ada1
          b764c5386326cd8ae89e4efe0c923e84
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
