from abc import ABC, abstractmethod
class Coffee(ABC):
    """Abstract class – defines the blueprint for every coffee."""

    def __init__(self, name, size="Medium"):
        self._name = name          
        self._size = size

    @abstractmethod
    def make(self):
        """Every subclass MUST implement how the coffee is made."""
        pass

    @abstractmethod
    def display(self):
        """Every subclass MUST implement its own hash-art image."""
        pass

    def info(self):
        print(f"\n☕  {self._name}  |  Size: {self._size}")
        print("—" * 35)
class Latte(Coffee):
    def __init__(self, size="Medium"):
        super().__init__("Latte", size)
        self.__recipe = ["Espresso (1 shot)", "Steamed Milk (200ml)", "Milk Foam (1 tbsp)"]

    def make(self):
        print("Recipe:")
        for step in self.__recipe: 
            print(f"  + {step}")

    def display(self):
        print("""
        ( (
         ) )
      .........
      |  LATTE |
      |  ~   ~ |
      |________|
        """)
class Mocha(Coffee):
    def __init__(self, size="Medium"):
        super().__init__("Mocha", size)
        self.__recipe = ["Espresso (1 shot)", "Chocolate Syrup (2 tbsp)", "Steamed Milk (150ml)", "Whipped Cream"]

    def make(self):
        print("Recipe:")
        for step in self.__recipe:
            print(f"  + {step}")

    def display(self):
        print("""
        ) )
       ( (
      .........
      | MOCHA  |
      | ♥♥♥♥♥ |
      |________|
        """)
class Espresso(Coffee):
    def __init__(self, size="Small"):
        super().__init__("Espresso", size)
        self.__recipe = ["Finely Ground Coffee (7g)", "Hot Water (30ml) at 90°C"]

    def make(self):
        print("Recipe:")
        for step in self.__recipe:
            print(f"  + {step}")

    def display(self):
        print("""
          ( (
           ) )
         .....
         |ESP|
         |***|
         |___|
        """)

class Cappuccino(Coffee):
    def __init__(self, size="Medium"):
        super().__init__("Cappuccino", size)
        self.__recipe = ["Espresso (1 shot)", "Steamed Milk (100ml)", "Thick Milk Foam (100ml)", "Cinnamon Powder"]

    def make(self):
        print("Recipe:")
        for step in self.__recipe:
            print(f"  + {step}")

    def display(self):
        print("""
       (   (
        ) )
      .........
      |CAPPUCC.||
      | ~~~~~ |
      |________|
        """)

class CoffeeMachine:
    """Simulates the coffee machine – takes order and serves coffee."""

    MENU = {
        "1": ("Latte",      Latte),
        "2": ("Mocha",      Mocha),
        "3": ("Espresso",   Espresso),
        "4": ("Cappuccino", Cappuccino),
    }

    def run(self):
        print("\n" + "=" * 35)
        print("   ☕  WELCOME TO COFFEE MACHINE  ☕")
        print("=" * 35)

        while True:
            print("\nMENU:")
            for key, (name, _) in self.MENU.items():
                print(f"  [{key}] {name}")
            print("  [0] Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "0":
                print("\nThank you! Enjoy your coffee. ☕\n")
                break
            elif choice in self.MENU:
                name, CoffeeClass = self.MENU[choice]
                size = input("Size (Small / Medium / Large): ").strip() or "Medium"
                coffee = CoffeeClass(size) 
                coffee.display()
                coffee.info()
                coffee.make()
            else:
                print("❌ Invalid choice. Try again.")
if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.run()