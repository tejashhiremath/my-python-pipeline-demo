# app.py
def greet(name="World"):
    return f"Hello, {name} from Azure Pipelines on Windows!"

if __name__ == "__main__":
    message = greet()
    print(message)
    # Let's add a small check to simulate a test
    if "Azure Pipelines" in message:
        print("Greeting contains expected phrase.")
    else:
        print("Greeting does NOT contain expected phrase. This is a problem!")
        exit(1) # Exit with error code if check fails