import random
import time
import asyncio
from autobahn.twisted.wamp import ApplicationRunner

BARBER_SLEEP_TIME = 5
MAX_WAITING_TIME = 10
NUM_CHAIRS = 3

class BarberShop:
    def __init__(self):
        self.customers = []
        self.num_waiting = 0

    def add_customer(self, customer_id):
        if self.num_waiting < NUM_CHAIRS:
            self.customers.append(customer_id)
            self.num_waiting += 1
            print(f"Customer {customer_id} is waiting in the waiting room.")
            return True
        else:
            print(f"No chairs available for customer {customer_id}.")
            return False

    def remove_customer(self, customer_id):
        if customer_id in self.customers:
            self.customers.remove(customer_id)
            self.num_waiting -= 1
            print(f"Customer {customer_id} has left the barbershop.")
            return True
        else:
            print(f"Customer {customer_id} is not in the waiting room.")
            return False

    def get_waiting_customers(self):
        return self.customers

async def simulate_customer(barbershop, customer_id):
    if barbershop.add_customer(customer_id):
        print(f"Customer {customer_id} wakes the barber.")
        # Call the "cut_hair" procedure on the Crossbar server to simulate the barber cutting the hair
        await runner.call("com.barbershop.cut_hair", customer_id)
        barbershop.remove_customer(customer_id)
    else:
        print(f"Customer {customer_id} leaves without a haircut.")

def run_barbershop():
    barbershop = BarberShop()

    async def on_join(session, details):
        print(f"Client {session.id} has joined the barbershop.")

    async def on_leave(session, details):
        print(f"Client {session.id} has left the barbershop.")

    async def cut_hair(session, customer_id):
        print(f"Barber is cutting the hair of customer {customer_id}.")
        time.sleep(BARBER_SLEEP_TIME)
        print(f"Barber has finished cutting the hair of customer {customer_id}.")
        # Publish a message to the Crossbar server to inform all clients that the haircut is finished
        await runner.publish("com.barbershop.haircut_finished", customer_id)

    async def on_haircut_finished(session, customer_id):
        print(f"Customer {customer_id} has finished their haircut.")
        # Simulate the departure of the customer from the barbershop
        await simulate_customer(barbershop, customer_id)

    async def spawn_customer():
        # Generate a random ID for the new customer
        customer_id = random.randint(1, 1000)
        # Call the "simulate_customer" procedure on the Crossbar server to simulate the arrival of a new customer
        await runner.call("com.barbershop.simulate_customer", barbershop, customer_id)

    async def spawn_customers():
        while True:
            # Generate a random waiting time for the new customer
            waiting_time = random.randint(1, MAX_WAITING_TIME)
            # Wait for the specified amount of time
            await asyncio.sleep(waiting_time)
            # Spawn a new customer
            await spawn_customer()

    runner = ApplicationRunner(url="ws://localhost:8080/ws", realm="realm1")
    runner.run({
        "on_join": on_join,
        "on_leave": on_leave,
        "com.barbershop.cut_hair": cut_hair,
        "com.barbershop.haircut_finished": on_haircut_finished,
        })

if __name__ == '__main__':
    run_barbershop()
