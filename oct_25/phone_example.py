import random

NETWORK = {}  # phone number mapped to phones


class Plan:

    def __init__(self, type: str = 'GSM', data: int = 0, text: int = 0, talk: int = 0):
        self._type = type
        self._data = data
        self._text = text
        self._talk = talk

    def register(self, phone: 'CellPhone'):
        global NETWORK

        NETWORK[phone.get_phone_number()] = phone

    def can_sms(self) -> bool:
        return self._talk > 0

    def send_sms(self) -> bool:
        if self.can_sms():
            self._text -= 1
            return True

        return False

    def can_call(self, call_length) -> bool:
        return call_length <= self._talk

    def get_talk(self):
        return self._talk

    def get_text(self):
        return self._text

    def call(self, call_length) -> bool:

        if not self.can_call(call_length):
            return False

        self._talk -= call_length
        return True

    def __str__(self) -> str:
        return f"Type: {self._type} Data: {self._data} Text: {self._text} Talk: {self._talk}"


class CellPhone:

    def __init__(
        self, phone_number: str, screen_size: str, make: str, model: str,
            plan: Plan):
        self._phone_number = phone_number
        self._screen_size = screen_size
        self._make = make
        self._model = model
        self._plan = plan
        self._plan.register(self)
        self._apps = []

    def get_phone_number(self):
        return self._phone_number

    def _get_phone(self, phone_number: str):
        global NETWORK
        return NETWORK.get(phone_number)

    def send_sms(self, phone_number: str):

        if (other_phone := self._get_phone(phone_number)) is None:
            return False

        # y = 0 x ...
        # and => x
        # false => 0
        # return false and ...

        return self._plan.send_sms() and other_phone._plan.send_sms()

    def call(self, call_length, phone_number: str) -> bool:
        global NETWORK
        other_phone: CellPhone = NETWORK.get(phone_number, False)

        if not other_phone:
            return False

        if not other_phone._plan.can_call(call_length):
            return False

        if not self._plan.can_call(call_length):
            return False

        return self._plan.call(call_length) and other_phone._plan.call(call_length)

    def install_app(self, app) -> bool:
        if len(self._apps) < 10:
            self._apps.append(app)
            return True
        return False

    def uninstall_app(self, app) -> bool:
        if app in self._apps:
            self._apps.remove(app)
            return True
        return False

    def get_plan(self):
        return self._plan

    def __str__(self) -> str:
        return f"{self._make} {self._model} {self._phone_number}"


plan_a = Plan(talk=100, text=10)
plan_b = Plan(talk=100, text=10)
plan_c = Plan(talk=100, text=10)

iphone = CellPhone('123-456-7890', '5x2.5', 'Apple', 'iPhone 11', plan_a)
samsung = CellPhone('987-654-3210', '5x2.5', 'Samsung', 'Galaxy S9', plan_b)
oneplus = CellPhone('777-654-3210', '5x2.5', 'Huawei', 'One Plus', plan_c)

print('plan_a', plan_a)
print('plan_b', plan_b)
print('plan_b', plan_c)

# print('iphone', iphone)
# print('samsung', samsung)

#assert iphone.send_sms(samsung.get_phone_number())
#assert iphone.get_plan().get_text() == 9

phones = (iphone, samsung, oneplus)

for _ in range(25):
    params = {'k':2, 'population':phones}
    phone_1, phone_2 = random.sample(**params)

    print('-'*10)
    print(f'phone 1:  {phone_1} phone 2: {phone_2}')

    if not phone_1.send_sms(phone_2.get_phone_number()):
        print('Message send failure')

    print('plan_a', plan_a)
    print('plan_b', plan_b)
    print('plan_c', plan_c)


# print('-'*80)
# call_success = iphone.call(50, samsung.get_phone_number())
# if call_success:
#     print("Call succeeded")
# else:
#     print("Call failed")

# print('plan_a', plan_a)
# print('plan_b', plan_b)

# print('-'*80)
# call_success = oneplus.call(50, samsung.get_phone_number())
# if call_success:
#     print("Call succeeded")
# else:
#     print("Call failed") 
