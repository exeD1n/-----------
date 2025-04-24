from locust import HttpUser , SequentialTaskSet, task, between

class UserBehavior(SequentialTaskSet):
        
    @task
    def load_homepage(self):
        self.client.get("http://127.0.0.1:8000/categories/")

class WebsiteUser (HttpUser ):
    tasks = [UserBehavior] 
    wait_time = between(1, 5)  # Время ожидания между запросами
    