from fastcrawy import FastCrawyEngine

fc = FastCrawyEngine()

@fc.endpoint("/", "GET", tags=["FastCrawy Test"])
def run_test():
    return {"Hello": "World"}

if __name__ == "__main__":
    fc.run()