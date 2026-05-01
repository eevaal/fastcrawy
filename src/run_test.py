from fastpoint import fp

@fp.endpoint("GET", tags=["FastPoint GET Test"])
def get_test():
    payload = {
        "test": "test",
        "test2": "test2",
        "test3": "test3",
        "test4": "test4",
        "test5": "test5",
        "test6": "test6",
        "test7": "test7"
    }
    return payload

@fp.endpoint("/post-test", "POST", tags=["FastPoint POST Test"])
async def post_test():
    ...

if __name__ == "__main__":
    fp.run()
