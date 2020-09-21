from locust import HttpUser, task, between, TaskSet


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before 
            any task is scheduled
        """
        self.login()

    def login(self):
        self.client.post("/customer/login",
                         {
                             "customerEmail": "saul.quispe@eigital.com",
                             "merchantId": "5e81988515931d001e28c8d0",
                             "password": "a",
                             "storeId": "5e81988515931d001e28c8d1"
                         })

    @task(1)
    def index(self):
        self.client.get(
            "/customer?merchantId=5e81988515931d001e28c8d0&storeId=5e81988515931d001e28c8d1&customerId=5f516fec212b55001d0c9fd4")

    @task(1)
    def index2(self):
        self.client.get(
            "/tax?merchantId=5e81988515931d001e28c8d0&storeId=5e81988515931d001e28c8d1")
    
    @task(1)
    def index3(self):
        self.client.get(
            "/order?merchantId=5e81988515931d001e28c8d0&orderId=5f68b1806d788a001b77baaa")

    @task(1)
    def index4(self):
        self.client.get(
            "/Payment?merchantId=5e81988515931d001e28c8d0&storeId=5e81988515931d001e28c8d1&orderId=5f68b1806d788a001b77baaa")



class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 5000
    max_wait = 9000
    host = "https://api.orderos.net"