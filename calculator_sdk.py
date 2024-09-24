import requests

class CalculatorSDK:
    '''
    This is the class which contains the methods for calling each of the API endpoints.
    '''
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url
    
    def add(self, a, b):
        """
        This is the Add feature which adds two numbers
        """
        response = requests.get(f"{self.base_url}/add/", params={"a": a, "b": b})
        return response.json()
    
    def subtract(self, a, b):
        """
        This is the Subtract feature which subtract two numbers.
        """
        response = requests.get(f"{self.base_url}/sub/", params={"a": a, "b": b})
        return response.json()
    
    def multiply(self, a, b):
        """
        This is the Multiply feature which multiplies two numbers.
        """
        response = requests.get(f"{self.base_url}/mul/", params={"a": a, "b": b})
        return response.json()
    
    def divide(self, a, b):
        """
        This is the Divide feature which divides two numbers. Divide by zero is handled.
        """
        response = requests.get(f"{self.base_url}/div/", params={"a": a, "b": b})
        print (f"The response is {response}")
        if (response.status_code != 200):
            raise Exception(response.json())
        return response.json()
    

# calculator =     CalculatorSDK()

# result = calculator.add(2,3)
# print(f'The addition is {result}')

# result = calculator.div(2,0)
# print(f'The division is {result}')
