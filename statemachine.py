class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.step_counter = 0

    def add_state(self, name, handler):
        self.handlers[name] = handler

    def set_start(self, name):
        self.startState = name

    def run(self, cargo, num_steps):
        self.step_counter = 0
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")

        visited = [self.startState]

        while True:
            (newState, cargo) = handler(cargo)
            self.step_counter = self.step_counter + 1
            visited.append(newState)
            if self.step_counter == num_steps:
                if newState == self.startState:
                    print("valid siteswap")
                    for state in visited:
                        print(state)
                else:
                    print("invalid siteswap")
                    for state in visited:
                        print(state)
                break
            else:
                handler = self.handlers[newState]


