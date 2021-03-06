test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> stans_car = Car('Tesla', 'Model S')
          >>> stans_car.model
          066daa99c4c14fba33ca7fea6de5139e
          # locked
          >>> stans_car.gas = 10
          >>> stans_car.drive()
          6782dfbb8a7616b3f504afa7bdbc4efe
          # locked
          >>> stans_car.drive()
          8e18dc54497447151e91747068c581ce
          # locked
          >>> stans_car.fill_gas()
          b2a03f7caa4dde07c2acd64a249d03c9
          # locked
          >>> stans_car.gas
          e0c9124d3360b0721b517ec33d41b017
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> stans_car = Car('Tesla', 'Model S')
          >>> Car.headlights
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> stans_car.headlights
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> Car.headlights = 3
          >>> stans_car.headlights
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          >>> stans_car.headlights = 2
          >>> Car.headlights
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> stans_car = Car('Tesla', 'Model S')
          >>> stans_car.wheels = 2
          >>> stans_car.wheels
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> Car.num_wheels
          612ff2a71cad53bc4c7f85fac678a06d
          # locked
          >>> stans_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          8e18dc54497447151e91747068c581ce
          # locked
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          8a2fd4e4c3c6dcce2dc631af62ee217a
          # locked
          >>> Car.drive(stans_car) # Type Error if an error occurs and Nothing if nothing is displayed
          8e18dc54497447151e91747068c581ce
          # locked
          >>> MonsterTruck.drive(stans_car) # Type Error if an error occurs and Nothing if nothing is displayed
          8a2fd4e4c3c6dcce2dc631af62ee217a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> kevins_car = MonsterTruck('Monster', 'Batmobile')
          >>> kevins_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          543d3c4044c7b885e6bc773187315cb9
          2e96bc0878a8a5a4b77deec4ef4b3d09
          # locked
          >>> Car.drive(kevins_car) # Type Error if an error occurs and Nothing if nothing is displayed
          2e96bc0878a8a5a4b77deec4ef4b3d09
          # locked
          >>> MonsterTruck.drive(kevins_car) # Type Error if an error occurs and Nothing if nothing is displayed
          543d3c4044c7b885e6bc773187315cb9
          2e96bc0878a8a5a4b77deec4ef4b3d09
          # locked
          >>> Car.rev(kevins_car) # Type Error if an error occurs and Nothing if nothing is displayed
          8a2fd4e4c3c6dcce2dc631af62ee217a
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> class FoodTruck(MonsterTruck):
          ...    delicious = 'meh'
          ...    def serve(self):
          ...        if FoodTruck.size == 'delicious':
          ...            print('Yum!')
          ...        if self.food != 'Tacos':
          ...            return 'But no tacos...'
          ...        else:
          ...            return 'Mmm!'
          >>> taco_truck = FoodTruck('Tacos', 'Truck')
          >>> taco_truck.food = 'Guacamole'
          >>> taco_truck.serve() # Type Error if an error occurs and Nothing if nothing is displayed
          e076e15f27097db8c1e27601ac471441
          # locked
          >>> taco_truck.food = taco_truck.make
          >>> FoodTruck.size = taco_truck.delicious
          >>> taco_truck.serve() # Type Error if an error occurs and Nothing if nothing is displayed
          cda23c7687a29f0644375d5e0251e70b
          # locked
          >>> taco_truck.size = 'delicious'
          >>> taco_truck.serve() # Type Error if an error occurs and Nothing if nothing is displayed
          cda23c7687a29f0644375d5e0251e70b
          # locked
          >>> FoodTruck.pop_tire() # Type Error if an error occurs and Nothing if nothing is displayed
          8a2fd4e4c3c6dcce2dc631af62ee217a
          # locked
          >>> FoodTruck.pop_tire(taco_truck) # Type Error if an error occurs and Nothing if nothing is displayed
          1bc84be8d31d6e15063845bc7f2f5a49
          # locked
          >>> taco_truck.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          543d3c4044c7b885e6bc773187315cb9
          1263d1e44258ea466c7bca14cf0dced1
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
