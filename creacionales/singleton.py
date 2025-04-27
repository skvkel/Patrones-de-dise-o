from threading import Lock, Thread


class Singleton(type):

    _instance = {}
    _lock_singleton: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        # Acquire lock
        with cls._lock_singleton:
            print(f"Trying instance with value {args[0]}")
            # Is instance is not created
            if cls not in cls._instance:
                print(f"Creating instance with value {args[0]}")
                # Create instance and store him in class envvar
                instance = super().__call__(*args, **kwargs)
                cls._instance[cls] = instance
            else:
                print(f"Instance already exist. Returning instance {cls._instance[cls]}")
        return cls._instance[cls]


class MySingletonWithClassValue(metaclass=Singleton):
    # We have a class value, that will be used for all instances.
    # If we instance with 2 different values, the first one will not be overwritten

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self): ...


def singleton_class_value(value: str) -> None:
    singleton = MySingletonWithClassValue(value)
    print(f"Value of instacen attribue: {singleton.value}")


if __name__ == "__main__":

    process1 = Thread(target=singleton_class_value, args=("FIRST",))
    process2 = Thread(target=singleton_class_value, args=("SECOND",))
    process1.start()
    process2.start()
    process1.join()
    process2.join()

