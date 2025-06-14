class UppercaseAttributeMeta(type):
    def __new__(cls, name, bases, dct):
        for attr_name in dct:
            if not attr_name.startswith('__') and not attr_name.isupper():
                raise ValueError(f"❌ Attribute '{attr_name}' is not uppercase.")
        print(f"✅ Class '{name}' created successfully with all uppercase attributes.")
        return super().__new__(cls, name, bases, dct)

# Example usage:
class Settings(metaclass=UppercaseAttributeMeta):
    api_key = "abcdef123"
    TIMEOUT = 30
    ENABLE_LOGGING = True


print("Settings class is ready to use.")




