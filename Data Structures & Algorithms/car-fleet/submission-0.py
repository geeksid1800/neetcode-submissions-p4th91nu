class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        It is fairly obvious we have to sort the cars basis starting position before doing
        any analysis. We also can calculate the time each car would take if it didn't collide
        with any cars ahead of it, by t[i] = (target - pos[i])/speed[i]
        We now see an approach: If a car B behind car A has t[B] <= t[A], then it would've
        reached target before A if not for being single lane, so that means it catches up at
        some point, and they travel together forming a fleet.
        Also we note that time taken by a fleet is decided by the most ahead one (i.e slowest),
        so it's t[i] is the only thing we need to retain, if we want to check if any car
        behind it is part of the same fleet.
        Approach: maintain a stack for cars, and starting from the end, calculate t[i] for
        each new car. If it is less than the car on top of the stack, they are part of the same
        fleet, and don't add it to the stack.
        Final number of elements in the stack is the # of fleets
        '''
        stk = []
        cars = []
        for pos, spd in zip(position, speed):
            cars.append({"pos":pos, "t":(target-pos)/spd})
        
        cars.sort(key = lambda c: c.get("pos"), reverse = True)
        for car in cars:
            if len(stk) == 0 or stk[-1].get("t") < car.get("t"):
                #car does not catch up to stk[-1], so it is not part of the same fleet
                stk.append(car)
        
        return len(stk)